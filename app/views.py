from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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
    wd=Webpage.objects.filter(name__contains='a')
    wd=Webpage.objects.all()
    wd=Webpage.objects.filter(Q(name='santosh') | Q(url__endswith='in'))
    wd=Webpage.objects.filter(Q(topic_name='Hockey') & Q(url__startswith='https'))
    wd=Webpage.objects.filter(name__in=['santosh','Dhoni'])
    wd=Webpage.objects.all()
    

    


    
    
    d={'wd':wd}
    return render(request,'display_webpage_table.html',d)

def display_access_record(request):
    ad=AccessRecord.objects.all()
    ad=AccessRecord.objects.exclude(author='A')
    ad=AccessRecord.objects.all().order_by('-author')
    ad=AccessRecord.objects.all()
    ad=AccessRecord.objects.filter(date__gt='1998-05-28')
    ad=AccessRecord.objects.filter(date__lt='1998-05-28')
    ad=AccessRecord.objects.filter(date__gte='1998-05-28')
    ad=AccessRecord.objects.filter(date__lte='2023-05-18')
    ad=AccessRecord.objects.filter(date__year='2022')
    ad=AccessRecord.objects.filter(date__month='10')
    ad=AccessRecord.objects.filter(date__day='28')
    ad=AccessRecord.objects.filter(date__year__gt='2021')
    ad=AccessRecord.objects.filter(date__month__lt='05')



    d={'accessrecords':ad}
    return render(request,'display_access_record.html',d)


def update_webpages(request):
    
    #Webpage.objects.filter(name='Abc').update(url='http://abcd.in')
    #Webpage.objects.filter(topic_name='Cricket').update(url='http://IndianCricket.com')
    #Webpage.objects.filter(name='sony').update(topic_name='Cricket')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='Hockey')
    #Webpage.objects.filter(name='Dhoni').update(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='Pqr',defaults={'url':'http://Foot Ball.in'})
    #Webpage.objects.update_or_create(topic_name='Cricket',defaults={'url':'http://India.in'})
    CTO=Topic.objects.get(topic_name='Cricket')
    #Webpage.objects.update_or_create(name='Dhoni',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(name='Rahul',defaults={'topic_name':CTO})
    #Webpage.objects.update_or_create(name='Pandya',defaults={'url':'https://Pandya.com'})
    Webpage.objects.update_or_create(name='Nipun',defaults={'topic_name':CTO})





    
    wd=Webpage.objects.all()
    d={'wd':wd}
    return render(request,'display_webpage_table.html',d)


def delete_webpages(request):
    
    #Webpage.objects.filter(name='Nipun').delete()
    Webpage.objects.filter(name='Rahul').delete()

    wd=Webpage.objects.all()
    d={'wd':wd}
    return render(request,'display_webpage_table.html',d)