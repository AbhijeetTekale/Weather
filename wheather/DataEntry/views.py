from django.shortcuts import render
from .forms import *
from django.http import *
import webbrowser
para1_max = 80
para1_min = 20
para2_max = 80
para2_min = 20
para3_max = 80
para3_min = 20
para4_max = 80
para4_min = 20
para5_max = 80
para5_min = 20
para6_max = 80
para6_min = 20
para7_max = 80
para7_min = 20
para8_max = 80
para8_min = 20
def home(request):
    if request.method == 'POST':
        form = Details(request.POST)
        if form.is_valid():
            form.save()
            obj = Test.objects.last()
            sms_start = 'http://sms.iotsystem.in/api/sendmsg.php?user=cbrozit&pass=123456789&sender=STUDIT&'
            sms_receiver = 'phone=7507594132&text='
            sms_end = '&priority=ndnd&stype=normal'
            msg = ''
            if int(obj.parameter1) > int(para1_max):
                msg += 'parameter1%20increased%20to%20' + obj.parameter1 + '%20'
            elif int(obj.parameter1) < int(para1_min):
                msg += 'parameter1%20decreased%20to%20' + obj.parameter1 + '%20'
            if int(obj.parameter2) > int(para2_max):
                msg += 'parameter2%20increased%20to%20' + obj.parameter2 + '%20'
            elif int(obj.parameter2) < int(para2_min):
                msg += 'parameter2%20decreased%20to%20' + obj.parameter2 + '%20'
            if int(obj.parameter3) > int(para3_max):
                msg += 'parameter3%20increased%20to%20' + obj.parameter3 + '%20'
            elif int(obj.parameter3) < int(para3_min):
                msg += 'parameter3%20decreased%20to%20' + obj.parameter3 + '%20'
            if int(obj.parameter4) > int(para4_max):
                msg += 'parameter4%20increased%20to%20' + obj.parameter4 + '%20'
            elif int(obj.parameter4) < int(para4_min):
                msg += 'parameter4%20decreased%20to%20' + obj.parameter4 + '%20'
            if int(obj.parameter5) > int(para5_max):
                msg += 'parameter5%20increased%20to%20' + obj.parameter5 + '%20'
            elif int(obj.parameter5) < int(para5_min):
                msg += 'parameter5%20decreased%20to%20' + obj.parameter5 + '%20'
            if int(obj.parameter6) > int(para6_max):
                msg += 'parameter6%20increased%20to%20' + obj.parameter6 + '%20'
            elif int(obj.parameter6) < int(para6_min):
                msg += 'parameter6%20decreased%20to%20' + obj.parameter6 + '%20'
            if int(obj.parameter7) > int(para7_max):
                msg += 'parameter7%20increase%20to%20' + obj.parameter7 + '%20'
            elif int(obj.parameter7) < int(para7_min):
                msg += 'parameter7%20decreased%20to%20' + obj.parameter7 + '%20'
            if int(obj.parameter8) > int(para8_max):
                msg += 'parameter8%20increased%20to%20' + obj.parameter8 + '%20'
            elif int(obj.parameter8) < int(para8_min):
                msg += 'parameter8%20decreased%20to%20' + obj.parameter8 + '%20'
            sms = sms_start + sms_receiver + msg + sms_end
            webbrowser.open(sms)
            return HttpResponse('Data Saved Successfully')

    else:
        form = Details()
    return render(request,'Entry.html',{'form':form})
