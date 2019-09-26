from django import forms
from .models import *



class AddReview(forms.Form):
	OPTIONS = (
	 	('yangon','Yangon'),
	 	('mandalay','Mandalay'),
	 	('bagan','Bagan'),
      
        	)
	reviewer = forms.CharField(label='Reviewer Name', max_length=100)
	place_name = forms.ChoiceField(label='Place Name', required=True, choices=OPTIONS)
	image = forms.ImageField()
	review = forms.CharField(label='Review', widget=forms.Textarea)
    # pub_date = forms.DateTimeField()


