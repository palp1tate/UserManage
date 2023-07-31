"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import depart,user,pretty,admin,account,order,chart,upload
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('department/list/',depart.department_list),
    path('department/add/',depart.department_add),
    path('department/delete/',depart.department_delete),
    path('department/edit/<int:nid>/',depart.department_edit),

    path('user/list/',user.user_list),
    path('user/add/',user.user_add),
    path('user/modelform/add/',user.user_modelform_add),
    path('user/edit/<int:nid>/',user.user_edit),
    path('user/delete/<int:nid>/',user.user_delete),

    path('pretty/list/',pretty.pretty_list),
    path('pretty/add/',pretty.pretty_add),
    path('pretty/edit/<int:nid>/',pretty.pretty_edit),
    path('pretty/delete/<int:nid>/',pretty.pretty_delete),

    # 管理员的管理
    path('admin/list/',admin.admin_list),
    path('admin/add/',admin.admin_add),
    path('admin/edit/<int:nid>',admin.admin_edit),
    path('admin/delete/<int:nid>',admin.admin_delete),
    path('admin/reset/<int:nid>',admin.admin_reset),

    path('login/',account.login),
    path('logout/', account.logout),
    path('image/code/',account.image_code),

    path('order/list/',order.order_list),
    path('order/add/',order.order_add),
    path('order/delete/',order.order_delete),
    path('order/detail/',order.order_detail),
    path('order/edit/',order.order_edit),

    # 数据统计
    path('chart/list/', chart.chart_list),
    path('chart/bar/', chart.chart_bar),
    path('chart/pie/', chart.chart_pie),
    path('chart/line/', chart.chart_line),
    path('chart/highcharts/', chart.highcharts),

    #文件上传
    path('upload/list/',upload.upload_list),

]