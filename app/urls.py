from django.urls import path
from .views import *
from app import views

app_name = 'home'


urlpatterns = [
        path('', views.loginFunction,name='login'),
        path('reg/', views.Reg,name='reg'),
        path('productlist/', views.Productlist,name='productlist'),
        path('logout/',logoutView,name='logout'),
        path('addproduct/',addproduct,name='addproduct'),
        path('save_product/',Saveproduct,name='save_product'),
        path('editproduct/<str:id>',Editproduct,name='editproduct'),
        path('deleteproduct/<str:id>',DeleteProduct,name='deleteproduct'),
        path('addproductcatogery/',views.addproductcatogery,name="addproductcatogery"),
        path('Save_Category/',views.SaveCategory,name="Save_Category"),
        path('editcategory/<str:id>',Editcategory,name='editcategory'),
        path('categorylist/', views.categorylist,name='categorylist'),
        path('deletecategory/<str:id>',DeleteCategory,name='deletecategory'),
        



]