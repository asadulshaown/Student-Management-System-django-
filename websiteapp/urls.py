
from django.urls import path
from . import views

urlpatterns = [
  path('', views.index_page, name='home_page'),
  path('registar/', views.registar, name='registar'),
  path('login/', views.login, name='login_page'),
  path('show_data/', views.showData, name='show_data'),
  path('edit/<int:id>/', views.Edit, name='edit'),
  path('update/<int:id>', views.update_data, name='update'),
  path('delete/<int:id>', views.Delete, name='delete')
  
]