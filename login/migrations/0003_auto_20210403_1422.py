# Generated by Django 3.1.5 on 2021-04-03 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticketinbox', '0005_auto_20210403_1422'),
        ('login', '0002_auto_20210401_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='executive',
            name='id',
        ),
        migrations.AddField(
            model_name='executive',
            name='ticket_assigned',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ticketinbox.ticket'),
        ),
        migrations.AlterField(
            model_name='executive',
            name='executive_id',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
    ]