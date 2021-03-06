from django.urls import path
from employee import views

urlpatterns=[
    # path('index/',views.IndexView.as_view()),
    # path('signin/',views.LoginView.as_view()),
    # path('signout/',views.LogoutView.as_view()),
    # path('profile/add',views.EmployeeCreaetView.as_view(),name="add-emp")
    path('add',views.EmployeeCreateView.as_view(),name='add-emp'),
    path("all",views.EmployeeListView.as_view(),name="emp-list"),
    path("details/<str:emp_id>",views.EmployeeDetailView.as_view(),name="emp-detail"),
    path("change/<str:emp_id>",views.EmployeeEditView.as_view(),name="emp-edit"),
    path("delete/<str:emp_id>",views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path("",views.index,name="index"),
    path("accounts/signup",views.SignUpView.as_view(),name="sign-up"),
    path("accounts/signin", views.SignInView.as_view(), name="sign-in"),
    path("accounts/signout",views.sign_out,name="sign-out")
]