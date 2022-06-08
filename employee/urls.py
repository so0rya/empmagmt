from django.urls import path
from employee import views

urlpatterns=[
    path('index/',views.IndexView.as_view()),
    path('signin/',views.LoginView.as_view()),
    path('signout/',views.LogoutView.as_view()),
    path('profile/add',views.EmployeeCreaetView.as_view(),name="add-emp")
]