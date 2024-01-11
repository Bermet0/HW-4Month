from django.urls import path
from . import views

urlpatterns = [
    path('male_list/', views.ClothListMale.as_view(), name='male_list'),
    path('female_list/', views.ClothListFemale.as_view(), name='female_list'),
    path('kids_list/', views.ClothListKids.as_view(), name='kids_list'),
    path('forall_list/', views.ClothListUni.as_view(), name='forall_list'),
    path('create_order/', views.CreateOrderView.as_view(), name='create_order'),
    path('cloth_list/', views.ClothList.as_view(), name='cloth_list'),
]