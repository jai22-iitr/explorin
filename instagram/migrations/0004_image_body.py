# Generated by Django 3.1.4 on 2021-01-02 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_auto_20210102_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='body',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
