from django import forms
from .models import Data

class DataForm(forms.ModelForm):

    class Meta:
        model = Data
        fields = '__all__'


    def __init__(self, *args, **kwargs):
        super(DataForm,self).__init__(*args, **kwargs)
       