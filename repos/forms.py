from django import forms
from django.forms import ValidationError
from products.models import Projects , Contacts


#
# class ProductForm(forms.Form):
#     title = forms.CharField(required=True)
#     price = forms.FloatField(min_value=0)
#     stock = forms.IntegerField()
#     description = forms.Textarea()
#     thumbnail = forms.CharField()
#     rating = forms.FloatField(max_value=5)
#     category = forms.ModelChoiceField(Category.objects.all(), required=False)
#

class ProjectModelForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = '__all__'
