# Generated by Django 4.1.3 on 2022-12-07 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='photo1',
            field=models.ImageField(default=1, upload_to='media/'),
            preserve_default=False,
        ),
    ]
