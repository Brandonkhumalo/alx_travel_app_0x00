from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    host_email = serializers.EmailField(source='host.email', read_only=True)

    class Meta:
        model = Listing
        fields = [
            'listing_id',
            'title',
            'description',
            'location',
            'price_per_night',
            'host',
            'host_email',
            'created_at'
        ]
        read_only_fields = ['listing_id', 'created_at', 'host_email']


class BookingSerializer(serializers.ModelSerializer):
    guest_email = serializers.EmailField(source='guest.email', read_only=True)
    listing_title = serializers.CharField(source='listing.title', read_only=True)

    class Meta:
        model = Booking
        fields = [
            'booking_id',
            'listing',
            'listing_title',
            'guest',
            'guest_email',
            'check_in',
            'check_out',
            'created_at'
        ]
        read_only_fields = ['booking_id', 'created_at', 'listing_title', 'guest_email']
