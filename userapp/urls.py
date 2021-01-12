from django.urls import path

from userapp import views

urlpatterns = [
    path('student/', views.StudentGenerAPIView.as_view()),
    path('student/<str:id>', views.StudentGenerAPIView.as_view()),
    path('login/', views.StudentViewSet.as_view({"post":"stu_login"})),
]