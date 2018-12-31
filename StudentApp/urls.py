"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', TemplateView.as_view(template_name="Welcome.html")),
    path('e_home/',views.home ),
    path('student_login/',views.student_login ),
    path('front_office/',views.front_office ),
    path('front_office_details/',views.front_office_details ),


    path('contact_us/',views.conatct_us ),

    path('student_registration/',views.student_registration ),

    path('student_login_details/',views.student_login_details ),

    path('student_update_profile/',views.student_update_profile ),

    path('student_update_details/',views.student_update_details ),

    path('Student_leave_request/',views.student_leave_request ),

    path('getCampusFromCity/',views.getCampusFromCity ),
    path('getCampusFromCities/',views.getCampusFromCities),
    path('student_leave_request_details/',views.student_leave_request_details ),
    path('student_transfer_request/',views.student_transfer_request),
    path('student_transfer_request_details/',views.student_transfer_request_details),
    path('courses/', views.course),
    path('current_course/', views.current_course),
    path('galery/', views.galery),

    path('home1/', views.home1),

    path('history_leave_request/', views.history_leave_request),
    path('student_leave_request_detail/', views.student_leave_requestdetail),
    path('studentregistration/', views.studentregistration),
    # path('upload_images/', views.upload_images),
    #path('upload_details/', views.upload_datails),
    path('add_Contact/', views.add_Contact),
    path('update_Contact/', views.update_Contact),
    path('add_contact_details/', views.add_contact_details),
    path('update_contact_details/', views.update_contact_details),
    path('new_courses/', views.new_courses),
    # path('fee_report/', views.fee_report),
    # path('payment/', views.payment),
    # path('getAmountFromInstallment/', views.getAmountFromInstallment),
    # path('payment_details/', views.payment_detail),
    # path('previousdetails/', views.previousdetails),
    # path('pending/', views.pending_details),
    #
    path('feedback/', views.feedback),
    path('timetable/', views.timetable),
    path('feedbackdetails/', views.feedbackdetails),
    path('getFeeFromCourse/', views.getFeeFromCourse),










]
