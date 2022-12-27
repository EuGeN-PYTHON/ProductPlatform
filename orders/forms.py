from datetime import datetime

from django import forms
from django.forms import SelectDateWidget, DateInput

from orders.models import Order, Feedback, ResponseOrder, Agreement


class CreateOrderForm(forms.ModelForm):
    """Форма для изменения данных в заказе"""

    class Meta:
        model = Order
        fields = ['category', 'name', 'description', 'end_time', 'quantity', 'delivery_address', 'units_quantity']
        widgets = {
            'end_time': (DateInput(attrs={'type': 'datetime-local'}))
        }

    def __init__(self, *args, **kwargs):
        super(CreateOrderForm, self).__init__(*args, **kwargs)

        self.fields['name'].widget.attrs['placeholder'] = "Введите наименование заказа"
        self.fields['name'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['category'].widget.attrs['placeholder'] = "Выберите категорию"
        self.fields['category'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['quantity'].widget.attrs['placeholder'] = "Введите количество"
        self.fields['quantity'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['units_quantity'].widget.attrs['placeholder'] = "Выберите единицу измерения"
        # self.fields['units_quantity'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['delivery_address'].widget.attrs['placeholder'] = "Введите адрес доставки"
        self.fields['delivery_address'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['end_time'].widget.attrs['min'] = datetime.now().strftime(
            "%Y-%m-%d %H:%M")
        self.fields['end_time'].widget.attrs['class'] = "datetimepicker"

        self.fields['description'].widget.attrs['placeholder'] = "Опишите детали заказа"


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name_user', 'email', 'issue', 'message', ]

    def __init__(self, *args, **kwargs):
        super(FeedbackForm, self).__init__(*args, **kwargs)
        self.fields['name_user'].widget.attrs['type'] = 'text'
        self.fields['name_user'].widget.attrs['id'] = 'name'
        self.fields['name_user'].widget.attrs['name'] = 'name'
        self.fields['name_user'].widget.attrs['placeholder'] = 'Имя...'
        self.fields['name_user'].widget.attrs['required'] = ''

        self.fields['email'].widget.attrs['type'] = 'text'
        self.fields['email'].widget.attrs['id'] = 'email'
        self.fields['email'].widget.attrs['name'] = 'email'
        self.fields['email'].widget.attrs['placeholder'] = 'Эл. почта...'
        self.fields['email'].widget.attrs['required'] = ''
        self.fields['email'].widget.attrs['pattern'] = '[^ @]*@[^ @]*'

        self.fields['issue'].widget.attrs['type'] = 'text'
        self.fields['issue'].widget.attrs['id'] = 'subject'
        self.fields['issue'].widget.attrs['name'] = 'subject'
        self.fields['issue'].widget.attrs['placeholder'] = 'Тема...'
        self.fields['issue'].widget.attrs['required'] = ''

        self.fields['message'].widget.attrs['name'] = 'user_message'
        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['id'] = 'user_message'
        self.fields['message'].widget.attrs['placeholder'] = 'Сообщение...'
        self.fields['message'].widget.attrs['required'] = ''


class ResponseOrderForm(forms.ModelForm):
    class Meta:
        model = ResponseOrder
        fields = ['price', 'offer']

    def __init__(self, *args, **kwargs):
        super(ResponseOrderForm, self).__init__(*args, **kwargs)
        self.fields['price'].widget.attrs['type'] = 'number'
        self.fields['price'].widget.attrs['min'] = '1'
        self.fields['price'].widget.attrs['step'] = '1'
        self.fields['price'].widget.attrs['id'] = 'price-suggestion'
        self.fields['price'].widget.attrs['placeholder'] = 'Предложение...'
        self.fields['price'].widget.attrs['required'] = 'True'
        self.fields['price'].widget.attrs['name'] = 'name'

        self.fields['offer'].widget.attrs['type'] = 'text'
        self.fields['offer'].widget.attrs['id'] = 'description'
        self.fields['offer'].widget.attrs['placeholder'] = 'Описание...'
        self.fields['offer'].widget.attrs['required'] = 'True'
        self.fields['offer'].widget.attrs['name'] = 'message'
        self.fields['offer'].widget.attrs['class'] = 'form-control'


class CreateAgreementForm(forms.ModelForm):
    """Форма для изменения данных в Соглашении"""

    class Meta:
        model = Agreement
        fields = ['customer_signer', 'customer_attorney', 'supplier_signer', 'supplier_attorney']

    def __init__(self, *args, **kwargs):
        super(CreateAgreementForm, self).__init__(*args, **kwargs)

        self.fields['customer_signer'].widget.attrs['placeholder'] = "Петрова Петра Петровича"
        self.fields['customer_signer'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['customer_attorney'].widget.attrs['placeholder'] = "Устава/Доверенности №... от..."
        self.fields['customer_attorney'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['supplier_signer'].widget.attrs['placeholder'] = "Иванова Ивана Ивановича"
        self.fields['supplier_signer'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"

        self.fields['supplier_attorney'].widget.attrs['placeholder'] = "Устава/Доверенности №... от..."
        self.fields['supplier_attorney'].widget.attrs['aria-describedby'] = "inputGroup-sizing-sm"
