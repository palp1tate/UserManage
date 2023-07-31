from django.shortcuts import render,redirect
from web import models
from web.utils.pagination import Pagination
from web.utils.form import PrettyModelForm,PrettyEditModelForm
# Create your views here.
def pretty_list(request):
    #靓号列表
    data_dict={}
    search_data=request.GET.get('q','')
    if search_data:
        data_dict["mobile__contains"]=search_data
    queryset=models.PrettyNum.objects.filter(**data_dict).order_by('-level')
    page_object=Pagination(request,queryset,page_size=20,plus=3)
    context = {
        "queryset": page_object.page_queryset,  # 分完页的数据
        "page_string": page_object.html(),  # 生成页码
        "search_data":request.GET.get('q', ''),
    }
    return render(request, 'pretty_list.html', context)



def pretty_add(request):
    if request.method == 'GET':
        form=PrettyModelForm()
        return render(request,'pretty_add.html',{'form':form})
    form=PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/pretty/list')
    else:
        return render(request,'pretty_add.html',{'form':form})


def pretty_edit(request,nid):
    # 编辑用户
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == 'GET':
        # 根据ID去数据库获取要编辑的那一行数据
        form = PrettyEditModelForm(instance=row_object)
        return render(request, 'pretty_edit.html', {'form': form})
    form = PrettyEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        # 默认保存的是用户输入的所有数据，如果想要用户再输入以外增加一点值
        # form.instance.字段名=值
        form.save()
        return redirect('/pretty/list')
    else:
        return render(request, 'pretty_edit.html', {'form': form})
def pretty_delete(request,nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect('/pretty/list')


