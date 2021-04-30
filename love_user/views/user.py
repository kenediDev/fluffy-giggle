from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.core.mail import EmailMessage
from love_user.serializer.user_serializer import UserSerializer, UserModelSerializer


class UserAPIView(APIView):
    permission_classes = [
        permissions.AllowAny,
    ]
    serializer_class = UserSerializer

    def post(self, r):
        serializer = self.serializer_class(data=r.data)
        serializer.context["args"] = "reset"
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": _("Accounts has been reset")}, status=status.HTTP_200_OK
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserModelViewSets(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    serializer_query = UserSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [
                permissions.AllowAny,
            ]
        else:
            permission_classes = [
                permissions.IsAuthenticated,
            ]
        return [permission() for permission in permission_classes]

    def list(self, r):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, r):
        serializer = self.serializer_query(data=r.data)
        serializer.context["args"] = "create"
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": _("Accounts has been created")},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
