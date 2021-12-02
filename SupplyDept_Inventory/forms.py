from django.forms import ModelForm
from .models import deliveryrecords

class deliveryrecordsForm(ModelForm):
    class Meta:
        model = deliveryrecords
        fields = '__all__'
