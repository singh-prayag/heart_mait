# Generated by Django 4.1.6 on 2023-02-12 19:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("heartML", "0003_person_delete_topic"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="person", name="result", field=models.TextField(null=True),
        ),
    ]
