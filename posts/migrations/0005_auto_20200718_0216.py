# Generated by Django 3.0.8 on 2020-07-17 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_remove_image_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='img/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
