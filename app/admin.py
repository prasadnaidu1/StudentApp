from django.contrib import admin

from.models import city,campuses,student_leave,front_office_module,\
    faculity_registration,add_daily_timetable,add_classes,fee_details,installment_name,installment_payment
admin.site.register(city)
admin.site.register(campuses)
admin.site.register(student_leave)
admin.site.register(front_office_module)
admin.site.register(faculity_registration)
admin.site.register(add_daily_timetable)
admin.site.register(add_classes)
admin.site.register(fee_details)
admin.site.register(installment_name)
admin.site.register(installment_payment)

