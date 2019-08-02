# Generated by Django 2.2.2 on 2019-06-25 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('context', models.TextField()),
                ('image', models.ImageField(upload_to='news/')),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]