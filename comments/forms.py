from django import forms
from django.contrib.auth import get_user_model

from comments.models import PostModel, Attachment
from comments.utils import validate_html
from captcha.fields import CaptchaField

UserModel = get_user_model()


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class PostCreateForm(forms.ModelForm):
    files = MultipleFileField(
        required=False,
        label="Attach Files",
    )
    captcha = CaptchaField(label="Captcha")

    class Meta:
        model = PostModel
        fields = ['text', 'parent', 'files']

    def clean_text(self):
        text = self.cleaned_data["text"]
        try:
            cleaned_text = validate_html(text)
        except ValueError as e:
            raise forms.ValidationError(f"Error in HTML tags")
        return cleaned_text

    def save(self, commit=True):
        post = super().save(commit=commit)

        files = self.cleaned_data.get('files')
        for file in files:
            Attachment.objects.create(
                post=post,
                file=file,
                file_type='image' if file.content_type.startswith('image') else 'text',
            )
        return post
