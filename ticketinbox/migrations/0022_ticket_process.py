# Generated by Django 3.1.7 on 2021-05-23 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0021_auto_20210504_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='process',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
