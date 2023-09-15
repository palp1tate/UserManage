# UserManage——用户管理系统

本用户管理系统来源于武沛齐老师的b站网课：<https://www.bilibili.com/video/BV1NL41157ph?p=1&vd_source=84fc27804252448ba51ef3b6abfd5d36>

视频里的学习文档和源码均已提交到Github上。

## 克隆使用：
```bash
git clone https://github.com/palp1tate/UserManage.git
```

## 下载依赖

`pip`下载完需要的依赖包，比如`django`等。

## 配置数据库

打开`settings.py`，配置关于MySQL的部分：
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourdatabasename',  # 数据库名字
        'USER': 'yourusername',
        'PASSWORD': 'yourpwd',
        'HOST': '127.0.0.1',  # 那台机器安装了MySQL
        'PORT': 3306,
    }
}
```
创建你在上述配置命名的数据库，然后在项目根目录运行命令以完成数据库迁移：

```bash
python manage.py makemigrations
python manage.py migrate
```

然后在`web_admin`这张表插入一条数据：
> id：1
> 
> username：admin
> 
> password：44243401cf81aa8ba0798b1d181de015

这样做的目的是方便管理员登录，以上密码是经过MD5加密后的数据，真实密码为`123`，登入系统后可在web界面修改密码。

## 运行项目：

```python
python manage.py runserver
```

然后访问：<http://127.0.0.1:8000/>，自动跳入登录界面。分别输入`admin`和`123`，验证码根据实际情况填写。

![image](https://github.com/palp1tate/UserManage/assets/120303802/7458af6e-e0e4-410a-a904-d893b9eda5f9)

![image](https://github.com/palp1tate/UserManage/assets/120303802/361e5e96-942b-4e9a-b56b-2810a13e5fd9)

![image](https://github.com/palp1tate/UserManage/assets/120303802/99ac77ef-ace1-4d08-b1d6-c492d7767108)

![image](https://github.com/palp1tate/UserManage/assets/120303802/88834b2b-e286-4121-8cb9-810c1a15926d)









