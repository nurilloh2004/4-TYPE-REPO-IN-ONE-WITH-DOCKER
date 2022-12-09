from django.shortcuts import render, get_object_or_404
from .models import Post
from django.http import Http404


def post_list(request, id):
    """Function for posting list."""
    try:
        post = Post.published.get(id=id)
    except Post.DoesNotExist:
        raise Http404('No Post Found.')

    return render(request, 'blog/post/list.html', {'post': post})
