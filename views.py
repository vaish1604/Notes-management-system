from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import signup_table
from .models import faculty_signup
import mysql.connector
from operator import itemgetter

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method=="POST":
        data=request.POST.get
        firstname=data('firstname',False)
        lastname=data('lastname',False)
        yearofjoining=data('yearofjoining',False)
        registration=data('registration',False)
        pwd=data('pwd',False)
        #rpwd=data('rpwd',False)
        #if pwd==rpwd:
        ins=signup_table(firstname=firstname,lastname=lastname,yearofjoining=yearofjoining,registration=registration,pwd=pwd)
        ins.save()
        print("data has been saved")
        return render('thankyou')
 
    else:     
        return render(request,'signup.html')

def facultysignup(request):
    if request.method=="POST":
        data=request.POST.get
        firstname=data('firstname',False)
        lastname=data('lastname',False)
        coursecode=data('coursescode',False)
        registration=data('registration',False)
        classnumber=data('classnumber',False)
        pwd=data('pwd',False)
        #rpwd=data('rpwd',False)
        #if pwd==rpwd:
        ins=faculty_signup(firstname=firstname,lastname=lastname,coursecode=coursecode,registration=registration,classnumber=classnumber,pwd=pwd)
        ins.save()
        print("data has been saved")
        return redirect('thankyou')
 
    else:     
        return render(request,'facultysignup.html')


def login(request):
    con1=mysql.connector.connect(host="localhost",user="root",passwd="system",database="notes")
    cursor1=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",passwd="system",database="notes")
    cursor2=con2.cursor()
    sql_reg="select registration from signup_table"
    sql_pwd="select pwd from signup_table"
    cursor1.execute(sql_reg)
    cursor2.execute(sql_pwd)
    r=[]
    p=[]
    for i in cursor1:
        r.append(i)
    for j in cursor2:
        p.append(j)
        
    res1=list(map(itemgetter(0),r))
    res2=list(map(itemgetter(0),p))

    if request.method=="POST":
        data=request.POST.get
        registration=data('registration',False)
        pwd=data('pwd',False)
        i=1
        k=len(res1)
        while i<k:
            if res1[i]==registration and res2[i]==pwd:
                return redirect(request,'thankyou') 
    else:     
        return render(request,'login.html')

def faculty_login(request):
    con1=mysql.connector.connect(host="localhost",user="root",passwd="system",database="notes")
    cursor1=con1.cursor()
    con2=mysql.connector.connect(host="localhost",user="root",passwd="system",database="notes")
    cursor2=con2.cursor()
    sql_reg="select registration from faculty_signup"
    sql_pwd="select pwd from faculty_signup"
    cursor1.execute(sql_reg)
    cursor2.execute(sql_pwd)
    r=[]
    p=[]
    for i in cursor1:
        r.append(i)
    for j in cursor2:
        p.append(j)
        
    res1=list(map(itemgetter(0),r))
    res2=list(map(itemgetter(0),p))

    if request.method=="POST":
        data=request.POST.get
        registration=data('registration',False)
        pwd=data('pwd',False)
        i=1
        k=len(res1)
        while i<k:
            if res1[i]==registration and res2[i]==pwd:
                return redirect(request,'thankyou') 
    else:     
        return render(request,'facultylogin.html')

def thankyou(request):
    # here
    return render(request,'templates/thankyou.html')


