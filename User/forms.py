from django.forms import ModelForm

from User.models import Users


class UserCreationForm(ModelForm):

    class Meta:
        model = Users
        fields = ["email"]