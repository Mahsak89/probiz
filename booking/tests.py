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


class UserUpdateViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        # Create a test appointment
        self.appointment = Appointment.objects.create(
            user=self.user, service='Test Service', day=date.today(), time='3 PM'
        )

    def test_user_update_view_get(self):
        url = reverse('userUpdate', args=[self.appointment.id])
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userUpdate.html')


class UserUpdateSubmitViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        # Create a test appointment
        self.appointment = Appointment.objects.create(
            user=self.user, service='Test Service', day=date.today(), time='3 PM'
        )

    def test_user_update_submit_view_get(self):
        url = reverse('userUpdateSubmit', args=[self.appointment.id])
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userUpdateSubmit.html')


class UserPanelViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='testpassword'
        )
        # Create some test appointments for the user
        self.appointment1 = Appointment.objects.create(
            user=self.user, service='Service 1', day=date.today(), time='3 PM'
        )
        self.appointment2 = Appointment.objects.create(
            user=self.user, service='Service 2', day=date.today() + timedelta(days=1), time='4 PM'
        )

    def test_user_panel_view_get(self):
        url = reverse('userPanel')
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'userPanel.html')

        appointments = response.context['appointments']
        self.assertEqual(len(appointments), 2)
