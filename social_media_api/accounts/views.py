from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'username': user.username,
            'email': user.email,
            'bio': user.bio
        })

# Create your views here.
