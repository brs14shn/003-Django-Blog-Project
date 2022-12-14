from django import forms

from .models import Post, Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','content','post_image','category','status')


class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=('comment',)
        labels={'comment':'Comment'}