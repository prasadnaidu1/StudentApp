from django.db import models
class Student_Registration(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    father_name=models.CharField(max_length=50)
    mother_name=models.CharField(max_length=50)
    contact_no=models.IntegerField(default=10)
    email=models.EmailField(primary_key=True)
    date_of_birth=models.DateField()
    gender=models.CharField(max_length=20)
    material_status=models.CharField(max_length=15)
    course=models.CharField(max_length=15)
    fee_of_course=models.IntegerField()
    username=models.CharField(max_length=12)
    password=models.CharField(max_length=12)
    r_number=models.CharField(max_length=12)
    def __str__(self):
        return self.first_name
class city(models.Model):
    city_id=models.IntegerField(primary_key=True)
    cityname=models.CharField(max_length=20)

    def __str__(self):
        return self.cityname
class campuses(models.Model):
    campus_id=models.IntegerField(primary_key=True)
    cityname=models.ForeignKey(city,on_delete=models.CASCADE)
    campusname=models.CharField(max_length=20)

    def __str__(self):
        return self.campusname

class student_leave(models.Model):
    r_number = models.CharField(max_length=12,primary_key=True)
    cities=models.CharField(max_length=20)
    campus=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    from_date=models.DateField()
    to_date=models.DateField()

    def __str__(self):
        return self.name
class transfer_request(models.Model):
    city=models.CharField(max_length=20)
    campus=models.CharField(max_length=20)
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=30)

class front_office_module(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    contact_no=models.IntegerField(primary_key=True)
    email=models.EmailField()
    address=models.CharField(max_length=50)
    joining_date =models.DateField()
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    def __str__(self):
        return self.name
class faculity_registration(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField(primary_key=True)
    subject=models.CharField(max_length=50)
    exp=models.IntegerField()
    def __str__(self):
        return self.subject
class add_classes(models.Model):
    id=models.IntegerField(default=10,primary_key=True)
    class_name=models.CharField(max_length=30)


    def __str__(self):
        return self.class_name
class add_daily_timetable(models.Model):
    Class=models.ForeignKey(add_classes,on_delete=models.CASCADE)
    subject=models.ForeignKey(faculity_registration,on_delete=models.CASCADE)
    class_starting_time=models.TimeField()
    class_ending_time=models.TimeField()
    total_duration=models.IntegerField()
# class file_upload(models.Model):
#     file=models.ImageField()
#     des=models.CharField(max_length=100)
class add_contact(models.Model):
    address=models.CharField(max_length=150)
    email=models.EmailField(primary_key=True)
    contact=models.IntegerField()

class fee_details(models.Model):
    class_name=models.ForeignKey(add_classes,on_delete=models.CASCADE)
    fee=models.CharField(max_length=20)


class installment_name(models.Model):
    installment_id=models.IntegerField(primary_key=True)
    coursename=models.ForeignKey(add_classes,on_delete=models.CASCADE)
    installment_Name=models.CharField(max_length=50)
    def __str__(self):
        return self.installment_Name

class installment_payment(models.Model):
    installment_id=models.IntegerField(primary_key=True)
    installment_name=models.ForeignKey(installment_name,on_delete=models.CASCADE)
    installment_amount=models.IntegerField()
class payment_details(models.Model):
    DateandTIme=models.CharField(max_length=30)
    coursename=models.CharField(max_length=50)
    Installment_name=models.CharField(max_length=50,primary_key=True)
    amount=models.IntegerField()
    holdername = models.CharField(max_length=50)
    card_number=models.IntegerField()
    card_cvv=models.IntegerField()
class feedBackDetails(models.Model):
    f_name=models.CharField(max_length=50)
    message=models.CharField(max_length=500)























