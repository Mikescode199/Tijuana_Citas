# Generated by Django 3.0.5 on 2020-05-01 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chicas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chica',
            name='imagen_profile',
            field=models.ImageField(blank=True, upload_to='chicas'),
        ),
    ]
