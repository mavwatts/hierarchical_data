from django import forms 
from hierarchy_app.models import Pokemon
from mptt.forms import TreeNodeChoiceField

class PokemonForm(forms.ModelForm):
    parent = TreeNodeChoiceField(queryset=Pokemon.objects.all())

    class Meta: 
        model = Pokemon
        fields = ["name"]
