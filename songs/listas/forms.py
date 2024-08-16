from django import forms

class songForm(forms.Form):
    name = forms.CharField(label="Nombre de la canción", max_length=30)
    descripcion = forms.CharField(widget=forms.Textarea())