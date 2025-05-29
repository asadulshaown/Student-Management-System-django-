
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Members

# for index page
def index_page(request):
  return render(request , 'index.html')


# data pass form registration page 
def registar(request):
 
  if request.method == 'POST':
    firstNmae = request.POST.get('first_name')
    lastName = request.POST.get('last_name')
    Roll = request.POST.get('roll')
    password = request.POST.get('password')
    
    if Members.objects.filter(roll=Roll).exists() or Members.objects.filter(password=password).exists():
      return HttpResponse('This roll already exists. Please use another one.')
        
    registarData = Members(firstname=firstNmae, lastname=lastName, roll=Roll, password=password)
    registarData.save()        
    return redirect('/')          
  else:  
      return render(request , "registar.html")

# get user data from Members table
def showData(request):
  user_all_data = Members.objects.all()
  usre_data = {'data':user_all_data}
  return render(request, 'showData.html', usre_data)
  


# for login page 
def login(request):
    user_all_data = Members.objects.all()
    data = {'data':user_all_data}
    if request.method == 'POST':
          user_roll = request.POST.get('roll')
          user_password = request.POST.get('password')
           
          for i in user_all_data:
            if user_roll == i.roll and user_password == i.password:
              return redirect('/show_data')
          else:
            return redirect('/registar') 
    else:
        return render(request, 'login.html')
      
def Edit(request, id):
  userData = Members.objects.get(id=id)
  return render(request, 'update.html', {'data':userData})

def update_data(request, id):
  first_name = request.POST['first_name']
  last_name = request.POST['last_name']
  roll = request.POST['roll']
  
  user_data = Members.objects.get(id=id) 
  user_data.firstname = first_name
  user_data.lastname = last_name
  user_data.roll = roll
  user_data.save()
  return redirect('/show_data')

def Delete(request, id):
  data = Members.objects.get(id=id)
  data.delete()
  return redirect('/show_data')
  