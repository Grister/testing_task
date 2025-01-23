from django.db import models
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class PostModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='replies'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Post by {self.user} - {self.text[:20]}"

    def is_root(self):
        return self.parent is None


class Attachment(models.Model):
    post = models.ForeignKey(PostModel, on_delete=models.CASCADE, related_name='attachments')
    file = models.FileField(upload_to='attachments/')
    file_type = models.CharField(max_length=10, choices=[
        ('image', 'Image'),
        ('text', 'Text')
    ])
    uploaded_at = models.DateTimeField(auto_now_add=True)


class LikeModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='likes')
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, related_name='likes')

    class Meta:
        unique_together = "user", "post"


class DislikeModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.PROTECT, related_name='dislikes')
    post = models.ForeignKey(PostModel, on_delete=models.PROTECT, related_name='dislikes')

    class Meta:
        unique_together = "user", "post"
