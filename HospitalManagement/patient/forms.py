from django import forms



BG=(
    ('O+','O+'),
    ('O-','O-'),
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
)
DP=(
    ('hear','heart'),
    ('Ear','Ear')
)
class appointment_form(forms.Form):
    Blood_Group=forms.ChoiceField(label='Blood_group',choices=BG)
    Disease=forms.ChoiceField(label='department',choices=DP)
