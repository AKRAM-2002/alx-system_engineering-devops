# 1-user_limit.pp

exec { 'increase-file-descriptor-limit':
  command => 'echo "* - nofile 65536" >> /etc/security/limits.conf && echo "session required pam_limits.so" >> /etc/pam.d/common-session',
  path    => '/bin:/usr/bin:/sbin:/usr/sbin',
  onlyif  => 'grep -q "holberton" /etc/passwd',
}

