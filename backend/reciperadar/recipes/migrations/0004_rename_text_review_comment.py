# Generated by Django 4.2.4 on 2023-09-02 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_review_rating'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='comment',
        ),
    ]
