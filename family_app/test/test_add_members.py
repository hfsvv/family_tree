from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from unittest.mock import patch
from family_app.models import MemberModel


class MemberTests(APITestCase):
    
    @patch('jwt.decode')
    def test_add_member(self,mock_decode):
        url = reverse('add_member')
        data =[ {'name': 'Alice'}]
        mock_decode.return_value = {"user_id":132}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(MemberModel.objects.count(), 1)
        self.assertEqual(MemberModel.objects.get().name, 'Alice')
