# Generated by Django 3.1.4 on 2021-01-07 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0016_remove_image_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='editprofile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
