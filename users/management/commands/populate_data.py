__author__ = 'Nishanth'
import datetime
import random
import json

from django.core.management.base import BaseCommand

from users.models import User
from activity.models import ActivityPeriod
from django.conf import settings


class Command(BaseCommand):
    help = "Save users and activity records over months."

    def get_user_details(self, user):
        user_details = {'is_staff': True, 'is_active': True}
        user_details['id'] = user['id']
        user_details['real_name'] = user['real_name']
        user_details['timezone'] = user['tz']
        user_details['username'] = ''.join(user['real_name'].split(" "))
        user_details['email'] = ''.join(user['real_name'].split(" ")) + '@fullthrottle.com'
        return user_details

    def handle(self, *args, **options):
        test_file = settings.BASE_DIR + '\dumpdata\Test JSON.json'
        date_formatter =  "%b %d %Y  %I:%M%p"
        users_activity = json.loads(open(test_file).read())
        for user in users_activity['members']:
            user_details = self.get_user_details(user)
            user_instance = User.objects.create_user(**user_details)
            activity_periods = []
            for activity in user['activity_periods']:
                st_time = datetime.datetime.strptime(activity['start_time'], date_formatter)
                et_time = datetime.datetime.strptime(activity['end_time'], date_formatter)
                activity = ActivityPeriod(start_time=st_time, end_time=et_time, user_id=user_instance)
                activity_periods.append(activity)
            ActivityPeriod.objects.bulk_create(activity_periods)
        self.stdout.write(self.style.SUCCESS('User and ActivityRecords records saved successfully.'))