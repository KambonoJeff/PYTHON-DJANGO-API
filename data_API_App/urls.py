##################################################################################
###############    FOREIGN CLASS IMPORTATIONS   #################################
################################################################################
from django.contrib import admin
from django.urls import path
from data_API_App.views import data_list, data_create, data_comb
from . import views
##################################################################################
###############    VIEW FUNCTIONALITY   ########################################
################################################################################
urlpatterns = [
    path('home1', data_create),  
    path('list/<int:pk>', data_comb),  
    path('list/', data_list),



     
    # path('shoplist/', views.ClassMethod.as_view()),  
   
]