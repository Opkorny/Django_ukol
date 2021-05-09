from django.forms import ModelForm
from .models import *


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'measure', 'type', 'price', 'mark', 'akce', 'description', 'img']