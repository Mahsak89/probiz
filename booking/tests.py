from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date, timedelta
from .models import Appointment


class BookingViewTest(TestCase):
    def test_booking_view_get(self):
        url = reverse('booking')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'booking.html')
git 