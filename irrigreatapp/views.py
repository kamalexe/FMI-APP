from django.shortcuts import render,HttpResponse,redirect, reverse
from fmiapp.models import FarmerInfo,MerchantInfo
from django.http import HttpResponseRedirect
import random
from .models import SmUser,SmUserProfile,Post
from datetime import datetime
# Create your views here.

def bloghome(request):
    print('blogHome')
    global username
    try:
        print(request.session['smUser'])
        if request.session['smUser']:
            userid = SmUser.objects.get(email=request.session['smUser'])
            username = SmUserProfile.objects.get(email=request.session['smUser'])
        allSmUser = SmUserProfile.objects.all().order_by('?')[:3]
        post = Post.objects.filter(user_id = username.id)
        path = request.path_info
        context = {'userid':userid,'username': username,'allSmUser':allSmUser,'post':post,'path':path}
        # return render(request, 'bloghome.html', context)
        return render(request, 'bloghome.html',context)
    except Exception as e:
        print(e)
    return render(request, 'sm_login.html')

def smRegView(request):
    return render(request, 'sm_reg.html')

def smReg(request):
    print(request.method)
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    bdate = request.POST.get('bdate')
    gender = request.POST.get('gender')
    updateDate = datetime.now()
    creatDate = datetime.now()
    sm_user = SmUser(fname=fname,lname=lname,email=email,password=password,bdate=bdate,gender=gender,updateDate=updateDate,creatDate=creatDate)
    sm_user.save()

    username = SmUser.objects.get(email = email,password=password)
    id = username.id
    user_id = username.id
    # user_id = request.POST.get('user_id')
    fname = fname
    lname = lname
    email = email
    password = password
    bdate = bdate
    gender = gender
    updateDate = datetime.now()
    creatDate = datetime.now()
    SmUserProfileObj = SmUserProfile(id=id,user_id=user_id,fname=fname,lname=lname, email= email,password=password, bdate= bdate,gender=gender,updateDate=updateDate,creatDate=creatDate)
    SmUserProfileObj.save()
    # return HttpResponse('reg')
    return render(request, 'sm_login.html')

def smLoginView(request):
    return render(request, 'sm_login.html')

def smLogin(request):
    try:
        email = request.POST.get('email')
        password = request.POST.get('password')
        sm_user = SmUser.objects.get(email = email,password=password)
        request.session['smUser'] = email
        return redirect(reverse('irrigreatapp:bloghome'))
    except:
        return redirect(reverse('irrigreatapp:smRegView'))

def smProfile(request):
    if request.session['smUser']:
        # username = FarmerInfo.objects.get(userid=request.session['farmer'])
        username = SmUser.objects.get(email=request.session['smUser'])
    else:
        return render(request, 'sm_login.html')
    # user_id = username.id
    profile_id = request.POST.get('profileId')
    user_id = request.POST.get('userid')
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    email = request.POST.get('email')
    password = request.POST.get('password')
    bdate = request.POST.get('bdate')
    gender = request.POST.get('gender')
    city = request.POST.get('city')
    userType = request.POST.get('user_type')
    about = request.POST.get('about')
    updateDate = datetime.now()
    SmUserProfile.objects.filter(user_id= user_id,id = profile_id).update(fname=fname,lname=lname,email=email,gender=gender ,city=city,userType=userType, about=about,updateDate=updateDate)
    SmUser.objects.filter(id= user_id).update(gender=gender)
    return redirect(reverse('irrigreatapp:bloghome'))

def smLogout(request):
    request.session['smUser']= None
    return render(request, 'sm_login.html')

def friendprofile(request ,id):
    sm_userobj = SmUserProfile.objects.get(id = id)
    username = SmUserProfile.objects.get(user_id = sm_userobj.id)
    
    allSmUser = SmUserProfile.objects.all().order_by('?')[:3]
    post = Post.objects.filter(user_id=username.id)
    path = request.path_info
    context = {'username':username,'allSmUser':allSmUser,'post':post,'path':path}
    return render(request, 'othersProfile.html',context)


def follow(request,id):
    follower = SmUser.objects.get(email=request.session['smUser'])
    username = SmUserProfile.objects.get(id=id)

    if username.follow.filter(id=follower.id).exists():
        username.follow.remove(follower.id)
        follow = False
    else:
        username.follow.add(follower.id)
        follow = True
    return redirect(f'/irrigreatapp/friendprofile/{id}')

def createPost(request,id):
    caption = request.POST.get('postcaption')
    user_id = request.POST.get('userid')

    image = request.FILES.get('postimg')
    creatDate = datetime.now()
    updateDate = datetime.now()
    print(caption)
    print(user_id)
    print(image)
    post = Post.objects.create(caption=caption,user_id=user_id,image=image,creatDate=creatDate,updateDate=updateDate)
    # post = Post(caption=caption,user_id=user_id,image=image,creatDate=creatDate,updateDate=updateDate)
    # post.save()
    return redirect(f'/irrigreatapp/')
    # return HttpResponse('Posted')

def likepost(request,id):
    print('**************')
    print(request.path_info)
    print('**************')
    follower = SmUser.objects.get(email=request.session['smUser'])
    path = request.POST.get('path')
    username = Post.objects.get(id=id)

    if username.likes.filter(id=follower.id).exists():
        username.likes.remove(follower.id)
        likes = False
    else:
        username.likes.add(follower.id)
        likes = True
    return HttpResponseRedirect(path)

def deletePost(request,id):
    post = Post.objects.filter(id = id)
    post.delete()
    return redirect(reverse('irrigreatapp:bloghome'))