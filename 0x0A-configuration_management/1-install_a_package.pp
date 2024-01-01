# install_flask.pp

# Include the stdlib module for package management
include stdlib

# Define a class for installing Python and pip3
class { 'python':
  version => '3',
}

package { 'python3-pip':
  ensure   => 'present',
  provider => 'pip3',
  require  => Class['python'],
}

# Install Flask version 2.1.0 and Werkzeug version 2.0.2 using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.0.2',
  provider => 'pip3',
  require  => Package['python3-pip'],
}
