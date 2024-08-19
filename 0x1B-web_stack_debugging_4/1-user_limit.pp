# Fix open files with user holberton
exec { 'Fix hard limit':
    provider => 'shell',
    command  => 'sed -i "s/4/20000/; s/5/20000/" /etc/security/limits.conf'
}
