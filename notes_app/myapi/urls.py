# myjsonapp/urls.py
from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView , TokenRefreshView


urlpatterns = [
    path('notes/', views.get_notes, name='get_notes'),
    path('create/',views.addNote),
    path('note<int:id>/',views.noteDetail),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
