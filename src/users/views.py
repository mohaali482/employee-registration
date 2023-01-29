from rest_framework import permissions, views
from rest_framework.response import Response

from .serializers import UserSerializer


class UserProfile(views.APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Return the detail of the current user
        """
        user = request.user

        serializer = UserSerializer(user)

        return Response(serializer.data)
