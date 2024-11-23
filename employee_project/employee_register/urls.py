from django.urls import path,include
from. import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'),      # Insert operation
    path('<int:id>/', views.employee_form, name='employee_update'),  # Update operation
    path('list/', views.employee_list, name='employee_list'),    # List all employees
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),  # Delete operation
]