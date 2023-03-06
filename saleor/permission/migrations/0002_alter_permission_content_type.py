# Generated by Django 3.2.16 on 2022-12-21 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("permission", "0001_initial"),
        ("auth", "0013_auto_20221214_1224"),
    ]

    operations = [
        migrations.AlterField(
            model_name="permission",
            name="content_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="content_type",
                to="contenttypes.contenttype",
                verbose_name="content type",
            ),
        ),
    ]