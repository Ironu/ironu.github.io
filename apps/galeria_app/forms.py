from django import forms
from .models import Comentarios
from django.forms import widgets

class ComentarioForm(forms.Form):
    model = Comentarios
    fields = ('autor', 'cuerpo_comentario')

    autor = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            "class":"form-control",
            "placeholder":"Ingresa tu nombre"
        })
    )

    cuerpo_comentario = forms.CharField(widget=forms.Textarea(
        attrs={
            "class":"form-control comment-textarea",
            "id":"comentario",
            "placeholder":"Dejame un comentario"
        }
    ))