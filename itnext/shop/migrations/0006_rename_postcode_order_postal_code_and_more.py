# Generated by Django 5.0.6 on 2024-05-23 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_order_orderitem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='postcode',
            new_name='postal_code',
        ),
        migrations.RemoveField(
            model_name='order',
            name='company_name',
        ),
        migrations.AddField(
            model_name='order',
            name='payment_method',
            field=models.CharField(default='Cash on Delivery', max_length=20),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.CharField(max_length=20),
        ),
    ]
