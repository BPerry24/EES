from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from EESAPI.serializers.SpillSerializer import SpillSerializer


class SpillDetail(APIView):
    authentication_classes = []
    permission_classes = []

    def get_object(self):
        pass

    def get(self, request, format=None):
        pass

    def post(self, request, format=None):
        pass
