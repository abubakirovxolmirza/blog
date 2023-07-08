from django import forms
from .models import Profile, BlogPost


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ( 'image',)


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title', 'slug', 'content', 'image')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title of the Blog'}),
            'slug': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'do not write a number here'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content of the Blog'}),
        }

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if BlogPost.objects.filter(slug=slug).exists():
            raise forms.ValidationError("A blog post with this slug already exists.")
        return slug
