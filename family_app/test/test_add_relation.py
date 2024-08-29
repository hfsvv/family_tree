from rest_framework.test import APITestCase
from django.urls import reverse
from family_app.enums import RelationTypes
from rest_framework import status
from unittest.mock import patch


from family_app.models import MemberRelationshipModel,MemberModel

class RelationshipTests(APITestCase):
    def setUp(self):
        self.member1 = MemberModel.objects.create(name='Alice')
        self.member2 = MemberModel.objects.create(name='Bob')

    @patch('jwt.decode')
    def test_add_relationship(self,mock_decode):
        url = reverse('add_relation')
        data = {
            'member1': self.member1.name,
            'member2': self.member2.name,
            'relation': RelationTypes.PARENT.value
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MemberRelationshipModel.objects.count(), 1)
        relationship = MemberRelationshipModel.objects.get()
        self.assertEqual(relationship.member1, self.member1)
        self.assertEqual(relationship.member2, self.member2)
        self.assertEqual(relationship.relation_type, RelationTypes.PARENT.value)
