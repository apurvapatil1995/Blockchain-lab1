# Generated by Django 2.1.7 on 2019-02-15 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wapp', '0002_saleitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Txn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='buyer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='saleitem',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='txn',
            name='item_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='wapp.SaleItem'),
        ),
        migrations.AddField(
            model_name='txn',
            name='seller_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='seller', to=settings.AUTH_USER_MODEL),
        ),
    ]
