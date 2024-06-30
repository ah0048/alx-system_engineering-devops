#  using Puppet to make changes to our configuration file.
file_line { 'identity file for private key':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => '    IdentityFile ~/.ssh/school',
}

file_line { 'turn off passwd authentication':
    ensure => 'present',
    path   => '~/.ssh/config',
    line   => '    PasswordAuthentication no',
}
