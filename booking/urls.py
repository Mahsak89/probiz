from django.urls import path
from .views import IndexView, BookingView, BookingSubmitView, UserPanelView, UserUpdateView, UserUpdateSubmitView, deleteAppointment

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('booking/', BookingView.as_view(), name='booking'),
    path('booking/submit/', BookingSubmitView.as_view(), name='bookingSubmit'),
    path('user/panel/', UserPanelView.as_view(), name='userPanel'),
    path('user/update/<int:id>/', UserUpdateView.as_view(), name='userUpdate'),
    path('user/update/submit/<int:id>/',
         UserUpdateSubmitView.as_view(), name='userUpdateSubmit'),
    path('delete/<int:id>/',
         deleteAppointment, name='appointmentDelete'),


]
