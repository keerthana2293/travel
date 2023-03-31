# Generated by Django 4.1.7 on 2023-02-24 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='people',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=250)),
                ('image1', models.ImageField(upload_to='pics')),
                ('desc1', models.TextField()),
            ],
        ),
    ]
