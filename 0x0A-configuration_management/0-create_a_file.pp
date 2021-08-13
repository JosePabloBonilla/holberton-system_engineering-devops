#create file using puppet
file { 'file task 0':
path    => '/tmp/holberton',
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
