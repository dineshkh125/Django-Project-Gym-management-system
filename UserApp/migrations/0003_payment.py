# Generated by Django 4.0.4 on 2022-06-13 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_no', models.CharField(max_length=4)),
                ('expiry', models.CharField(max_length=10)),
                ('cvv', models.CharField(max_length=4)),
                ('balance', models.FloatField(default=20000)),
            ],
            options={
                'db_table': 'Payment',
            },
        ),
    ]