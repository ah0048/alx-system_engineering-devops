# fix nginx limit files
exec { 'fix ulimit':
    provider => 'shell',
    command  => 'sed -i s/15/5000/ /etc/default/nginx; service nginx restart',
}
