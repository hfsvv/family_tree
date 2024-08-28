from rest_framework import serializers
from family_app.models import MemberModel , MemberRelationshipModel

class MemberSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = MemberModel
        fields = ['name']
        
