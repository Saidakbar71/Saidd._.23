# Generated by Django 4.1.4 on 2022-12-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_language'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aloqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('text', models.TextField()),
            ],
        ),
    ]
