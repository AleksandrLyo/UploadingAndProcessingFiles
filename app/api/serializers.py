from rest_framework import serializers
from files.models import File
from files.tasks import process_file


class FileSerializer(serializers.ModelSerializer):
    file = serializers.FileField(allow_empty_file=False, required=True)

    class Meta:
        model = File
        fields = ("file", "uploaded_at", "processed")
        read_only_fields = ("processed",)

    def create(self, validated_data):
        file = validated_data.pop("file")
        instance = File.objects.create(file=file, **validated_data)

        process_file.delay(instance.id)
        return instance