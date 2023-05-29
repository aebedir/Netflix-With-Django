from django.shortcuts import render ,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import *
# Create your views here.

def userRegister(request):
    if request.method == 'POST':
        kullanici = request.POST['kullanici']
        email = request.POST['email']
        resim = request.FILES['resim']
        telefon = request.POST['telefon']
        sifre = request.POST['sifre1']
        sifre2 = request.POST['sifre2']

        if sifre == sifre2:
            if User.objects.filter(username = kullanici).exists():
                messages.error(request,'Kullanıcı Adı Mevcut')
            elif User.objects.filter(email = email).exists():
                messages.error(request,'Email daha önce kullanılmış')
            elif len(sifre)<6:
                messages.error(request,'Şifre 6 karakterden uzun olmalıdır')
            elif kullanici.lower() in sifre.lower():
                messages.error(request,'Kullanıcı adı ile şifre benzer olamaz')
            else:
                user = User.objects.create_user(
                    username = kullanici,
                    email = email,
                    password=sifre
                )
                Hesap.objects.create(
                    user = user,
                    resim = resim,
                    telefon = telefon
                )
                user.save()
                messages.success(request,'Kayıt Başarılı , Giriş Yapabilirsiniz')
                return redirect('login')
        else:
            messages.error(request,'Şifreler Uyuşmuyor')
    return render(request,'register.html')

def userLogin(request):
    if request.method=='POST':
        kullanici = request.POST['kullanici']
        sifre = request.POST['sifre']

        user = authenticate(request,username=kullanici,password=sifre)

        if user is not None:
            login(request,user)
            messages.success(request,'Giriş Başarıyla Yapıldı')
            return redirect('profiles')
        else:
            messages.error(request,'Kullanıcı adı veya şifre hatalı')
            return redirect('login')
    return render(request,'login.html')

@login_required(login_url='login')
def profiles(request):
    profiller = Profile.objects.filter(user=request.user)
    context = {
        'profiller':profiller
    }
    return render(request,'browse.html',context)


@login_required(login_url='login')
def create_profile(request):
    form = ProfileForm()
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            if Profile.objects.filter(user=request.user).count() < 4:                
                newProfile = form.save(commit=False)
                newProfile.user = request.user
                newProfile.save()
                messages.success(request,'Profil Oluşturuldu')
                return redirect('profiles')
            else:
                messages.warning(request,'En fazla 4 profil oluşturabilirsiniz')
                return redirect('profiles')
    context={
        'form':form
    }
    return render(request,'create-profile.html',context)

def hesap(request):
    profil = request.user.hesap
    context = {
        'profil':profil
    }
    return render(request,'hesap.html',context)