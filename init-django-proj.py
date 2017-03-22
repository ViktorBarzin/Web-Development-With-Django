'''
This script automates the process of creating a new django project.

Simply run it and it will walk you through starting project,
setting up superuser(optional), running initial migrations and creating a new app(optional)

NOTE: You must be in a virtual enviorment with django installed
'''


import os


BASE_DIR = os.getcwd()


class DjangoCommander(object):
    '''
    This class is responsible for issuing project initialization commands
    to OS
    '''
    def __init__(self, project_name):
        self.commands = []
        os.system('django-admin startproject {}'.format(project_name))

        self.path = os.path.join(BASE_DIR, project_name)
        # Changing dir to django project BASE_DIR
        os.chdir(self.path)


    def add_command(self, command):
        self.commands.append(command)

    def run_commands(self):
        for command in self.commands:
            os.system(command)

    def create_app(self, project_name, app_name):
        import ipdb; ipdb.set_trace() # BREAKPOINT

        os.system('python manage.py startapp {}'.format(app_name))
        # Registering app into settings.py
        os.system("sed -i \"/INSTALLED_APPS/a\ \ \ \ '{}',\" {}/settings.py".format(app_name, project_name))


def main():

    # Project name
    proj_name = input('Enter project name:')
    if proj_name is None or proj_name is '':
        print('Project name cannot be empty!')
        return

    commander = DjangoCommander(proj_name)


    # Main app name
    base_app_name = input('Enter base app name(leave empty if you don\'t want another app):')

    # run migrations
    commander.add_command('python manage.py migrate')
    # Create super user?
    add_super_user = input('Do you want to add super user?(y/N):')
    if add_super_user.lower() == 'y':
        commander.add_command('python manage.py createsuperuser')

    # Change cwd into project dir
    # Execute all commands
    commander.run_commands()

    if base_app_name:
        commander.create_app(proj_name, base_app_name)


if __name__ == "__main__":
    main()
