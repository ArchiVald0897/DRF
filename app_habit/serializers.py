from rest_framework import serializers

from app_habit.models import Habit
from app_habit.validators import RewardAndRelatedValidator, TimeToCompleteValidator, RelatedPleasantValidator, \
    PleasantHabitValidator, HabitFrequencyValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        validators = [
            RewardAndRelatedValidator(reward='reward', related='related_habit'),
            TimeToCompleteValidator(duration='time_to_complete'),
            RelatedPleasantValidator(pleasant='related_habit'),
            PleasantHabitValidator(pleasant='pleasant_sign', reward='reward', related='related_habit'),
            HabitFrequencyValidator(frequency='frequency', pleasant_sign='pleasant_sign')
            ]
