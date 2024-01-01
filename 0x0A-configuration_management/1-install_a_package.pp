# Using Puppet, install flask from pip3

class { 'python':
  version => 'present',
}

package { 'python3-pip':
  ensure   => 'present',
  provider => 'pip3',
  require  => Class['python'],
}

package { 'Werkzeug':
  ensure   => 'latest',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
