import subprocess

def create_virtualenv(venv_name):
    subprocess.run(["python", "-m", "venv", venv_name])

if __name__ == "__main__":
    venv_name = input("Введите имя виртуального окружения: ")
    create_virtualenv(venv_name)
