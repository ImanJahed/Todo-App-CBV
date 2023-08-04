from django.urls import path


from . import views

urlpatterns = [
    path('', views.TodoListApiView.as_view()),
    path('detail/<int:pk>', views.TodoRetrieveUpdateDeleteView.as_view()),
]
