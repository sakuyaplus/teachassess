from tcomments.models import TComment
from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.
def tcomment(request):

    
    if request.method == 'POST':
        user_id=request.POST['user_id']
        user_name=request.POST['user_name']
        teacher_id=request.POST['teacher_id']
        teacher_name=request.POST['teacher_name']
        try:
            stars=request.POST['rating']
        except:
            messages.error(request,'评价星级范围为1-5')
            return redirect('/teachers/'+teacher_id)

        message=request.POST['message']
        if int(stars)<1 or int(stars)>5:
            messages.error(request,'评价星级范围为1-5')
            return redirect('/teachers/'+teacher_id)
      
        has_commented = TComment.objects.all().filter(teacher_id=teacher_id,user_id=user_id)
        if has_commented: #如果评价过，可以修改
            for i in has_commented:
                i.stars=stars
                i.message=message
                i.save()
            messages.success(request,'评价修改成功')
            return redirect('/teachers/'+teacher_id)
       

        comment = TComment(user_id=user_id,user_name=user_name,teacher_id=teacher_id,
        stars=stars,message=message,teacher_name=teacher_name)

        comment.save()
        messages.success(request,'评价成功')

     
        return redirect('/teachers/'+teacher_id)
    return redirect('index')