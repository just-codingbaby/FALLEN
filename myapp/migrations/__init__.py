
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='itemfound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('place', models.TextField(default='Found this item near ..')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('contactme', models.CharField(default='email', max_length=150)),
                ('username', models.CharField(blank=True, default='NULL', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='itemlost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_title', models.CharField(max_length=100)),
                ('place', models.TextField(default='Lost this item near ..')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('contactme', models.CharField(default='email', max_length=150)),
                ('username', models.CharField(blank=True, default='NULL', max_length=100)),
            ],
        ),
    ]