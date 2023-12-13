
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from users.tests.factory_user import UserFactory
from users.models import CustomUser


class TestApi(APITestCase):

    def setUp(self):
        # self.headerInfo = {'content-type': 'application/json'}
        self.password = "Vidhan!@#123"
        self.user = UserFactory(password=self.password)
        self.user.is_superuser = True
        self.user.save()

        self.token = str(AccessToken.for_user(self.user))


    def test_create_user(self):
        """ test POST method for User endpoint"""
        data = {
            "email": "vidhan@gmail.com",
            "password": "Vidhan!@#123",
            "type": "student",
            "phone": "7076838626"
        }
        reg_url = reverse('user-list')
        response = self.client.post(reg_url, data=data,)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_success(self):

        data = {
            'email': self.user.email,
            'password': self.password
        }

        response = self.client.post(reverse('token'), data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)

    def test_get_user_authenticated(self):

        url = reverse('user-list')
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_unauthenticated(self):

        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_user_authenticated(self):

        user_id = self.user.id
        url = reverse('user-detail', args=[user_id])
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_user_failed(self):

        user_id = 100
        url = reverse('user-detail', args=[user_id])
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_user_data(self):

        user_id = self.user.id
        url = reverse('user-detail', args=[user_id])
        data = {
            "email": "vidhan1@gmail.com"
        }
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_user_data(self):
        user_id = self.user.id
        url = reverse('user-detail', args=[user_id])
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # tearDown is mainly used for test file creation/reading,
    # spin off processes, open network connections, etc.
    def tearDown(self):
        CustomUser.objects.all().delete()
