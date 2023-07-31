from django.shortcuts import render,redirect
from web import models
from web.utils.pagination import Pagination
# Create your views here.
# 部门管理
def department_list(request):
    # 部门列表
    # 数据库获取部门信息
    queryset=models.Department.objects.all()
    page_object = Pagination(request, queryset,page_size=10,plus=3)

    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html()  # 生成页码
    }
    return render(request, 'department_list.html', context)


def department_add(request):
    # 添加部门
    if request.method=='GET':
        return render(request,'department_add.html')
    title=request.POST.get('title')
    models.Department.objects.create(title=title)

    # 重定向回部门列表
    return redirect('/department/list')

def department_delete(request):
    # 删除部门
    nid=request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect('/department/list')

def department_edit(request,nid):
    # 修改部门
    if request.method =='GET':
        row_object=models.Department.objects.filter(id=nid).first()
        return render(request,'department_edit.html',{'title':row_object.title})
    title=request.POST.get('title')
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect('/department/list')
