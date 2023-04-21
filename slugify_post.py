from django.utils.text import slugify
from paginaApp.models import Post

for post in Post.objects.all():
    post.slug = slugify(post.titulo)
    post.save()
