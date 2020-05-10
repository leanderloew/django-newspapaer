from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from .models import CustomUser

class CustomUserCreationFrom(UserCreationForm):
    class Meta(UserCreationForm):
        # this kind of makes sense to me: when we create this form we are using the CustomUser instead of the ordinary user presumably
        # the meta class is about intercepting, and modifying the creation og the class here
        model=CustomUser

        #similarly, the fields (it is supposed to have) is in its meta class.
        #the meta class knows which fields the class should have, this isnt a feature of the class since the class doesnt really exist yet.
        #we are taking the fields its supposed to have and add the age field
        fields= UserCreationForm.Meta.fields + ("age",)


class CustomUserUpdateForm(UserChangeForm):

    class Meta(UserChangeForm):
        model=CustomUser
        #this desnt seem necessary to me
        fields = UserChangeForm.Meta.fields