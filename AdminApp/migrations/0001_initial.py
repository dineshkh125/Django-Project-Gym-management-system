# Generated by Django 4.0.4 on 2022-06-08 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=300)),
                ('description', models.CharField(max_length=100)),
                ('imageurl', models.ImageField(default='abc.jpg', upload_to='Images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category')),
            ],
            options={
                'db_table': 'Service',
            },
        ),
    ]
