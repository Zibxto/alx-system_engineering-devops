# ssh configuration file spacification

file { '/home/zibxto/.ssh/ssh_config':
    ensure  => 'present',
    owner   => 'zibxto',
    group   => 'zibxto',
    mode    => '0744',
    content => 'Host test
                    HostName 100.25.15.14
                    User ubuntu
                    PubkeyAuthentication yes
                    IdentifyFile ~/.ssh/school
                    PasswordAuthentication no'
}