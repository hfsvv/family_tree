from rest_framework.test import APITestCase
from django.urls import reverse
from family_app.enums import RelationTypes
from rest_framework import status
from unittest.mock import patch
from family_app.models import MemberRelationshipModel,MemberModel



class TestClosestDegree(APITestCase):
    
    
    def setUp(self):
        self.jenny = MemberModel.objects.create(name='Jenny Doe')
        self.jimmy = MemberModel.objects.create(name='Jimmy Doe')
        self.john = MemberModel.objects.create(name='John Doe')
        self.jane = MemberModel.objects.create(name='Jane Doe')
        self.james = MemberModel.objects.create(name='James Doe')
        self.jezza = MemberModel.objects.create(name='Jezaa Doe')
        self.jason = MemberModel.objects.create(name='Jason Doe')
        
        
        MemberRelationshipModel.objects.create(
            member1=self.jimmy,
            member2=self.jenny,
            relation_type=RelationTypes.CHILD.value
        )
      
        MemberRelationshipModel.objects.create(
            member1=self.jezza,
            member2=self.jimmy,
            relation_type=RelationTypes.CHILD.value
        )
        MemberRelationshipModel.objects.create(
            member1=self.john,
            member2=self.jenny,
            relation_type=RelationTypes.CHILD.value
        )
        MemberRelationshipModel.objects.create(
            member1=self.jane,
            member2=self.john,
            relation_type=RelationTypes.SPOUSE.value
        )
        MemberRelationshipModel.objects.create(
            member1=self.james,
            member2=self.jane,
            relation_type=RelationTypes.SIBLING.value
        )
        
        MemberRelationshipModel.objects.create(
            member1=self.jason,
            member2=self.james,
            relation_type=RelationTypes.CHILD.value
        )
        MemberRelationshipModel.objects.create(
            member1=self.jezza,
            member2=self.jason,
            relation_type=RelationTypes.SPOUSE.value
        )
      
      
    @patch('jwt.decode')
    def test_find_shortest_path(self,mock_jwt):
        url = reverse('shortest_path_count') + '?start=James Doe&end=Jenny Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['edge_count'], 3)
        url = reverse('shortest_path_count') + '?start=John Doe&end=James Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['edge_count'], 2)
        url = reverse('shortest_path_count') + '?start=Jenny Doe&end=Jane Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['edge_count'], 2)
        url = reverse('shortest_path_count') + '?start=Jason Doe&end=Jason Doe'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEqual(data['edge_count'], 1)

        url = reverse('shortest_path_count') + '?start=Jason Doe&end=Jason Does'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = response.json()
        self.assertEqual(data['error'], "Members not found")

