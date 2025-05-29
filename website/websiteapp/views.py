
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Members

# for index page
def index_page(request):
  return render(request , 'index.html')


# data pass form registration page 
def registar(request):
  
  if request.method == 'POST':
    firstNmae = request.POST['first_name']
    lastName = request.POST['last_name']
    Roll = request.POST['roll']
    password = request.POST['password']
    registarData = Members(firstname=firstNmae, lastname=lastName, roll=Roll, password=password)
    registarData.save()
    return redirect('login/')
  else:  
    return render(request , "registar.html")

# get user data from Members table
def show_all_data(request):
  user_all_data = Members.objects.all()
  data = {'user_all_data':user_all_data}
  if login:
     return render(request, 'showData.html', data)
  else:
    return HttpResponse('please login')

# for login page 
def login(request):
    user_all_data = Members.objects.all()
    data = {'user_all_data':user_all_data}
    if request.method == 'POST':
          user_roll = request.POST.get('roll')
          user_password = request.POST.get('password') 
          for i in user_all_data:
            if user_roll == i.roll and user_password == i.password:
              return redirect('../show_data')
          else:
            return redirect('../registar') 
    else:
        return render(request, 'login.html')