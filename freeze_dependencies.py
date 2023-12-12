import subprocess

def freeze_dependencies(venv_name):
    subprocess.run([venv_name + "/bin/pip", "freeze", ">", "requirements.txt"], shell=True)

if __name__ == "__main__":
    venv_name = input("Введите имя виртуального окружения: ")
    freeze_dependencies(venv_name)
