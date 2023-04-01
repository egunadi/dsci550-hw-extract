from tika import translate

translated = translate.auto_from_buffer('Hola, amigo', 'en', requestOptions = {'timeout': 180})
print(translated)
