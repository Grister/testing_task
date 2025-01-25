from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from comments.models import PostModel, LikeModel, DislikeModel

from comments import models
from comments.forms import PostCreateForm


class PostView(LoginRequiredMixin, CreateView, ListView):
    model = models.PostModel
    template_name = 'comments/index.html'
    paginate_by = 25
    form_class = PostCreateForm
    login_url = '/sign-in/'
    success_url = reverse_lazy('comments:index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        parent_id = form.cleaned_data.get('parent')
        if parent_id:
            form.instance.parent = parent_id
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        return super().post(request, *args, **kwargs)

    def get_queryset(self):
        queryset = models.PostModel.objects.filter(parent=None).prefetch_related('replies', 'user')
        filter_value = self.request.GET.get('filter', 'newest')

        if filter_value == 'username':
            queryset = queryset.order_by('user__username')
        elif filter_value == 'email':
            queryset = queryset.order_by('user__email')
        elif filter_value == 'newest':
            queryset = queryset.order_by('-created_at')
        elif filter_value == 'oldest':
            queryset = queryset.order_by('created_at')

        return queryset


@csrf_exempt
@login_required
def like_post(request, post_id):
    post = get_object_or_404(PostModel, pk=post_id)
    like, created = LikeModel.objects.get_or_create(user=request.user, post=post)

    if not created:
        like.delete()
        return redirect('comments:index')
    else:
        DislikeModel.objects.filter(user=request.user, post=post).delete()
        return redirect('comments:index')


@csrf_exempt
@login_required
def dislike_post(request, post_id):
    post = get_object_or_404(PostModel, pk=post_id)
    dislike, created = DislikeModel.objects.get_or_create(user=request.user, post=post)

    if not created:
        dislike.delete()
        return redirect('comments:index')
    else:
        LikeModel.objects.filter(user=request.user, post=post).delete()
        return redirect('comments:index')
