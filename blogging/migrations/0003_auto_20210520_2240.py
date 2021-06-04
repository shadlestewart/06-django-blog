# Generated by Django 3.1.5 on 2021-05-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0002_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "Categories"},
        ),
        migrations.RemoveField(
            model_name="category",
            name="posts",
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ManyToManyField(to="blogging.Category"),
        ),
    ]
