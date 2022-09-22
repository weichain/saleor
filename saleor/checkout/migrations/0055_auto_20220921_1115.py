# Generated by Django 3.2.15 on 2022-09-21 11:15

import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import saleor.core.utils.json_serializer


class Migration(migrations.Migration):

    dependencies = [
        ("checkout", "0054_alter_checkout_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="CheckoutMetadata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "private_metadata",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                        null=True,
                    ),
                ),
                (
                    "metadata",
                    models.JSONField(
                        blank=True,
                        default=dict,
                        encoder=saleor.core.utils.json_serializer.CustomJsonEncoder,
                        null=True,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.RemoveIndex(
            model_name="checkout",
            name="checkout_p_meta_idx",
        ),
        migrations.RemoveIndex(
            model_name="checkout",
            name="checkout_meta_idx",
        ),
        migrations.RemoveField(
            model_name="checkout",
            name="metadata",
        ),
        migrations.RemoveField(
            model_name="checkout",
            name="private_metadata",
        ),
        migrations.AddField(
            model_name="checkoutmetadata",
            name="checkout",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="metadata",
                to="checkout.checkout",
            ),
        ),
        migrations.AddIndex(
            model_name="checkoutmetadata",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["private_metadata"], name="checkoutmetadata_p_meta_idx"
            ),
        ),
        migrations.AddIndex(
            model_name="checkoutmetadata",
            index=django.contrib.postgres.indexes.GinIndex(
                fields=["metadata"], name="checkoutmetadata_meta_idx"
            ),
        ),
    ]