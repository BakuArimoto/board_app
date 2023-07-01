from django.urls import path
from .views import signupfunc, loginfunc, listfunc, logoutfunc

urlpatterns = [
    path('signup/', signupfunc, name='signup'),
    path('login/', loginfunc, name='login'),
    path('list/', listfunc, name='list'),
    path('logou/t', logoutfunc, name='logout')
]
