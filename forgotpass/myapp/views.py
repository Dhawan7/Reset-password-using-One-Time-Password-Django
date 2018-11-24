from django.shortcuts import render
from .forms import regForm,regform1
import requests
import random
from django.http import HttpResponse
from .models import reg
from django.contrib.auth.models import User
from django.contrib.auth import login
def regView(request):
    form = regForm()
    form1 = regform1()
    if request.method == 'POST':
        form = regForm(data=request.POST)
        form1 = regform1(data=request.POST)

        if form.is_valid() and form1.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()

            profile = form1.save(commit = False)
            profile.user = user
            profile.save()
            return HttpResponse('Register Successfully!!!')

    return render(request,'index.html',{'form':form,'form1':form1})

def reset(request):
    if request.method == 'POST':
        username = request.POST['fuser']
        password = request.POST['password']
        cpass = request.POST['cpass']
        if password != cpass:
            response = 'Password Does Not Match!!!'
        else:
            getUser = User.objects.get(username=username)
            getUser.set_password(password)
            response='Password Changed Successfully!!!'
        return render(request,'reset.html',{'r':response})
    return render(request,'reset.html')

def gotp(request):
    otp = random.randint(10000,99999)
    ruser = request.GET['user']
    chkUser = User.objects.filter(username__iexact=ruser)
    if len(chkUser)!=0:
        for i in chkUser:
            uid = i.id
        getUser = reg.objects.get(user_id=uid)
        number= str(getUser.contact)
        message = "{} is your One Time Password for reset your password \n Don't share it with anyone".format(otp)
        genOtp = requests.get('http://api.textlocal.in/send/?username=YOUR USERNAME&hash=YOUR HASH KEY&message='+message+'&sender=TXTLCL&numbers='+number+'&test=0')
        snumber = number.replace(number[:6],'******')
        print(otp)
        msz = ['An OTP sent to your {} mobile number @'.format(snumber),otp]
        return HttpResponse(msz)
    else:
        return HttpResponse('Please Enter a Correct Username')
