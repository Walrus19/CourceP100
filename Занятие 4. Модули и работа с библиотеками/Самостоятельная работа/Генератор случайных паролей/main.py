import random
def get_random_password(n=8) -> str:
      # TODO написать функцию генерации случайных паролей
    passw = [random.choice('qwertyuiopasdfghjklzxcvbnm01234567890QWERTYUIOPASDFGHJKLZXCVBNM') for _ in range(n)]
    return ''.join(passw)

print(get_random_password())
