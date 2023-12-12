import os
import subprocess

def create_django_project(project_name):
    subprocess.run(["django-admin", "startproject", project_name])

if __name__ == "__main__":
    project_name = input("Введите имя проекта: ")
    create_django_project(project_name)
