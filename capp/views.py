import os

from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from .forms import *
from cproject.settings import EMAIL_HOST_USER


# Create your views here.

def index(request):
    return render(request,'index.html')

# def login(request):
#     return render(request, 'login.html')

# def register(request):
#     return render(request, 'registration.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def job(request):
    return render(request, 'job-listing.html')

def blog(request):
    return render(request, 'blog.html')

def team(request):
    return render(request, 'team.html')

def terms(request):
    return render(request, 'terms.html')

def testimonials(request):
    return render(request, 'testimonials.html')

def register(request):
    if request.method=='POST':
        a = regform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['companyname']
            em = a.cleaned_data['email']
            ph = a.cleaned_data['number']
            ps = a.cleaned_data['password']
            cp = a.cleaned_data['cpassword']
            ad = a.cleaned_data['address']
            if ps==cp:
                b = regmodel(companyname=nm, email=em, number=ph, password=ps, address=ad)
                b.save()
                return HttpResponse("Registration Success....")
            else:
                return HttpResponse("Incorrect Password!")
        else:
            return HttpResponse("Registration Failed!")
    else:
        return render(request,'registration.html')

def login(request):
    if request.method == 'POST':
        a = logform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = regmodel.objects.all()
            for i in b:
                cmp = i.companyname
                request.session['companyname']=cmp
                id = i.id
                if i.email == em and i.password == ps:
                    # return HttpResponse("Login Success")
                    return render(request, 'profile.html',{'cmp':cmp, 'id':id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'login.html')

# def nav(request):
#     return render(request, 'navbar.html')
#
# def footer(request):
#     return render(request, 'footer.html')

def profile(request):
    return render(request, 'profile.html')

def vacancy(request, id):
    b = regmodel.objects.get(id=id)
    cn = b.companyname
    el = b.email
    if request.method=='POST':
        a = upform(request.POST)
        if a.is_valid():
            nm = a.cleaned_data['cname']
            em = a.cleaned_data['email']
            jt = a.cleaned_data['jtitle']
            jp = a.cleaned_data['jtype']
            wt = a.cleaned_data['wtype']
            ex = a.cleaned_data['exp']
            ql = a.cleaned_data['qualify']
            b = addmodel(cname=nm, email=em, jtitle=jt, jtype=jp, wtype=wt, exp=ex, qualify=ql)
            b.save()
            # return redirect(vacancydis)
            return HttpResponse("Upload Success....")
        else:
            return HttpResponse("Upload Failed!")
    else:
        return render(request,'vacancyupload.html', {'cn':cn, 'el':el})

def vacancydis(request):
    x = addmodel.objects.all()
    b = request.session['companyname']
    return render(request,'vacancysuccess.html', {'a':x, 'b':b})

def vacancyedit(request, id):
    a = addmodel.objects.get(id=id)
    if request.method == 'POST':
        a.name = request.POST.get('cname')
        a.email = request.POST.get('email')
        a.jtitle = request.POST.get('jtitle')
        a.jtype = request.POST.get('jtype')
        a.wtype = request.POST.get('wtype')
        a.exp = request.POST.get('exp')
        a.qualify = request.POST.get('qualify')
        a.save()
        return redirect(vacancydis)
    return render(request, 'vacancyedit.html', {'x': a})

def vacancydel(request, id):
    a = addmodel.objects.get(id=id)
    a.delete()
    return redirect(vacancydis)

def uregister(request):
    if request.method=='POST':
           un=request.POST.get("username")
           fn=request.POST.get("first_name")
           ln=request.POST.get("last_name")
           em=request.POST.get("email")
           ps=request.POST.get("password")
           cps=request.POST.get("cpassword")
           if ps==cps:
                b = User(username=un, first_name=fn, last_name=ln, email=em, password=ps)
                b.save()
                return redirect(ulogin)
           else:
               return HttpResponse("Registration Failed!")
    else:
        return render(request,'userregis.html')


def ulogin(request):
    if request.method == 'POST':
        a = ulogform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ps = a.cleaned_data['password']
            b = User.objects.all()
            for i in b:
                usr = i.username

                if i.email == em and i.password == ps:
                    id=i.id
                    request.session['id']=i.id
                    # return HttpResponse("Login Success")
                    return render(request, 'userprofile.html',{'usr':usr, 'id':id})
            else:
                return HttpResponse("Login failed")
    else:
        return render(request, 'userlogin.html')


def vacancyapply(request):
    x = addmodel.objects.all()
    return render(request,'vacancyapply.html', {'a':x})

def viewusers(request):
    x = User.objects.all()
    return render(request, 'viewusers.html', {'a': x})

def useredit(request, id):
    a = User.objects.get(id=id)
    if request.method == 'POST':
        a.username = request.POST.get("username")
        a.first_name = request.POST.get("first_name")
        a.last_name = request.POST.get("last_name")
        a.email = request.POST.get("email")
        # a.password = request.POST.get("password")
        a.save()
        return redirect(viewusers)
    return render(request, 'useredit.html', {'x': a})

def userdel(request, id):
    a = User.objects.get(id=id)
    a.delete()
    return render(request, 'userprofiledisplay.html')
def userdetails(request, id):
    b = User.objects.get(id=id)
    fn = b.first_name
    ln = b.last_name
    el = b.email
    if request.method == 'POST':
        a = userprofileform(request.POST, request.FILES)
        if a.is_valid():
            ig = a.cleaned_data['image']
            nm = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            re = a.cleaned_data['resume']
            ql = a.cleaned_data['qualify']
            ex = a.cleaned_data['exp']
            ad = a.cleaned_data['address']
            ph = a.cleaned_data['phone']
            id=request.session['id']
            b = userprofilemodel(uid=id,image=ig, fname=nm, email=em, resume=re, qualify=ql, exp=ex, address=ad, phone=ph)
            b.save()
            # return HttpResponse("Details Uploaded Successfully...")
            return render(request, 'userprofiledisplay.html')
        else:
            return HttpResponse("Details Upload failed!")
    return render(request, 'userprofiledetails.html', {'fn':fn, 'ln':ln, 'el':el})


def userdisplay(request,id):
    a = userprofilemodel.objects.all()

    li = []  # image.png
    fname = []  # xyz
    email = []
    li2 = []
    qualify = []
    exp = []
    address = []
    phone = []
    id = []
    uid=[]
    for i in a:
        ui=i.uid
        uid.append(ui)
        id1 = i.id
        id.append(id1)
        img = i.image  # '[New_App/static/image.png]'
        li.append(str(img).split('/')[-1])
        nm = i.fname
        em = i.email
        re = i.resume
        li2.append(str(re).split('/')[-1])
        ql = i.qualify
        ex = i.exp
        ad = i.address
        ph = i.phone
        fname.append(nm)
        email.append(em)
        qualify.append(ql)
        exp.append(ex)
        address.append(ad)
        phone.append(ph)
    kk=request.session['id']
    print(kk)
    print(uid)
    mylist = zip(li, fname, email, li2, qualify, exp, address, phone, id,uid)  # [(name.png, xyz, ...) , (name2, abc, ...)]
    return render(request, 'userprofiledisplay.html', {'list': mylist,'kk':kk})


def edituserdetails(request, id):
    a = userprofilemodel.objects.get(id=id)
    image = str(a.image).split('/')[-1]
    resume = str(a.resume).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(a.image) >0:
                os.remove(a.image.path)
            a.image = request.FILES['image']
            if len(a.resume) >0:
                os.remove(a.resume.path)
            a.resume = request.FILES['resume']
        a.name = request.POST.get('fname')
        a.email = request.POST.get('email')
        a.qualify = request.POST.get('qualify')
        a.exp = request.POST.get('exp')
        a.address = request.POST.get('address')
        a.phone = request.POST.get('phone')
        a.save()
        return render(request, 'userlogin.html')
    return render(request, 'edituserdetails.html',{'a':a, 'image':image, 'resume':resume})


def deleteuserdetails(request, id):
    a = userprofilemodel.objects.get(id=id)
    if len(a.image)>0:
        os.remove(a.image.path)
    if len(a.resume)>0:
        os.remove(a.resume.path)
    a.delete()
    return render(request, 'userlogin.html')

def jobapply(request, id):
    a = addmodel.objects.get(id=id)
    cm = a.cname
    jb = a.jtitle
    if request.method == 'POST':
        a = jobapplyform(request.POST,request.FILES)
        if a.is_valid():
            cn = a.cleaned_data['cname']
            jt = a.cleaned_data['jtitle']
            nm = a.cleaned_data['fname']
            em = a.cleaned_data['email']
            re = a.cleaned_data['resume']
            b = jobapplymodel(cname=cn, jtitle=jt, fname=nm, email=em, resume=re)
            b.save()
            subject = f"New job applied to {cn}"
            message = f"hi {nm}\n your application for {jt} is applied successfully"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            # return HttpResponse("Details Uploaded Successfully...")
            return render(request, 'applysuccess.html')
        else:
            return HttpResponse("Details Upload failed!")
    return render(request, 'jobapply.html', {'cm': cm, 'jb': jb})


def wishlist(request,id):
    a = addmodel.objects.get(id=id)
    b = wishlistmodel(cname=a.cname,email=a.email,jtitle=a.jtitle,jtype=a.jtype,wtype=a.wtype,exp=a.exp,qualify=a.qualify)
    b.save()
    # return HttpResponse("Job added to wishlist")
    return redirect(wishdisplay)

def wishdisplay(request):
    a = wishlistmodel.objects.all()
    return render(request, 'wishlistdisplay.html', {'a': a})

def wishdelete(request,id):
    a = wishlistmodel.objects.get(id=id)
    a.delete()
    return redirect(wishdisplay)

def displayappliedusers(request, id):
    a = jobapplymodel.objects.all()
    b = request.session['companyname']
    cname = []
    jtitle = []
    fname = []
    email = []
    resume1 = []
    id1 = []
    for i in a:
        id = i.id
        id1.append(id)
        cn = i.cname
        jt = i.jtitle
        nm = i.fname
        em = i.email
        re = i.resume
        cname.append(cn)
        jtitle.append(jt)
        fname.append(nm)
        email.append(em)
        resume1.append(str(re).split('/')[-1])
    mylist = zip(cname, jtitle, fname, email, resume1, id1)
    return render(request, 'displayappliedusers.html', {'list': mylist, 'b':b})


def success(request):
    return render(request, 'applicationsuccess.html')


def email(request, id):
    a = jobapplymodel.objects.get(id=id)
    ems = a.email
    cn = a.cname
    if request.method == 'POST':
        a = emailform(request.POST)
        if a.is_valid():
            em = a.cleaned_data['email']
            ms = a.cleaned_data['message']
            subject = f"{cn}"
            message = f"{ms}"
            email_from = EMAIL_HOST_USER
            send_mail(subject, message, email_from, [em])
            # return HttpResponse("Details Uploaded Successfully...")
            return render(request, 'applicationsuccess.html')
        else:
            return HttpResponse("Details Upload failed!")
    return render(request, 'email.html', {'em': ems})


def deleteapuser(request, id):
    a = jobapplymodel.objects.get(id=id)
    a.delete()
    return redirect(displayappliedusers)

