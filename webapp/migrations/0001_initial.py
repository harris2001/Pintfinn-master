# Generated by Django 2.0.7 on 2018-10-25 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='kosits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highh', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='stocks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('datee', models.DateField(max_length=100)),
                ('closee', models.IntegerField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='kosits',
            name='portfolio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.stocks'),
        ),
    ]
