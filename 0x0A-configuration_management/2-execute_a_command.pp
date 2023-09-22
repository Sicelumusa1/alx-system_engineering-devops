#  Puppet manifest that kills a process named killmenow.
exec { 'kill_process':
  command => 'pkill killmenow',
  onlyif  => 'pgrep killmenow',
  path    => '/usr/bin:/bin',
}
