from django import forms 
from category.models import Category

class newcategory(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'



        labels={
        'name':'Select Category'
               }