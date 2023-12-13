# from rest_framework.test import APIRequestFactory

# factory = APIRequestFactory()
# request = factory.post('/assessment/', {'course': 1,
#                                         'title': 'new assess',
#                                         'duration': '00:05:00',
#                                         'type': 'mcq'})

# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from assessment.models import Assessment

# class AccountTests(APITestCase):
#     def test_create_account(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse('api/assessment/create/')
#         data = {"course": 1,
#                 "title": "new assess",
#                 "duration": "00:05:00",
#                 "type": "mcq"
#                 }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Assessment.objects.count(), 1)
#         self.assertEqual(Assessment.objects.get().name, 'DabApps')