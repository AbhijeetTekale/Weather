from django.shortcuts import render
from DataEntry.models import Test
from django.http import HttpResponse
from django.utils.dateformat import datetime
import subprocess
para1_min=10
para1_max=100
para2_min=10
para2_max=100
para3_min=10
para3_max=100
para4_min=10
para4_max=100
para5_min=10
para5_max=100
para6_min=10
para6_max=100
para7_min=10
para7_max=100
para8_min=10
para8_max=100
msg=' '

def search(request):
        obj = Test.objects.last()
        msg =''
        if int(obj.parameter1) > int(para1_max):
            msg += 'parameter1 increased to ' + obj.parameter1 + '\n'
        elif int(obj.parameter1) < int(para1_min):
            msg += 'parameter1 decreased to ' + obj.parameter1 + '\n'
        if int(obj.parameter2) > int(para2_max):
            msg += 'parameter2 increased to ' + obj.parameter2 + '\n'
        elif int(obj.parameter2) < int(para2_min):
            msg += 'parameter2 decreased to ' + obj.parameter2 + '\n'
        if int(obj.parameter3) > int(para3_max):
            msg += 'parameter3 increased to ' + obj.parameter3 + '\n'
        elif int(obj.parameter3) < int(para3_min):
            msg += 'parameter3 decreased to ' + obj.parameter3 + '\n'
        if int(obj.parameter4)>int(para4_max):
            msg += 'parameter4 increased to ' + obj.parameter4 + '\n'
        elif int(obj.parameter4) < int(para4_min):
            msg += 'parameter4 decreased to ' + obj.parameter4 + '\n'
        if int(obj.parameter5) > int(para5_max):
            msg += 'parameter5 increased to ' + obj.parameter5 + '\n'
        elif int(obj.parameter5) < int(para5_min):
            msg += 'parameter5 decreased to ' + obj.parameter5 + '\n'
        if int(obj.parameter6) > int(para6_max):
            msg += 'parameter6 increased to ' + obj.parameter6 + '\n'
        elif int(obj.parameter6) < int(para6_min):
            msg += 'parameter6 decreased to ' + obj.parameter6 + '\n'
        if int(obj.parameter7) > int(para7_max):
            msg += 'parameter7 increased to ' + obj.parameter7 + '\n'
        elif int(obj.parameter7) < int(para7_min):
            msg += 'parameter7 decreased to ' + obj.parameter7 + '\n'
        if int(obj.parameter8) > int(para8_max):
           msg += 'parameter8 increased to ' + obj.parameter8 + '\n'
        elif int(obj.parameter8) < int(para8_min):
            msg += 'parameter8 decreased to ' + obj.parameter8
            return render(request,'search.html',{'obj':obj})
        return render(request,'search.html', {'obj': obj})

def response(request):
    if request.method=='POST':
        dat1 = request.POST['srh']
        if dat1:
            obj = Test.objects.filter(Date__icontains=dat1)
            if obj:
                return render(request,"Responses.html",{"obj":obj})
            else:
                return render(request,'Abc.html')
        else:
            return HttpResponse("Please Enter Date!!")
    return render(request,'Responses.html')

def Generate(request):
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    obj1 = Test.objects.filter(Date__icontains=yesterday)
    if obj1:
        render(request, "index.html", {"obj1": obj1})
    else:
        return render(request, 'Abc.html')
    return render(request, "index.html", {"obj1": obj1})