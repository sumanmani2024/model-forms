from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *

def insert_topic(request):
    TF=TopicForm()
    d={'form':TF}
    if request.method=='POST':
        data=TopicForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('inserted in topics succesfully')
    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    Wp=WebpageForm()
    d1={'form':Wp}
    if request.method=='POST':
        data=WebpageForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('inserted in webpages seccesfully')
    return render(request,'insert_webpage.html',d1)


def insert_AccessRecords(request):
    AC=AccessRecordsForm()
    d2={'form':AC}
    if request.method=='POST':
        data=AccessRecordsForm(request.POST)
        if data.is_valid():
            data.save()
            return HttpResponse('inserted in AccessRecords seccesfully')
    return render(request,'AccessRecordsForm.html',d2)

