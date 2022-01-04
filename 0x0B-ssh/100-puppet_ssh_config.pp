# Adding lines to ssh_config using puppet
include stdlib

file_line { 'BatchMode':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no'
}

file line { 'IdentityFile':
  ensure => 'present',
  path   => 'etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.shh/school'
}
