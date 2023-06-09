# Generated by Django 4.2 on 2023-05-29 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isim', models.CharField(max_length=100)),
                ('resim', models.ImageField(upload_to='filmler/')),
                ('katgori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movies.kategori')),
            ],
        ),
    ]
