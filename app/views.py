from django.shortcuts import render
from app.models import *
# Create your views here.
def display_topic_table(request):
    td=Topic.objects.get(topic_name='Foot Ball')
    td1=Topic.objects.get(topic_name='Cricket')
    d={'topics':td,'tdata':td1}
    return render(request,'display_topic_table.html',d)

def display_webpage_table(request):
    wd=Webpage.objects.filter(topic_name='Cricket')
    d={'webpages':wd}
    return render(request,'display_webpage_table.html',d)

def display_access_record(request):
    ad=AccessRecord.objects.filter(author='A')
    d={'accessrecords':ad}
    return render(request,'display_access_record.html',d)