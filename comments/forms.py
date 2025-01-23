from django import forms
from django.contrib.auth import get_user_model

from comments.models import PostModel, Attachment
from captcha.fields import CaptchaField

UserModel = get_user_model()


class PostCreateForm(forms.ModelForm):
    file = forms.FileField(required=False, label="Attach File")
    captcha = CaptchaField(label="Captcha")

    class Meta:
        model = PostModel
        fields = ['text', 'parent', 'file']

    def save(self, commit=True):
        post = super().save(commit=commit)

        file = self.cleaned_data.get('file')
        if file:
            Attachment.objects.create(
                post=post,
                file=file,
                file_type='image' if file.content_type.startswith('image') else 'text',
            )
        return post
