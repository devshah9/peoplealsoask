# Generated by Django 4.1.3 on 2022-12-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paa', '0002_alter_keywordanswer_keywordofpaa_keywordvideos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='keywordgoogleimages',
            name='image',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='keywordimages',
            name='image',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='keywordvideos',
            name='video',
            field=models.CharField(max_length=5000),
        ),
    ]