# Generated by Django 4.2.1 on 2023-06-09 05:59

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bulletins', '0007_subscribers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bulletin',
            name='bul_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]