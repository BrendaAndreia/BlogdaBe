# Generated by Django 4.1.4 on 2023-04-08 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginaApp', '0002_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(upload_to='post_imagens/'),
        ),
    ]
