from web import models
from django.core.exceptions import ValidationError
import re
from web.utils.bootstrap import BootStrapModelForm


# modelform演示
class UserModelForm(BootStrapModelForm):
    class Meta:
        model=models.UserInfo
        fields=['name','password','age','account','create_time','gender','depart']

        # 设置样式
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control","placeholder":'姓名'}),
        #     "password": forms.TextInput(attrs={"class": "form-control","placeholder":'密码'}),
        #     "age": forms.TextInput(attrs={"class": "form-control","placeholder":'年龄'}),
        #     "account": forms.TextInput(attrs={"class": "form-control","placeholder":'余额'}),
        #     "create_time": forms.TextInput(attrs={"class": "form-control","placeholder":'入职时间'}),
        #     "gender": forms.Select(attrs={"class": "form-control","placeholder":'性别'}),
        #     "depart": forms.Select(attrs={"class": "form-control","placeholder":'部门'}),
        # }

class PrettyModelForm(BootStrapModelForm):
    # # 验证方式一
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators = [RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误'),],
    #
    # )

    # 验证方式2
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        exists=models.PrettyNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        if len(txt_mobile)!=11 or re.findall(r'^1[3-9]\d{9}$',txt_mobile)==[]:
            # 验证不通过
            raise ValidationError("手机号格式错误")
            # 验证通过,用户输入的值返回
        return txt_mobile
    class Meta:
        model=models.PrettyNum
        # fields='__all__'
        fields=['mobile','price','level','status']
        # exclude=['']
        # widgets={
        # "mobile": forms.TextInput(attrs={"class": "form-control", "placeholder": '手机号'}),
        # "price": forms.TextInput(attrs={"class": "form-control", "placeholder": '价格'}),
        # "level": forms.Select(attrs={"class": "form-control"}),
        # "status": forms.Select(attrs={"class": "form-control"}),
        # }


class PrettyEditModelForm(BootStrapModelForm):
    # mobile=forms.CharField(disabled=True,label='手机号')

    def clean_mobile(self):
        # 排除自己以外，其他的数据是否手机号是否重复？
        # 当前编辑的哪一行的ID
        # print(self.instance.pk)
        txt_mobile = self.cleaned_data["mobile"]
        exists = models.PrettyNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError('手机号已存在')
        if len(txt_mobile)!=11 or re.findall(r'^1[3-9]\d{9}$',txt_mobile)==[]:
            # 验证不通过
            raise ValidationError("手机号格式错误")
            # 验证通过,用户输入的值返回
        return txt_mobile
    class Meta:
        model=models.PrettyNum
        fields=['mobile','price','level','status']
