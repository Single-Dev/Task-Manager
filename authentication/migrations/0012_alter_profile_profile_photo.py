# Generated by Django 4.2.1 on 2023-07-29 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_profile_facebook_profile_github_profile_instagram_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, default='profile/profile.jpg', null=True, upload_to='profile'),
        ),
    ]