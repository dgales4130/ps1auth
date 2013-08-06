from fabric.api import *
from cuisine import *

def staging():
    env.root = '/srv/http/arbitrarion.com/app/'
    env.hosts = ['arbitrarion.com']
    env.mode = 'staging'

def production():
    env.root = '/srv/http/members.pumpingstationone.org/app'
    env.hosts = ['vm.pumpingstationone.org']
    env.mode = 'production'

def deploy():
    with cd('%(root)s' % env):
        run('git pull')
        with prefix('workon ps1auth'):
            run('pip install -r requirements/%(mode)s.txt' % env)
            run('./manage.py syncdb --noinput')
            run('./manage.py migrate --noinput')
            run('./manage.py collectstatic --noinput')
            run('killall /home/hef/.virtualenvs/ps1auth/bin/python2', warn_only=True)

