# Generated by Django 4.0.4 on 2022-04-21 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='descriptionShoes',
            field=models.TextField(default='pendiente', max_length=150),
        ),
        migrations.AddField(
            model_name='shoes',
            name='imageShoes',
            field=models.ImageField(default='*', upload_to='Images/imageShoes'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='priceShoes',
            field=models.FloatField(null=True),
        ),
    ]
