from django.http import HttpResponse
from django.shortcuts import render
import datetime




from .models import Student_Registration,city,campuses,student_leave,\
    transfer_request,front_office_module,add_contact,add_classes,fee_details,installment_name,\
    installment_payment,payment_details,add_daily_timetable,feedBackDetails
import random

# Create your views here.
def home(request):
    type="e_home"
    return render(request,"Welcome.html",{"type":type})


def student_login(request):
    s_details=request.GET.get("type")
    return render(request,"Welcome.html",{"type":s_details})


def front_office(request):
    f_details = request.GET.get("type")
    return render(request, "Welcome.html", {"type": f_details})


def front_office_details(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    res=front_office_module.objects.filter(username=username,password=password)
    if not res:
        type="front_office"
        return  render(request,"Welcome.html",{"type":type,"msg":"InvalidUser"})
    else:
        type="frontoffice_home"
        name=""
        for x in res:
            name=x.name


        return render(request,"Welcome.html",{"type":type,"name":name})


def student_registration(request):
    r_number=request.POST.get("r_number")
    f_name=request.POST.get("f_name")
    l_name=request.POST.get("l_name")
    father_name=request.POST.get("fa_name")
    mother_name=request.POST.get("mo_name")
    contact_no=request.POST.get("contactnumber")
    date_of_birth=request.POST.get("dob")
    email=request.POST.get("email")
    gender=request.POST.get("gender")
    material_status=request.POST.get("material")
    cou_res=request.POST.get("course")
    fee=request.POST.get("fee")
    username=request.POST.get("username")
    password=request.POST.get("password")
    result=Student_Registration(first_name=f_name,last_name=l_name,contact_no=contact_no,
                         father_name=father_name,mother_name=mother_name,email=email,
                         course=cou_res,gender=gender,material_status=material_status,
                        username=username,password=password,date_of_birth=date_of_birth,r_number=r_number,fee_of_course=fee)
    result.save()

    return render(request,"Welcome.html",{"type":"studentregistration","message":"Successfully Registred Your Application","res":"home1"})


def student_login_details(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    res=Student_Registration.objects.filter(username=username,password=password)

    if not res:
        type="studentlogin"
        return render(request,"Welcome.html",{"type":type,"msg":"Invalid User"})
    else:
        type="Student_home"
        name=""
        email= ""

        for x in res:
            name=x.first_name
            email=x.email

            return render(request,"Student _Home.html",{"type":type,"name":name,"email1": email})


def student_update_profile(request):
    type=request.GET.get("type")

    email=request.GET.get("email")

    result=Student_Registration.objects.filter(email=email)

    name = ""
    for x in result:
        name = x.first_name
    return render(request,"Student _Home.html",{"type":type,"result":result,"name":name})


def student_update_details(request):
    name=request.POST.get("t1")
    last_name=request.POST.get("t2")
    father_name=request.POST.get("t3")
    mothername=request.POST.get("t4")
    contact_no=request.POST.get("t5")
    email=request.POST.get("t6")
    dob=request.POST.get("t7")
    gender=request.POST.get("t8")
    m_status=request.POST.get("t9")
    username=request.POST.get("t10")
    password=request.POST.get("t11")
    Student_Registration.objects.filter(email=email).update(contact_no=contact_no,material_status=m_status,username=username,password=password)

    return render(request,"Student _Home.html",{"message1":"Updated Details Successfully","name":name})


def student_leave_request(request):
    s_details = request.GET.get("type")
    email = request.GET.get("email")

    res=city.objects.values("cityname")
    r_number=["Choose RollNUmber"]
    result=Student_Registration.objects.values("r_number")
    for y in result:
        r_number.append(y["r_number"])
    cities=["CityName"]
    for x in res:
        cities.append(x["cityname"])
    final = Student_Registration.objects.filter(email=email)

    name = ""
    for x in final:
        name = x.first_name
        print(name)

    return render(request, "Student _Home.html", {"type": s_details,"city":cities,
                                                  "email3":email,"r_number":r_number,"name":name})


def getCampusFromCity(request):
    sel_city=request.GET.get("city")
    res=city.objects.values("city_id").filter(cityname=sel_city)
    city_id=0
    for x in res:
        city_id = x["city_id"]
    res1 =campuses.objects.values('campusname').filter(cityname=city_id)
    campus=["Campuses"]


    if not res1:
        campus=["NoCampuses are Available"]
    else:
        for x in res1:
            campus.append(x["campusname"])
    r_number = ["Choose RollNUmber"]
    result = Student_Registration.objects.values("r_number")
    for y in result:
        r_number.append(y["r_number"])

    return render(request,"Student _Home.html",{"campus":campus,"city":sel_city,"type":"Student_leave_Request","key":"one","r_number":r_number})


def student_leave_request_details(request):
    r_number=request.POST.get("c6")
    cities=request.POST.get("c1")
    campus=request.POST.get("c2")
    name=request.POST.get("c3")
    f_date=request.POST.get("c4")
    t_date=request.POST.get("c5")

    res=student_leave(cities=cities,campus=campus,name=name,from_date=f_date,to_date=t_date,r_number=r_number)
    res.save()
    return render(request,"Student _Home.html",{"message":"Successfully Sended Your Request"})


def student_transfer_request(request):
    transfer=request.GET.get("type")
    email = request.GET.get("email")

    res=city.objects.values("cityname")
    cities=["City"]
    for x in res:
        cities.append(x["cityname"])
    final = Student_Registration.objects.filter(email=email)

    name = ""
    for x in final:
        name = x.first_name

    return render(request,"Student _Home.html",{"type":transfer,"city":cities,"name":name,"email":email})

def getCampusFromCities(request):
    sel_city=request.GET.get("city")


    res=city.objects.values("city_id").filter(cityname=sel_city)
    city_id=0
    for x in res:
        city_id = x["city_id"]
    res1 =campuses.objects.values('campusname').filter(cityname=city_id)
    campus=["Campuses"]


    if not res1:
        campus=["NoCampuses are Available"]
    else:
        for x in res1:
            campus.append(x["campusname"])

    return render(request,"Student _Home.html",{"campus":campus,"city":sel_city,
                                                "type":"student_transfer_request","key":"two"})

def student_transfer_request_details(request):
    city=request.POST.get("c1")
    campus=request.POST.get("c2")
    name=request.POST.get("c3")
    subject=request.POST.get("c4")
    transfer_request(city=city,campus=campus,name=name,subject=subject).save()
    return render(request,"Student _Home.html",{"message2":"Successfully sended"})


def conatct_us(request):
    contact=request.GET.get("type")
    res=add_contact.objects.all()
    return render(request,"Welcome.html",{"type":contact,"res":res})


def course(request):
    courses=request.GET.get("type")
    email=request.GET.get("email")


    res = Student_Registration.objects.filter(email=email)
    name = ""

    for x in res:
        name = x.first_name
    return render(request,"Student _Home.html",{"type":courses,"name":name,"email2":email})

def current_course(request):
    currentcourse = request.GET.get("type")
    mail=request.GET.get("email")
    res1 = Student_Registration.objects.filter(email=mail)
    name = ""
    for x in res1:
        name = x.first_name

    return render(request, "Student _Home.html", {"type": currentcourse,"res1":res1,"name":name})


def galery(request):
    image= request.GET.get("type")
    return render(request, "Student _Home.html", {"type": image})


def home1(request):
    res=request.GET.get("type")
    Email=request.GET.get("email")

    final=Student_Registration.objects.filter(email=Email)

    name = ""
    for x in final:
        name = x.first_name
    print(name)
    return  render(request,"Student _Home.html",{"type":res,"final":final,"name":name})


def history_leave_request(request):
    leave_history=request.GET.get("type")
    email=request.GET.get("email")
    res=student_leave.objects.filter()
    result = Student_Registration.objects.filter()
    name = ""
    for x in result:
        name = x.first_name
    return render(request,"Student _Home.html",{"type":leave_history,"res":res,"name":name})
    #if res:
        #result=student_leave.objects.filter()
        #return render(request,"Student _Home.html",{"type1":leave_history,"result":result})
    #else:
      #  return render(request,"Student _Home.html",{"type":leave_history,"message":"NO history"})


def student_leave_requestdetail(request):
    leave_details = request.GET.get("type")

    email = request.GET.get("email")
    roll_number = ""
    Roll_number = student_leave.objects.filter()
    for x in Roll_number:
        roll_number = x.r_number
    result = Student_Registration.objects.filter(email=email)
    name = ""
    for x in result:
        name = x.first_name

    return render(request,"Student _Home.html",{"type":leave_details,"EMAIL":email,"roll_number":roll_number,"type1":"student_leave_request","name":name})


def studentregistration(request):
    s_reg=request.GET.get("type")
    for x in range(1):
        res2 = random.randint(1, 100)
        id = "HR/PB" + str(res2)
    result = front_office_module.objects.filter()
    Name = ""
    for x in result:
        Name = x.name
    Course = ["Course"]
    re = add_classes.objects.values("class_name")
    for x in re:
        Course.append(x["class_name"])

    return render(request,"Welcome.html",{"type":s_reg,"id":id,"name":Name,"course":Course})


# def upload_images(request):
#     upload=request.GET.get("type")
#     if request.method == "POST":
#         file = file_info(request.POST, request.FILES)
#         if file.is_valid():
#             handle_uploaded_file(request.FILES['file'])
#             return HttpResponse("File updated successfully")
#     else:
#         file = file_info()
#         return render(request, "Welcome.html", {"form": file,"type":upload})


# def upload_datails(request):
#      file=request.POST.get("t1")
#      des=request.POST.get("t2")
#      file_upload(file=file,des=des).save()
#      return render(request,"Student _Home.html")


def add_Contact(request):
    contact = request.GET.get("type")


    return render(request,"Welcome.html",{"contact":contact})


def add_contact_details(request):
    add=request.POST.get("t1")
    email=request.POST.get("t2")
    contact=request.POST.get("t3")
    add_contact(address=add,email=email,contact=contact).save()
    return render(request,"Welcome.html")


def update_Contact(request):
    update = request.GET.get("type")
    res=add_contact.objects.filter()


    return render(request, "Welcome.html", {"update": update,"res":res})


def update_contact_details(request):
    add = request.POST.get("t1")
    email = request.POST.get("t2")
    contact = request.POST.get("t3")
    add_contact.objects.filter(email=email).update(address=add,contact=contact)
    return render(request,"Welcome.html",{"msg":"updated successfully"})


def new_courses(request):
    newCourse = request.GET.get("type")
    result=add_classes.objects.all()

    return render(request,"Student _Home.html",{"type":newCourse,"result1":result})


# def fee_report(request):
#     fee = request.GET.get("type")
#     email = request.GET.get("email")
#
#     return render(request,"Student _Home.html",{"fee":fee,"email":email})


# def payment(request):
#     type=request.GET.get("type")
#     email=request.GET.get("email")
#
#     Installment=[]
#     res1=installment_name.objects.values("installment_Name")
#     for x in res1:
#         Installment.append(x["installment_Name"])
#
#     res = Student_Registration.objects.filter(email=email)
#     course = ""
#     for x in res:
#         course = x.course
#
#     today = datetime.datetime.today()
#
#
#
#     return render(request,"Student _Home.html",{"type":type,"date":today,"installment":Installment,"course":course})
#
#
# def getAmountFromInstallment(request):
#     installment=request.GET.get("installment")
#
#     res=installment_name.objects.values("installment_id").filter(installment_Name=installment)
#     res1 = Student_Registration.objects.filter()
#     course = ""
#     for x in res1:
#         course = x.course
#
#     date = datetime.datetime.now()
#
#     installment_id=0
#     for x in res:
#         installment_id=x["installment_id"]
#
#
#     res2=installment_payment.objects.values("installment_amount").filter(installment_name=installment_id)
#
#     installments = []
#     if not res2:
#         installments=["Not Available"]
#     else:
#         for x in res2:
#             installments.append(x["installment_amount"])
#             print(installments)
#     # res = Student_Registration.objects.filter()
#     # fees = ""
#     # for x in res:
#     #     fees = x.fee_of_course
#
#
#     return render(request, "Student _Home.html", {"installments": installments, "installment_name": installment_name,
#                                                   "type": "payment", "key": "one" ,"course":course,"date":date})
#
#
# def payment_detail(request):
#     date=request.POST.get("p1")
#     Course=request.POST.get("p2")
#     install=request.POST.get("p3")
#     amount=request.POST.get("p4")
#     cardholdername=request.POST.get("p5")
#     cardnumber=request.POST.get("p6")
#     cvv=request.POST.get("p7")
#     payment_details(DateandTIme=date,coursename=Course,Installment_name=install,
#                     amount=amount,card_number=cardnumber,card_cvv=cvv,holdername=cardholdername).save()
#
#
#     return render(request,"Student _Home.html",{"message":"Successfully paid ","amount":amount,"type":"payment"})
#
#
# def previousdetails(request):
#     type= request.GET.get("type")
#     email=request.GET.get("email")
#
#     return render(request,"Student _Home.html",{"type":type})
#
#
# def pending_details(request):
#     type = request.GET.get("type")
#     email = request.GET.get("email")
#
#     return render(request, "Student _Home.html", {"type": type})





def feedback(request):
    type = request.GET.get("type")
    email = request.GET.get("email")

    return render(request, "Student _Home.html", {"type": type})


def timetable(request):
    type = request.GET.get("type")
    res=add_daily_timetable.objects.all()
    print(res)


    return render(request, "Student _Home.html", {"type": type,"res":res})


def feedbackdetails(request):
    f_name=request.POST.get("firstname")
    #l_name=request.POST.get("lastname")
    subject=request.POST.get("subject")
    feedBackDetails(f_name=f_name,message=subject).save()

    return render(request,"Student _Home.html",{"type":"feedback","message":"Successfully Given your Feedback"})
def getFeeFromCourse(request):
    course=request.GET.get("course")
    print(course)
    res=add_classes.objects.values("id").filter(class_name=course)
    course_id = 0
    for x in res:
        course_id = x["id"]
    res1 = fee_details.objects.values('fee').filter(class_name=course_id)
    Fees = ["Fee's"]

    if not res1:
        Fees = ["No Fee's Available"]
    else:
        for x in res1:
            Fees.append(x["fee"])
    for x in range(1):
         res2 = random.randint(1, 100)
         id = "HR/PB" + str(res2)

    return render(request,"Welcome.html",{"course":course,"fee":Fees,"type":"studentregistration","key":"one","id":id})









