from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(max_length=255)
    tags = forms.CharField(max_length=500)
    content = forms.CharField(widget=forms.Textarea)


class CommentForm(forms.Form):
    author_email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
