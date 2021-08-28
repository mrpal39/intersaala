from django import forms

from .models import Products


class ProductCreate(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['user',
                  'name',
                  'weight',
                  'price',
                  'stock',
                  ]
