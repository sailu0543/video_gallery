from django import forms 
from app.models import *


class video_form(forms.ModelForm):
    class Meta:
       model =Videoplayer
       fields='__all__'