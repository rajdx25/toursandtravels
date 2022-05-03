from user.models import Feedback
from django import forms

class Form(forms.ModelForm):
    
    class Meta:
        model = Feedback
        fields = "__all__"
