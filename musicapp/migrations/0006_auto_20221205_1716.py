# Generated by Django 3.0.8 on 2022-12-05 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0005_auto_20200712_1306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='language',
            field=models.CharField(choices=[('Russian', 'Russian'), ('English', 'English')], default='Hindi', max_length=20),
        ),
    ]
