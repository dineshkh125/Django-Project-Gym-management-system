# Generated by Django 4.0.5 on 2022-06-26 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order_Master',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('date_of_order', models.DateField()),
                ('amount', models.FloatField(default=100)),
                ('product_details', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Order_Master',
            },
        ),
    ]
