from django import forms
from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    """Form used to create and edit blog posts."""

    class Meta:
        model = BlogPost
        fields = ['title', 'category', 'image', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter blog title'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 8,
                'placeholder': 'Write your blog content here...'
            }),
        }

    # Image is optional; title, category and content are required by default
    # because CharField/TextField/ChoiceField are required unless blank=True.
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required = False
