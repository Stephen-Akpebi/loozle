# Generated by Django 4.1 on 2023-02-23 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0004_alter_item_sales_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="sales_category",
            field=models.CharField(
                choices=[
                    ("best-sellers", "best-sellers"),
                    ("new-arrivals", "new-aqrrivals"),
                    ("hot-sales", "hot-sales"),
                ],
                max_length=20,
            ),
        ),
    ]
