from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from .models import CustomUser
from .forms import CustomUserCreationFrom,CustomUserUpdateForm

class CustomUserAdmin(UserAdmin):
    #here we are jsut overwriting elements of the Adming class for the usermodel
    #in default all this stuff exists in kind of its own app in a way.

    #we are overwriting how to add a user with our custom creation form (which just saves it in the modiefied user model and
    #asks for age as well.
    add_form = CustomUserCreationFrom
    form = CustomUserUpdateForm
    model = CustomUser

admin.site.register(CustomUser,CustomUserAdmin)