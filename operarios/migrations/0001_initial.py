# Generated by Django 3.2.10 on 2024-10-20 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Operario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legajo', models.CharField(max_length=100)),
                ('nombre', models.CharField(max_length=100)),
                ('puesto', models.JSONField()),
            ],
        ),
    ]
