from rest_framework import serializers
from chief.models import chief

class chiefSerializer(serializers.ModelSerializer):
    class Meta:
        model=chief
        fields='__all__'
        read_only_field=['id']
