from rest_framework.test import APITestCase
from django.urls import reverse
from family_app.enums import RelationTypes
from rest_framework import status
from unittest.mock import patch
from family_app.models import MemberRelationshipModel,MemberModel



class PathFindingTests(APITestCase):
    def setUp(self):
        self.member1 = MemberModel.objects.create(name='Alice')
        self.member2 = MemberModel.objects.create(name='Bob')
        self.member3 = MemberModel.objects.create(name='Charlie')
        
        MemberRelationshipModel.objects.create(
            member1=self.member1,
            member2=self.member2,
            relation_type=RelationTypes.PARENT.value
        )
        MemberRelationshipModel.objects.create(
            member1=self.member2,
            member2=self.member3,
            relation_type=RelationTypes.SIBLING.value
        )

    @patch('jwt.decode')
    def test_find_shortest_path(self,mock_jwt):
        url = reverse('shortest_path_count') + '?start=Alice&end=Charlie'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertIn('path', data)
        self.assertIn('edge_count', data)
        self.assertEqual(data['path'], ['Alice', 'Bob', 'Charlie'])
        self.assertEqual(data['edge_count'], 2)
