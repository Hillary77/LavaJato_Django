# Generated by Django 4.2.5 on 2023-09-21 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servico', '0007_servico_identificador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='identificador',
        ),
    ]