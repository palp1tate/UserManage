from django.shortcuts import render,HttpResponse
def upload_list(request):
    if request.method=="GET":
        return render(request,'upload_list.html')
    file_object=request.FILES.get('avatar')
    with open(file_object.name,mode="wb") as f:
        for chunk in file_object.chunks():
            f.write(chunk)
    return HttpResponse('...')

