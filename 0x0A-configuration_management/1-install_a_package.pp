#install Puppet linter
package { 'task 1 puppet linter':
ensure   => '2.5.0',
provider => 'gem',
}
