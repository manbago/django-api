from rest_framework import serializers
from polls.models import Question,Choice

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice

class PollResultsSerializer(serializers.ModelSerializer):
    tracks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Question
        fields = ('question_text', 'pub_date', 'tracks')
