from django.urls import path
from .views import patient_signup, doctor_signup,patient_dashboard,doctor_dashboard,login_view,logout

app_name = 'authentication'

urlpatterns = [
    path('patient/signup/', patient_signup, name='patient_signup'),
    path('doctor/signup/', doctor_signup, name='doctor_signup'),
    path('patient/dashboard/', patient_dashboard, name='patient_dashboard'),
    path('doctor/dashboard/', doctor_dashboard, name='doctor_dashboard'),
    path('login/', login_view, name='login'),
    path('logout/', logout, name='logout'),

    
]
