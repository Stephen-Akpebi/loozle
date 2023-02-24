# Generated by Django 4.1 on 2023-02-24 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_alter_item_sales_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="sales_category",
            field=models.CharField(
                choices=[
                    ("best-sellers", "best-sellers"),
                    ("new-arrivals", "new-arrivals"),
                    ("hot-sales", "hot-sales"),
                ],
                max_length=20,
            ),
        ),
    ]
