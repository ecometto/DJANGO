# Generated by Django 4.1.3 on 2022-12-21 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(max_length=50)),
                ('mail', models.EmailField(max_length=50)),
                ('passw', models.TextField(max_length=50)),
            ],
        ),
    ]
