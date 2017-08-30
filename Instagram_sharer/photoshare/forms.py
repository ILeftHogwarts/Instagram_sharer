from django import forms
from .models import PostTags

class TagForm(forms.Form):
    select_tag = forms.ChoiceField(choices=[], required=False)

    def __init__ (self, *arg, **kwargs):
        super(TagForm, self).__init__(*arg,**kwargs)
        self.fields['select_tag'].choices = [(" ","All tags")]+[(cur_tag.tag,cur_tag.tag) for cur_tag in PostTags.objects.all()]
        self.fields['select_tag'].initial = [(" ","All tags")]