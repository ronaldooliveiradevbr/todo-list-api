from rest_framework import serializers

from todo_api.api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ('summary', 'description', 'status', 'created_at', 'updated_at')
        read_only_fields = ('created_at', 'updated_at')

    def get_created_at(self, obj):
        return obj.created_at.strftime('%Y-%m-%dT%H:%M:%S')

    def get_updated_at(self, obj):
        return obj.updated_at.strftime('%Y-%m-%dT%H:%M:%S')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
