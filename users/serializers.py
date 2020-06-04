__author__ = 'Nishanth'
from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *
from activity.models import ActivityPeriod
from pytz import timezone

date_formatter =  "%b %d %Y  %I:%M%p"

class ActivityPeriodSerializers(ModelSerializer):
    start_time = SerializerMethodField('starttime')
    end_time = SerializerMethodField('endtime')

    def starttime(self, activityperiod):
        timezone_str = activityperiod.user_id.timezone
        start_time = activityperiod.start_time.astimezone(timezone(timezone_str))
        return start_time.strftime(date_formatter)

    def endtime(self, activityperiod):
        timezone_str = activityperiod.user_id.timezone
        end_time = activityperiod.end_time.astimezone(timezone(timezone_str))
        return end_time.strftime(date_formatter)

    class Meta:
        model = ActivityPeriod
        fields = ('start_time', 'end_time')


class UserDetailsSerializer(ModelSerializer):
    tz = SerializerMethodField('time_zone')
    activity_periods = SerializerMethodField('periodactivities')

    def time_zone(self, user):
        return user.timezone

    def periodactivities(self, user):
        activity_periods = ActivityPeriod.objects.filter(user_id=user.id)
        result = ActivityPeriodSerializers(activity_periods, many=True)
        return result.data

    class Meta:
        model = User
        fields = ('id', 'real_name', 'tz', 'activity_periods')