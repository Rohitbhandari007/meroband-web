# Generated by Django 3.0.2 on 2020-08-31 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200901_0028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='videos',
            field=models.FileField(blank=True, default='none', upload_to='videos'),
        ),
    ]