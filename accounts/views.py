from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from tcomments.models import TComment

# Create your views here.
def register(request):
    
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password==password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, '该用户名已被注册')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, '该邮箱已被注册')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,email=email )

                #auth.login(request,user)
                #messages.success(reauest, "you are now logged in")
                #return redirect('index')

                user.save()
                messages.success(request,"注册成功")
                return redirect('login')
        else:
            messages.error(request, "确认密码与密码不匹配")
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"登陆成功")
            return redirect('dashboard')
        else:
            messages.error(request,"用户名或密码错误")
            return redirect('login')
    else:
        
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, '您已退出登录')
        return redirect('login')
    return render(request, 'accounts/register.html')

def dashboard(request):

    
    comments = TComment.objects.order_by('-comment_date').filter(
        user_id=request.user.id
    )
    commentcounts = len(comments)
    context = {
        'comments': comments,
        'commentcounts': commentcounts,
    }


    return render(request, 'accounts/dashboard.html',context)