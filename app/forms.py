from django import forms
class file_info(forms.Form):
    file=forms.ImageField()
    des=forms.CharField(max_length=500)