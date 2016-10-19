from __future__ import with_statement
from fabric.api import cd, run, env
from fabric.decorators import task

env.use_ssh_config = True
env.hosts = ['deploy5']

@task
def deploy():
    with cd('/var/www/vhosts/ifourhosting.co.uk/subs/sjb/repo'):
        run('git pull origin master')
        run('composer install')
