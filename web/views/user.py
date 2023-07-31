from django.shortcuts import render,redirect
from web import models
from web.utils.pagination import Pagination
from web.utils.form import UserModelForm
# Create your views here.
# 用户管理
def user_list(request):
    queryset=models.UserInfo.objects.all()
    page_object=Pagination(request,queryset)
    """
        # 用Python的语法获取数据
        for obj in queryset:
            print(obj.id, obj.name, obj.account, obj.create_time.strftime("%Y-%m-%d"), obj.gender, obj.get_gender_display(), obj.depart_id, obj.depart.title)
            # print(obj.name, obj.depart_id)
            # obj.depart_id  # 获取数据库中存储的那个字段值
            # obj.depart.title  # 根据id自动去关联的表中获取哪一行数据depart对象。
        """
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'user_list.html', context)

def user_add(request):
    if request.method =='GET':
    # 添加用户
        context={"gender_choices":models.UserInfo.gender_choices,
                "depart_list":models.Department.objects.all()}
        return render(request,'user_add.html',context)
    name=request.POST.get('name')
    pwd=request.POST.get('pwd')
    age=request.POST.get('age')
    ac=request.POST.get('ac')
    ctime=request.POST.get('ctime')
    gender_id=request.POST.get('gd')
    dp_id=request.POST.get('dp')
    models.UserInfo.objects.create(name=name,password=pwd,age=age,account=ac,create_time=ctime,gender=gender_id,depart_id=dp_id)
    return redirect('/user/list')


def user_modelform_add(request):
    if request.method == 'GET':
        form=UserModelForm()
        return render(request,'user_modelform_add.html',{'form':form})
    form=UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user/list')
    else:
        return render(request,'user_modelform_add.html',{'form':form})

def user_edit(request,nid):
    # 编辑用户
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        #根据ID去数据库获取要编辑的那一行数据
        form=UserModelForm(instance=row_object)
        return render(request,'user_edit.html',{'form':form})
    form=UserModelForm(data=request.POST,instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要用户再输入以外增加一点值
        # form.instance.字段名=值
        form.save()
        return redirect('/user/list')
    else:
        return render(request,'user_edit.html',{'form':form})

def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user/list')

