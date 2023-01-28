from django import forms
from .models import Post
class CreatePostForm(forms.ModelForm):
    # title = forms.CharField(max_length= 150)
    # content = forms.Textarea()
    class Meta:
        model = Post
        fields = ["title", "content"]
