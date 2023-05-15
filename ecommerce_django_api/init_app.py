# automate django migrate and superuser

import subprocess
import os
import random
import string

# Retrieve the current directory of the script
project_directory = os.path.dirname(os.path.abspath(__file__))

command_prefix = ["python", "manage.py"]

# Run migrations
subprocess.run(command_prefix + ["migrate"], cwd=project_directory)


def create_username():
    username_length = 8
    username = ''.join(random.choices(string.ascii_lowercase, k=username_length))
    return username


def create_password():
    password_length = 12
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(password_characters, k=password_length))
    return password


def is_exist(username):

    check_superuser_cmd = command_prefix + [
        "shell",
        "-c",
        f"from django.contrib.auth.models import User; print(User.objects.filter(username='{username}').exists())",
    ]
    existing_superuser = subprocess.run(
        check_superuser_cmd, capture_output=True, text=True
    ).stdout.strip()

    if existing_superuser == "True":
        return True
    return False


def main():
    username = create_username()
    password = create_password()
    if not is_exist(username):
        # Create a superuser
        subprocess.run(
            command_prefix
            + [
                "shell",
                "-c",
                f"from django.contrib.auth.models import User; User.objects.create_superuser('{username}', '', '{password}')",
            ]
        )
        print("Superuser created successfully.")
    else:
        print("Superuser already exists. Skipping creation.")

    print("Django migration and superuser creation completed successfully.")


if __name__ == '__main__':
    main()
