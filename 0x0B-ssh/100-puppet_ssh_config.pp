#  using Puppet to make changes to our configuration file.
file_line { 'identity file for private key':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'turn off passwd authentication':
    ensure => 'present',
    path   => '/etc/ssh/ssh_config',
    line   => '    PasswordAuthentication no',
}
