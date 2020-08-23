from django.shortcuts import render
from django.http import HttpResponse
import os
# Create your views here.
import csv
def home(request):
    return render(request,'index.html')

def add(request):
    return render(request,'student.html')

def search(request):
    return render(request,'search.html')

def record(request):
    id=request.POST['id']
    name=request.POST['studentname']
    gender=request.POST['gender']
    dob=request.POST['dob']
    city=request.POST['city']
    state=request.POST['state']
    mail=request.POST['mail']
    qualification=request.POST['qualification']
    stream=request.POST['stream']
    details = [id,name,gender,dob,city,state,mail,qualification,stream]
    with open('details.csv','a',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(details)

    return render(request,'done.html')

def find(request):
    id=request.POST['id']
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(path, 'details.csv')
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if id==row[0]:
                StudentId=row[0]
                StudentName=row[1]
                Gender=row[2]
                DateOfBirth=row[3]
                City=row[4]
                State=row[5]
                EmailId=row[6]
                Qualification=row[7]
                Stream=row[8]
                return render(request,'result.html', {'id' : StudentId,'name' : StudentName,'gen' : Gender,
                            'dob' : DateOfBirth,'cit' : City ,'sta' : State,'mai' : EmailId,'qua' : Qualification, 'stream' : Stream} )

def display(request):
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file = os.path.join(path, 'details.csv')
    rows=[]
    with open(file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            StudentId=row[0]
            StudentName=row[1]
            Gender=row[2]
            DateOfBirth=row[3]
            City=row[4]
            State=row[5]
            EmailId=row[6]
            Qualification=row[7]
            Stream=row[8]
            rowdict = {'id' : StudentId,'name' : StudentName,'gen' : Gender,
                        'dob' : DateOfBirth,'cit' : City ,'sta' : State,'mai' : EmailId,'qua' : Qualification, 'stream' : Stream}
            rows.append(rowdict)
    for row in rows:
        print(row['id'])
    return render(request,'display.html',{'rows' : rows} )
