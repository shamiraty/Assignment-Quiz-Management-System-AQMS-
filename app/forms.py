from django import forms
from .models import Programme, Stream, AcademicYear, YearOfStudy, Level, Assignment, Quiz
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class StudentSelectionForm(forms.Form):
    programme = forms.ModelChoiceField(queryset=Programme.objects.all(), widget=forms.Select(attrs={'class': 'select2'}))
    stream = forms.ModelChoiceField(queryset=Stream.objects.all(), widget=forms.Select(attrs={'class': 'select2'}))
    academic_year = forms.ModelChoiceField(queryset=AcademicYear.objects.all(), widget=forms.Select(attrs={'class': 'select2'}))
    year_of_study = forms.ModelChoiceField(queryset=YearOfStudy.objects.all(), widget=forms.Select(attrs={'class': 'select2'}))
    level = forms.ModelChoiceField(queryset=Level.objects.all(), widget=forms.Select(attrs={'class': 'select2'}))

    def __init__(self, *args, **kwargs):
        super(StudentSelectionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn btn-primary'))
