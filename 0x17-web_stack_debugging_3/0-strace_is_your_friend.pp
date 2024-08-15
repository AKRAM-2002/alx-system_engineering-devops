# This Puppet manifest fixes the Apache 500 error by ensuring the necessary file permissions and starting the Apache service


exec { 'fix config typo':
  command => "sed -i 's/.phpp/.php/' /var/www/html/wp-settings.php",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}
