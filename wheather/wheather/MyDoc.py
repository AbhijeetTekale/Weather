from django.shortcuts import render
from django.core.mail import EmailMessage
import pdfkit
from DataEntry.models import Test
def Reports(request):
    obj = Test.objects.last()
    pdfkit.from_url('http://127.0.0.1:8000/report', 'Reports.pdf')
    msg=EmailMessage('Reports from your Weather app',
              'find an attachments of reports of your app',
              'abhijjeet4321@gmail.com',
              ['abhijeettekaleb@gmail.com'])
    msg.content_subtype = "html"
    msg.attach_file('Reports.pdf')
    msg.send()
    return render(request,'Search.html',{'obj':obj})