# Generated by Django 2.1.15 on 2020-04-10 21:44

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=wagtail.core.fields.StreamField([('action_link', wagtail.core.blocks.StructBlock([('text', wagtail.core.blocks.CharBlock(label='Link text', required=True)), ('external_url', wagtail.core.blocks.URLBlock(label='URL', required=True)), ('new_window', wagtail.core.blocks.BooleanBlock(label='Open in new window', required=False))])), ('callout', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(default='Important', required=True)), ('heading_level', wagtail.core.blocks.IntegerBlock(default=3, help_text='The heading level affects users with screen readers. Default=3, Min=2, Max=4.', max_value=4, min_value=2, required=True)), ('body', wagtail.core.blocks.RichTextBlock(required=True))]))], default=''),
            preserve_default=False,
        ),
    ]
