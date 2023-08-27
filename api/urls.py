from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentDetails.as_view(),name='student'),
    path('<int:pk>/',views.StudentUpdates.as_view(),name='student')
]