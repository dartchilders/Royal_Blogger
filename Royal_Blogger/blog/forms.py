from django import forms
from .models import Post

# choices = Category.objects.all().values_list('name', 'name')

# choices_list = []

# for choice in choices:
#     choices_list.append(choice)


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'category', 'title', 'body', 'image', 'video']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'control is-flex is-justify-content-center', 'placeholder': 'Title'}),
            'author': forms.TextInput(attrs={'class': 'control is-flex is-justify-content-center', 'value': '', 'id': 'user', 'type': 'hidden'}),
            # 'category': forms.Select(choices=choices_list, attrs={'class': 'control is-flex is-justify-content-center', 'value': ''}),
            'body': forms.Textarea(attrs={'class': 'control mt-2', 'placeholder': 'Write post here...'}),
        }
