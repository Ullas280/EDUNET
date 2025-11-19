from rest_framework import serializers
from .models import Job, Application
from accounts.serializers import UserSerializer


class ApplicationSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    applicant = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = ('_id', 'applicant', 'createdAt')

    def get__id(self, obj):
        return str(obj.id)

    def get_applicant(self, obj):
        return str(obj.applicant.id)


class JobSerializer(serializers.ModelSerializer):
    _id = serializers.SerializerMethodField()
    applications = ApplicationSerializer(many=True, read_only=True)
    posted_by = UserSerializer(read_only=True)

    class Meta:
        model = Job
        fields = ('_id', 'id', 'title', 'description', 'location', 'position', 'jobType', 'salary', 'experience', 'posted_by', 'applications', 'createdAt')

    def get__id(self, obj):
        return str(obj.id)
