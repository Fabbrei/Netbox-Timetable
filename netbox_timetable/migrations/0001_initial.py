import django.contrib.postgres.fields
import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('extras', '0072_created_datetimefield'),
        ('ipam', '0057_created_datetimefield'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('cert_type', models.CharField(max_length=30)),
                ('common_name', models.CharField(max_length=255)),
                ('SAN_list', models.CharField(max_length=1000)),
                ('issue_date', models.DateField(blank=True, null=True)),
                ('expire_date', models.DateField()),
                ('device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='dcim.device')),
                ('virtual_machine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='virtualization.virtualmachine')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
            ],
            options={
                'ordering': ('common_name',),
            },
        )
    ]
