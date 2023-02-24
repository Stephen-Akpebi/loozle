# Generated by Django 4.1 on 2023-02-23 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="sales_category",
            field=models.CharField(
                choices=[
                    ("BS", "Best Sellers"),
                    ("NA", "New Arrivals"),
                    ("HS", "Hot Sales"),
                ],
                default="provide for each",
                max_length=2,
            ),
            preserve_default=False,
        ),
    ]