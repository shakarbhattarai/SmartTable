from rest_framework import serializers
from ResturantInfo.models import ResturantInfo, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return ResturantInfo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.CreatedAt = validated_data.get('CreatedAt', instance.CreatedAt)
        instance.ResturantName = validated_data.get('ResturantName', instance.ResturantName)
        instance.OwnerName = validated_data.get('OwnerName', instance.OwnerName)
        instance.District = validated_data.get('District', instance.District)
        instance.Address = validated_data.get('Address', instance.Address)
        instance.Trial = validated_data.get('Trial', instance.Trial)

        instance.save()
        return instance