from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
def display_topic_table(request):
    td=Topic.objects.all()
    td=Topic.objects.exclude(topic_name='Foot Ball')
    td=Topic.objects.all()[::-1]
    d={'topics':td}
    return render(request,'display_topic_table.html',d)

def display_webpage_table(request):
    wd=Webpage.objects.all()
    wd=Webpage.objects.exclude(topic_name='Cricket')
    wd=Webpage.objects.all()[::-1]
    wd=Webpage.objects.all().order_by(Length('topic_name').desc())
    wd=Webpage.objects.filter(name__startswith='V')
    wd=Webpage.objects.filter(url__endswith='org')
    #wd=Webpage.objects.filter(name__contains='a')
    
    d={'webpages':wd}
    return render(request,'display_webpage_table.html',d)

def display_access_record(request):
    ad=AccessRecord.objects.all()
    #ad=AccessRecord.objects.exclude(author='A')
    ad=AccessRecord.objects.all().order_by('-author')
    d={'accessrecords':ad}
    return render(request,'display_access_record.html',d)