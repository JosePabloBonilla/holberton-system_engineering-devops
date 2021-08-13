#install Puppet linter
package { 'task 1 puppet linter':
ensure   => '2.1.1',
provider => 'gem',
}
