# Generated by Django 2.2.12 on 2021-04-07 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0013_auto_20210407_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='source',
            field=models.CharField(choices=[('Email', 'Email'), ('Web-form', 'Web-form'), ('Social-media', 'Social-media')], max_length=30),
        ),
    ]
