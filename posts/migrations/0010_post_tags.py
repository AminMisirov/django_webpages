# Generated by Django 5.1.4 on 2024-12-23 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_tag_description_alter_tag_created_at_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='posts.tag'),
        ),
    ]