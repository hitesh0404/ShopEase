from django import forms
from .models import Product


class ProductUpdateForm(forms.Form):
    name = forms.CharField(min_length=2,max_length=30,help_text="enter the Product name",required=True,label="Product Name")






















class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



