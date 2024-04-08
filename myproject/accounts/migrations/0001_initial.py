# Generated by Django 4.2.7 on 2023-12-09 07:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resident',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='resident', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(blank=True, max_length=50, null=True)),
                ('fname', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='resident',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_resident_email'),
        ),
        migrations.AddConstraint(
            model_name='admin',
            constraint=models.UniqueConstraint(fields=('email',), name='unique_admin_email'),
        ),
    ]