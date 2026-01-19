from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import resolve_url

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def get_signup_redirect_url(self, request):
        # Redirect to our custom set-password page after Google signup
        return resolve_url('set-password')