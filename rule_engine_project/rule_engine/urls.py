from django.urls import path
from .views import home, create_rule, edit_rule

urlpatterns = [
    path('', home, name='home'),
    path('create_rule/', create_rule, name='create_rule'),
    path('edit_rule/', edit_rule, name='edit_rule'),
]
