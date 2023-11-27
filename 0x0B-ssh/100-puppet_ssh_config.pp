# ssh configuration file spacification

#configure ssh config

file_line{ 'passauth':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}

file_line{ 'identity':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school'

}