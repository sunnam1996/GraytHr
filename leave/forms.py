from django import forms
from django.forms import Select
from .models import *



class Leavetypecreateform(forms.ModelForm):


    class Meta:
        model = Leavetype
        fields = ['type',]


class Leaveapplyform(forms.ModelForm):
    # apply_to=forms.ChoiceField(choices=[])
    class Meta:
        model = Leaveapply
        fields = ['leavetype', 'from_date', 'to_date', 'from_session', 'to_session', 'apply_to', 'by', 'reason', 'cc_to']
        widgets = {
            'apply_to': Select(attrs={'class': 'select'}),
        }

    def __init__(self, *args, **kwargs):
        self.leads = kwargs.pop('leads', None)
        super(Leaveapplyform, self).__init__(*args, **kwargs)
        try:
            self.fields['apply_to'].choices = [(v.id,v)for k,v in self.leads.items()]
        except:
            pass


class Leavebalanceform(forms.ModelForm):
    class Meta:
        model = Leavebalance
        fields = ['balance', 'assign_leave_to', 'leavetype']


