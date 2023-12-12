import os
import subprocess

def run_django_project(project_name):
    os.chdir(project_name)
    subprocess.run(["python", "manage.py", "runserver"])

if __name__ == "__main__":
    project_name = input("Введите имя проекта: ")
    run_django_project(project_name)
