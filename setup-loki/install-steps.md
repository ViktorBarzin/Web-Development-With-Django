# These are the steps to setup loki on you own machine
# NOTE: Tested on **Ubuntu 16.04**, should work on **14.04** as well

# REQUIREMENTS:
1. Internet access
2. root privileges (to install apps and libs)

# Side effects:
1. Creates virtual env named "loki"
2. Creates user postgres and grants him permission to project db
**1 Creates db named loki and does all the required setup steps
3. Installs npm and setups bower to install bower_components.

`sudo chmod +x install-libs.sh`

`sudo chmod +x setup-loki.sh`

`./install-libs.sh`
# Must be run with source or virtualenv breaks !!!
`source setup-libs.sh`

# Go to Loki/ and run `python manage.py runserver`
# Should be up with all the jquery stuff

# If something does not work, repeat the proccess as root
