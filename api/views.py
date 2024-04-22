import os
import json
import random
import secrets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from users.models import User
from .serializers import UserSerializer


class SendCodeView(APIView):
    """"Отправляет код подтверждения на номер телефона."""

    def post(self, request):
        phone_number = request.data.get('phone_number')

        # Создание случайного 4-значного кода подтверждения
        verification_code = ''.join(random.choices('0123456789', k=4))

        # Создание инвайт-кода
        invitation_code = secrets.token_hex(3)  # 3 байта (6 символов)

        # Проверяем, существует ли пользователь с таким номером телефона
        user_model = get_user_model()
        user, created = user_model.objects.get_or_create(
            phone_number=phone_number)

        # Если пользователь создан впервые, сохраняем инвайт-код
        if created:
            user.invitation_code = invitation_code
            user.save()

        # Отправка кода подтверждения
        if self.send_verification_code(
            phone_number,
            verification_code,
            invitation_code
        ):
            return Response(
                {"status": "Code sent", "invitation_code": invitation_code},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Failed to send code"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def send_verification_code(
            self,
            phone_number,
            verification_code,
            invitation_code
    ):
        """Сохраняет код подтверждения и инвайт-код в файл."""

        file_path = 'verification_code.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                verification_codes = json.load(file)
        else:
            verification_codes = {}

        verification_codes[phone_number] = verification_code

        # Добавление инвайт-кода вместе с кодом подтверждения
        verification_codes[phone_number + '_invite'] = invitation_code

        with open(file_path, 'w') as file:
            json.dump(verification_codes, file)

        return True


class VerifyCodeView(APIView):
    """""Проверяет код подтверждения и выполняет авторизацию."""

    def post(self, request):
        """Проверяет код подтверждения, переданный в запросе."""
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        if self.verify_verification_code(phone_number, code):
            return Response(
                {"status": "Code verified"},
                status=status.HTTP_200_OK
            )
        else:
            return Response(
                {"error": "Invalid verification code"},
                status=status.HTTP_400_BAD_REQUEST
            )

    def verify_verification_code(self, phone_number, code):
        """Проверяет код подтверждения для номера телефона."""
        file_path = 'verification_code.json'
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                verification_code = json.load(file)
                saved_code = verification_code.get(phone_number)
                if saved_code == code:
                    # удаляем код подтверждения после проверки
                    del verification_code[phone_number]
                    with open(file_path, 'w') as file:
                        json.dump(verification_code, file)
                    return True
        return False


class ProfileView(APIView):
    """Возвращает профиль пользователя."""

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)


class ActivateInviteView(APIView):
    """Активирует инвайт-код в профиле пользователя."""

    def post(self, request):
        invitation_code = request.data.get('invaiting_code')
        user = request.user

        if user.invitation_code:
            return Response(
                {"error": "User already has an activated invitation code"},
                status=status.HTTP_400_BAD_REQUEST
            )

        user.invitation_code = invitation_code
        user.save()
        return Response(
            {"status": "Invitation code activated"},
            status=status.HTTP_200_OK
        )


class InvitedUsersView(APIView):
    """Возвращает список пользователей, которых пригласил пользователь."""

    def get(self, request):
        user = request.user
        invited_users = user.invited_users.all()
        serializer = UserSerializer(invited_users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
