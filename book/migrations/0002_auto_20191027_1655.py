# Generated by Django 2.2 on 2019-10-27 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_thumbnail', models.URLField()),
                ('thumbnail', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='IndustryIdentifies',
            fields=[
                ('type', models.CharField(max_length=10)),
                ('identifier', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='image_links',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='book.ImageLinks'),
        ),
        migrations.RemoveField(
            model_name='book',
            name='industry_identifies',
        ),
        migrations.AddField(
            model_name='book',
            name='industry_identifies',
            field=models.ManyToManyField(to='book.IndustryIdentifies'),
        ),
    ]
