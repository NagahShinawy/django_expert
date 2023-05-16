"""
automation of generate secret key
"""
import subprocess

command_prefix = ["python", "manage.py"]

secret_key = command_prefix + [
    "shell",
    "-c",
    f"from django.core.management.utils import get_random_secret_key; print(get_random_secret_key());",
]


secret_key = subprocess.run(
    secret_key, capture_output=True, text=True
).stdout.strip()

print(secret_key)
