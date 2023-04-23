# Generated by Django 4.2 on 2023-04-22 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('category', models.CharField(choices=[('bussines', 'ビジネス'), ('life', '生活'), ('other', 'その他')], max_length=100)),
            ],
        ),
    ]
