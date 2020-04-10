from django.urls import path,include
from . import views


app_name='db_xyw'
urlpatterns=[
path('detail/',views.detail,name='detail'),
path('adminisdetail/',views.adminisdetail,name='adminisdetail'),
path('adminisdetail_2/',views.adminisdetail_2,name='adminisdetail_2'),
path('adminisdetail_3/',views.adminisdetail_3,name='adminisdetail_3'),
path('advanceddetail/',views.advanceddetail,name='advanceddetail'),
path('addPerson/',views.addPerson,name='addPerson'),
path('delPerson/<int:person_id>', views.deletePerson, name='delPerson'),
path('del_AdvancedPerson/<int:person_id>', views.delete_AdvancedPerson, name='del_AdvancedPerson'),
path('delTemp/<int:person_id>', views.deleteTemp, name='delTemp'),
path('delTemp2/<int:person_id>', views.deleteTemp2, name='delTemp2'),
path('detail/line.html',views.line,name='line'),
path('addEnvironment/',views.addEnvironment,name='addEnvironment'),
path('delEnvironment/<int:environment_id>', views.deleteEnvironment,name='delEnvironment'),
path('login/',views.login,name='login'),
path('register/',views.register,name='register'),
path('logout/',views.logout,name='logout'),
path('adminislogin/',views.adminislogin,name='adminislogin'),
path('adminisregister/',views.adminisregister,name='adminisregister'),
path('advancedlogin/',views.advancedlogin,name='advancedlogin'),
path('advancedregister/',views.advancedregister,name='advancedregister'),
path('account/',views.account,name='account'),
path('account_edit/',views.account_edit,name='account_edit'),
path('pwd_edit/',views.pwd_edit,name='pwd_edit'),
path('authorize/',views.authorize,name='authorize'),
path('authoriz_2/',views.authorize_2,name='authorize_2'),
path('delAuthorize/<int:person_id>', views.deleteAuthorize,name='delAuthorize'),
path('watchPerson/<int:person_id>', views.watchPerson, name='watchPerson'),
]

#delPerson/<int:person_id>
#path('detail/line.html/<name>',views.line,name='line'),