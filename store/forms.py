from django import forms

from .models import Order, Product


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ("first_name", "last_name", "address", "zipcode", "city",)
        widgets = {

            "first_name": forms.TextInput(attrs={
                'class': 'mt-2 mb-2 w-full p-2 border border-gray-200',
            }),

            "last_name": forms.TextInput(attrs={
                'class': 'mt-2 mb-2 w-full p-2 border border-gray-200',
            }),

            "address": forms.TextInput(attrs={
                'class': 'mt-2 mb-2 w-full p-2 border border-gray-200',
            }),

            "zipcode": forms.TextInput(attrs={
                'class': 'mt-2 mb-2 w-full p-2 border border-gray-200',
            }),

            "city": forms.TextInput(attrs={
                'class': 'mt-2 mb-2 w-full p-2 border border-gray-200',
            }),

        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("category", "title", "description", "price", "image",)
        widgets = {

            "category": forms.Select(attrs={
                'class': 'w-full p-4 border border-gray-200',
            }),

            "title": forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200',
            }),

            "description": forms.Textarea(attrs={
                'class': 'w-full p-4 border border-gray-200',
            }),

            "price": forms.TextInput(attrs={
                'class': 'w-full p-4 border border-gray-200',
            }),

            "image": forms.FileInput(attrs={
                'class': 'w-full p-4 border border-gray-200',
            }),

        }