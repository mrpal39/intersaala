# Generated by Django 3.2.6 on 2021-08-27 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_delete_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='profile_pics'),
        ),
    ]
