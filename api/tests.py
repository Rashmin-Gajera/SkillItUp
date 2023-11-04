from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from skillitupcore.models import *


class AccountTests(APITestCase):
    def test_create_account(self):
        d1 = Domain(name="Medical",)
        d1.save()
        d2 = Domain(name="Science", )
        d2.save()
        sd1 = SubDomain(name="Physics", domain=d2)
        sd1.save()
        sd2 = SubDomain(name="Chemistry", domain=d2)
        sd2.save()
        sd3 = SubDomain(name="MBBS", domain=d1)
        sd3.save()
        """
        Ensure we can create a new account object.
        """
        response = self.client.get("/api/domains/2/", format='json')
        print(response.data)
        print("===========================")
        response = self.client.get("/api/topics/", format='json')
        print(response.data)
        print("===========================")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
