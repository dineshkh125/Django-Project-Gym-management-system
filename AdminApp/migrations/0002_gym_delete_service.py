# Generated by Django 4.0.4 on 2022-06-09 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdminApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('price', models.FloatField(default=300)),
                ('description', models.CharField(max_length=1000)),
                ('imageurl', models.ImageField(default='abc.jpg', upload_to='Images')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdminApp.category')),
            ],
            options={
                'db_table': 'Gym',
            },
        ),
        migrations.DeleteModel(
            name='Service',
        ),
    ]