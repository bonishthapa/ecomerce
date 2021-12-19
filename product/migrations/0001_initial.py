# Generated by Django 2.2.13 on 2021-12-19 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('discount_price', models.FloatField(blank=True, null=True)),
                ('price', models.FloatField()),
                ('category', models.CharField(choices=[('S', 'Shirt'), ('SW', 'Sport Wear'), ('OW', 'Outwear')], max_length=2)),
                ('label', models.CharField(choices=[('P', 'Primary'), ('S', 'Secondary'), ('D', 'Danger')], max_length=1)),
                ('slug', models.SlugField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
