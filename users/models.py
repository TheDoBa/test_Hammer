from django.contrib.auth.models import AbstractUser
from django.db import models
import secrets

from core.consts import CODE_LENGTH, NUMBER_LENGTH


class User(AbstractUser):
    """Модель пользователя."""
    phone_number = models.CharField(max_length=NUMBER_LENGTH)
    is_varified = models.BooleanField(
        default=False)  # Исправлено на is_verified
    invaiting_code = models.CharField(
        max_length=CODE_LENGTH,
        null=True,
        blank=True
    )
    refferal_code = models.CharField(
        max_length=CODE_LENGTH,
        null=True,
        blank=True
    )

    def save(self, *args, **kwargs):
        if not self.pk:  # Если это новый пользователь
            # Генерируем инвайт-код только при создании пользователя
            self.invitation_code = self.generate_invitation_code()
        super().save(*args, **kwargs)

    def generate_invitation_code(self):
        """Генерирует инвайт-код."""
        return secrets.token_hex(3)  # 3 байта (6 символов)
