# Generated by Django 4.1.3 on 2022-12-02 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paa', '0005_alter_keywordgoogleimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordgoogleimages',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='keywordimages',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='keywordrelated',
            name='related_search',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='keywordvideos',
            name='video',
            field=models.CharField(max_length=500),
        ),
    ]
