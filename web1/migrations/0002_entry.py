# Generated by Django 2.0.1 on 2018-01-16 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('topic', models.ForeignKey(on_delete=None, to='web1.Topic')),
            ],
            options={
                'verbose_name_plural': 'entries',
            },
        ),
    ]
