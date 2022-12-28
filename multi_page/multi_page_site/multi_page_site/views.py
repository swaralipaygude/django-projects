from django.shortcuts import render
from . import ml_model              # custom script for ML

def home(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def result(request):
    user_input = request.GET['user_ip']          # to get user ip in a var
    user_input = user_input.upper()
    num_input = request.GET['num_ip']
    num_input = ml_model.multiplier(num_input)
    return render(request,'result.html', {'form_name':user_input,'form_num':num_input})
    # 'form_name','form_num' are used to display val in result.html
