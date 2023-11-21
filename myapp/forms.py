import datetime
from django import forms
from django.core.files.storage import FileSystemStorage

from myapp.models import Product


class ProductFormWidget(forms.Form):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter product name'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False)
    number = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    image = forms.ImageField()


class ProductChoiceForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(ProductChoiceForm, self).__init__(*args, **kwargs)
        self.fields['product_id'] = forms.ChoiceField(
            label='prod_id',
            choices=[(product.id, product.name) for product in Product.objects.all()]
        )


class ImageForm(forms.Form):
    image = forms.ImageField()

    def save(self):
        image = self.cleaned_data['image']
        fs = FileSystemStorage(location='media/product_photos/')
        filename = fs.save(image.name, image)
        return fs.url(filename)
