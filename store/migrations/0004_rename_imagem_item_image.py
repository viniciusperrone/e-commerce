# Generated by Django 4.0.2 on 2022-02-25 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_item_imagem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='imagem',
            new_name='image',
        ),
    ]
