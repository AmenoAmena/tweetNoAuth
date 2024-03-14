from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):

    class Meta:
        model = Tweet
        fields = ('title','content')

    def __init__(self, *args, **kwargs):
        super(TweetForm, self).__init__(*args, **kwargs)

        autofocus_field = 'title'
        if autofocus_field in self.fields:
            self.fields[autofocus_field].widget.attrs['autofocus'] = True
