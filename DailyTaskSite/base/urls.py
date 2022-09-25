from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, CustomLogin, Register


urlpatterns = [
    path('login/', CustomLogin.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"), #redirect to login page
    path('register/', Register.as_view(), name="register"),
    path('', TaskList.as_view(), name="tasks"),
    path('task/<int:pk>/', TaskDetail.as_view(), name="details"),
    path('create-task/', TaskCreate.as_view(), name="task-create"),
    path('update-task/<int:pk>/', TaskUpdate.as_view(), name="task-update"),
    path('del-task/<int:pk>/', TaskDelete.as_view(), name="task-del"),
]