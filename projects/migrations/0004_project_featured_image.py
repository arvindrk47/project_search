# Generated by Django 4.2.7 on 2023-11-15 01:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_rename_vote_totoal_project_vote_total"),
    ]

    operations = [
        migrations.AddField(
            model_name="project",
            name="featured_image",
            field=models.ImageField(
                blank=True, default="default.jpg", null=True, upload_to=""
            ),
        ),
    ]
