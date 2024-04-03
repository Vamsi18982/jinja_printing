from django.shortcuts import render

# Create your views here.
def jinja_printing(request):
    d={'name':'vamsi','sname':'muneppagari','age':20}
    return render(request,'jinja_print.html',context=d)
