# Generated by Django 2.2 on 2019-10-28 16:22

from django.db import migrations
import partial_date.fields


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0004_auto_20191028_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=partial_date.fields.PartialDateField(),
        ),
    ]