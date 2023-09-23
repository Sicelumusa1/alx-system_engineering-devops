#  Create a file in /tmp with 0744 permissions, www-data as owner and group and contents 'I love Puppet'

file { '/tmp/school':
  ensure  => 'file',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
