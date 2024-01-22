# Inceases the amount of traffic an apache server can handle

# Increase limit
exec { 'fix-for-apache':
  command => '/bin/sed -i "s/MaxRequestWorkers 100/MaxRequestWorkers 4096/" /etc/apache2/apache2.conf',
  path    => '/usr/local/bin/:/bin/',
}

# Restart nginx
exec { 'apache-restart':
  command => 'etc/init.d/apache2 restart',
  path    => '/etc/init.d',
}
