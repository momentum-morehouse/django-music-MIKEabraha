from django import forms
from .models import Album 
import datetime



class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = [
            'albumtitle',
            'artistname',
           
           
            
            
        ]

        widgets = {
        'Released': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
         
class DateForm(forms.Form):
   day = forms.DateField(initial=datetime.date.today)
print(DateForm())       
        

