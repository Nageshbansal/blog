
from django import forms
from .models import  Post , Comment

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post

        fields =('title','desc','body','img')
        labels = {'title':'Title','desc':'Description','body':'body'}
        widgets = {'title':forms.TextInput(attrs={'class':'form-control'}),
                   'desc': forms.TextInput(attrs={'class': 'form-control'}),
                   'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = False

        self.fields['desc'].required = False
        self.fields['body'].required = False





class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment

        fields = ['body']
        labels = {'body': 'body'}
        widgets = {
                   'body': forms.Textarea(attrs={'class': 'form-control'}),
                   }
