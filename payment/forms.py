from django import forms
from .models import ShippingAddress


class ShippingForm(forms.ModelForm):
    shipping_full_name = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره نام کامل خود را وارد کنید'}),required=True)
    shipping_email = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شماره ایمیل  خود را وارد کنید'}),required=False)
    shipping_address1 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس اول خود را وارد کنید'}), required=False)
    shipping_address2 = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'آدرس دوم خود را وارد کنید'}), required=False )
    shipping_city = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'شهر خود را وارد کنید'}), required=False)
    shipping_state  = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'منطقه خود را وارد کنید'}), required=False)
    shipping_zipcode = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کد پستی خود را وارد کنید'}), required=False)
    shipping_country = forms.CharField(label="",widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'کشور خود را وارد کنید'}), required=False)

    class Meta:
        model = ShippingAddress
        fields = [
            'shipping_full_name',
            'shipping_email',
            'shipping_address1',
            'shipping_address2',
            'shipping_city',
            'shipping_state',
            'shipping_zipcode' ,
            'shipping_country',
                ]
       
        # exclude = ['user',]
