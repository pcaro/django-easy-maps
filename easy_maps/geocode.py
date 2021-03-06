# -*- coding: utf-8 -*-
from __future__ import absolute_import
from django.utils.encoding import smart_str
from geopy import geocoders
from geopy.exc import GeocoderServiceError


class Error(Exception):
    pass


def google_v3(address):
    """
    Given an address, return ``(computed_address, (latitude, longitude))``
    tuple using Google Geocoding API v3.
    """
    try:
        g = geocoders.GoogleV3()
        address = smart_str(address)
        results = g.geocode(address, exactly_one=False)
        if results is not None:
            return results[0]
        raise Error('No results found')
    except (UnboundLocalError, ValueError, GeocoderServiceError) as e:
        raise Error(e)
