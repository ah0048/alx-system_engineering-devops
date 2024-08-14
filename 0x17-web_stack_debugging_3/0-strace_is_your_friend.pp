exec { 'fix phpp typo'
    provider => 'shell',
    command => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
