# Using Puppet to install flask from pip3

exec { 'pip install flask == 2.1.0':
    command => '/usr/bin/pip3 install flask==2.1.0'
}