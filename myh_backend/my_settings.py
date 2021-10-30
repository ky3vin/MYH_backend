# my_settings.py

SECRET = { 'secret':'django-insecure-mi-u(5!!i&3%h*)@32s+6z32-rc26$ryhjcp13k4_26s$eczws', }
ALGORITHM = 'HS256'
# settings.py에 있는 SECRET_KEY복사

EMAIL = {
    'EMAIL_BACKEND' : 'django.core.mail.backends.smtp.EmailBackend',
    'EMAIL_USE_TLS' : True,
    'EMAIL_PORT' : 587,
    'EMAIL_HOST_USER' : 'mooyahongik@gmail.com',
    'EMAIL_HOST_PASSWORD' : 'manager123!',
    'EMAIL_HOST' : 'smtp.gmail.com',
    'SERVER_EMAIL' : "mooyahongik@gmail.com",
    'DEFAULT_FROM_MAIL' : 'mooyahongik',
    #'REDIRECT_PAGE' : 'path("auth/login/", LoginAPI.as_view()),'
}