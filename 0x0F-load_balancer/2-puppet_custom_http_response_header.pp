# creating a custom HTTP header response with Puppet.

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  service { 'nginx':
    ensure => running,
    enable => true,
  }

  file { '/etc/nginx/conf.d/custom.conf':
    ensure  => file,
    content => "add_header X-Served-By $::hostname;",
    notify  => Service['nginx'],
  }
}
