# This Puppet manifest fixes the Apache 500 error by ensuring the necessary file permissions and starting the Apache service

# Ensure the necessary file has the correct permissions
file { '/var/www/html/index.html':
  ensure  => file,
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0644',
}

# Ensure Apache is installed
package { 'apache2':
  ensure => installed,
}

# Ensure Apache service is running
service { 'apache2':
  ensure  => running,
  enable  => true,
}
