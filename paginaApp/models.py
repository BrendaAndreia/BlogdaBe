from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField

class Tag(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post_list_by_tag', args=[str(self.name)])
    
class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    data_postagem = models.DateTimeField(auto_now_add=True)
    imagem = models.ImageField(upload_to='post_imagens/')
    tags = models.ManyToManyField(Tag, blank=True)
    slug = AutoSlugField(populate_from='titulo', unique=True, null=True, blank=True, default='')
    
    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

