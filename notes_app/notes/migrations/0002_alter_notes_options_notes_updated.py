# Generated by Django 5.1.2 on 2024-10-20 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notes',
            options={'ordering': ['updated', 'created']},
        ),
        migrations.AddField(
            model_name='notes',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
