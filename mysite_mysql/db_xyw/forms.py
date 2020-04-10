from django import forms

class UserForm(forms.Form):
    UserName = forms.CharField(label="用户名", max_length=128)
    keyNumber = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    UserName = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    keyNumber1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    keyNumber2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    sex = forms.ChoiceField(label="性别", choices=gender)
    NickName=forms.CharField(label="昵称",max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    age=forms.IntegerField(label="年龄",widget=forms.TextInput(attrs={'class': 'form-control'}) )
    height=forms.IntegerField(label="身高(cm)",widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight=forms.IntegerField(label="体重(kg)",widget=forms.TextInput(attrs={'class': 'form-control'}))


class AdminisForm(forms.Form):
    UserName = forms.CharField(label="用户名", max_length=128)
    keyNumber = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

class AdminisRegisterForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    UserName = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    keyNumber1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    keyNumber2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    NickName=forms.CharField(label="昵称",max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))

class AdvancedForm(forms.Form):
    UserName = forms.CharField(label="用户名", max_length=128)
    keyNumber = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput)

class AdvancedRegisterForm(forms.Form):
    gender = (
        ('男', "男"),
        ('女', "女"),
    )
    UserName = forms.CharField(label="用户名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    keyNumber1 = forms.CharField(label="密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    keyNumber2 = forms.CharField(label="确认密码", max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    NickName=forms.CharField(label="昵称",max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
