# Generated by Django 4.2.4 on 2024-03-03 08:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_wtsuser_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wtsuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
