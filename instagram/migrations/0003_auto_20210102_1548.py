# Generated by Django 3.1.4 on 2021-01-02 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0002_auto_20210102_0305'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='myimage'),
        ),
    ]