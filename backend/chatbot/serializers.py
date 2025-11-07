from rest_framework import serializers


class ChatRequestSerializer(serializers.Serializer):
    """
    Serializer برای دریافت ورودی از کاربر (prompt)
    """
    prompt = serializers.CharField(required=True, allow_blank=False, max_length=5000)


class ChatResponseSerializer(serializers.Serializer):
    """
    Serializer برای ارسال پاسخ مدل به فرانت‌اند
    """
    response = serializers.CharField()


# (اختیاری) اگر بعداً بخوای پیام‌ها رو در دیتابیس ذخیره کنی، یه مدل و Serializer زیرش می‌سازی:
# class ChatMessageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ChatMessage
#         fields = ['id', 'role', 'content', 'timestamp']
