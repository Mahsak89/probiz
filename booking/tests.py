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


class BookingSubmitViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )

    def test_booking_submit_view_get(self):
        url = reverse('bookingSubmit')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookingSubmit.html')
