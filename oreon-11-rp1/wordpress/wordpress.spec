%global source0_hash none

# Fedora spec file for wordpress
#
# License: MIT
# http://opensource.org/licenses/MIT
#
# Please preserve changelog entries
#
%global wp_content %{_datadir}/wordpress/wp-content

%global upstream_version 6.9.4
#global upstream_prever  RC5
#global upstream_lower   rc5

Summary:    Blog tool and publishing platform
URL:        https://wordpress.org/
Name:       wordpress
Version:    %{upstream_version}%{?upstream_prever:~%upstream_lower}
Release:    1%{?dist}
# Wordpress     is GPL-2.0-or-later
# php-simplepie is BSD-3-Clause
# php-getid3    is LGPL-3.0-or-later (or some others)
# php-mailer    is LGPL-2.1-only
License:    GPL-2.0-or-later AND BSD-3-Clause AND LGPL-3.0-or-later AND LGPL-2.1-only

Source0:    https://wordpress.org/%{name}-%{upstream_version}%{?upstream_prever:-%{upstream_prever}}.tar.gz
Source1:    wordpress-httpd-conf
Source2:    README.fedora.wordpress
Source3:    README.fedora.wordpress-mu
Source4:    wordpress-nginx-conf
# To minify JS assets
Source5:    wordpress-minify.php

# Patch out copyrighted text of Hello, Dolly
# (and replace it with Free Software Song)
Patch0: wordpress-6.8-hello.patch
# Adjust tinymce's media plugin not to use its SWF plugin. This changes
# 'p.getParam("flash_video_player_url",u.convertUrl(u.url+"/moxieplayer.swf"))'
# to 'false'
Patch3: wordpress-5.1-tinymce_noflash.patch
# We drop the SWF files from mediaelement
Patch4: wordpress-5.6-mediaelement_no_swf.patch
# RPM configuration:
# Path to installation
# Disable auto-updater
Patch5: wordpress-5.4-config.patch
# RPM are readonly
# disable version check and updated
# change DISALLOW_FILE_MODS default value to true
# ignore WP_AUTO_UPDATE_CORE (always false)
Patch6: wordpress-5.8-noupdate.patch
# Debian patch for jshint
Patch8: wordpress-5.1-remove-jshint-refs.patch

BuildArch: noarch
BuildRequires: php-cli
BuildRequires: php-patchwork-jsqueeze
BuildRequires: php(language) >= 7.2

Requires: webserver
Requires: php(httpd)
Suggests: httpd
# For directory ownership
Requires: httpd-filesystem
Requires: nginx-filesystem
Requires: php(language) >= 7.2
Requires: php-sodium
Requires: php-ctype
Requires: php-filter
Requires: php-mysqli

# From phpcompatinfo report for version 4.5.3
Requires: php-curl
Requires: php-dom
Requires: php-exif
Requires: php-fileinfo
Requires: php-gd
Requires: php-gettext
Requires: php-iconv
Requires: php-intl
Requires: php-json
Requires: php-libxml
Requires: php-mbstring
Requires: php-openssl
Requires: php-simplexml
Requires: php-xml
Requires: php-xmlreader
Requires: php-zip
Requires: php-zlib
Requires: httpd
# Unbundled
Requires: /etc/pki/ca-trust/extracted/pem/tls-ca-bundle.pem
# Bundled
# grep "SIMPLEPIE_VERSION'" wordpress/wp-includes/class-simplepie.php
Provides: bundled(php-simplepie) = 1.9.0
# grep ' VERSION '  wordpress/wp-includes/ID3/getid3.php
Provides: bundled(php-getid3) = 1.9.24
# grep ' VERSION ' wordpress/wp-includes/PHPMailer/PHPMailer.php
Provides: bundled(php-phpmailer)  = 7.0.0
Provides: wordpress-mu = %{version}-%{release}
Obsoletes: wordpress-mu < 2.9.3

%description
Wordpress is an online publishing / weblog package that makes it very easy,
almost trivial, to get information out to people on the web.

Important information in %{_pkgdocdir}/README.fedora

%prep
%setup -q -n wordpress

# swfupload can just die in its entirety
rm -rf wp-includes/js/swfupload

# remove .htaccess, protected by httpd config file
rm wp-content/plugins/akismet/.htaccess

# only for PHP < 7.0 without random_int
rm -rf wp-includes/random_compat
# only for PHP < 7.2 without sodium_crypto_box
rm -rf wp-includes/sodium_compat

%patch -P0 -p1 -b .dolly
%patch -P3 -p1
# Adjust mediaelement not to use its SWF
%patch -P4 -p1
%patch -P8 -p1

# We patch .js files, so minify them
php %{SOURCE5} \
  wp-includes/js/tinymce/plugins/media/plugin.js \
  wp-includes/js/tinymce/plugins/media/plugin.min.js
php %{SOURCE5} \
  wp-includes/js/mediaelement/mediaelement-and-player.js \
  wp-includes/js/mediaelement/mediaelement-and-player.min.js
php %{SOURCE5} \
  wp-includes/js/mediaelement/mediaelement.js \
  wp-includes/js/mediaelement/mediaelement.min.js

# Re-Generated the archive
arc=wp-includes/js/tinymce/wp-tinymce.js
grep "^// Source" $arc | while read a b c
do
  if [ -f $c ]; then
    echo -e "\n$a $b $c"
    cat $c
  else
    exit 1
  fi
done >$arc.tmp
if [ -s $arc.tmp ]; then
  gzip -c $arc > $arc.gz
  ls -l $arc*
  mv $arc.tmp $arc
else
  exit 1
fi

# Create RPM configuration
sed -e 's/\r//' wp-config-sample.php >wp-config.php
%patch -P5 -p1
%patch -P6 -p1

# fix file encoding
sed -i -e 's/\r//' license.txt

: Bundled library versions
grep ' VERSION '  wp-includes/SimplePie/src/SimplePie.php
grep ' VERSION '  wp-includes/ID3/getid3.php
grep ' VERSION '  wp-includes/PHPMailer/PHPMailer.php

%build

%install
# Apache configuration
install -m 0644 -D -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/wordpress.conf

install -m 0644 -D -p %{SOURCE4} ${RPM_BUILD_ROOT}%{_sysconfdir}/nginx/default.d/wordpress.conf

# Application
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/wordpress
cp -pr * ${RPM_BUILD_ROOT}%{_datadir}/wordpress

# Configuration
install -m 0644 -D wp-config.php ${RPM_BUILD_ROOT}%{_sysconfdir}/wordpress/wp-config.php
/bin/ln -sf ../../../etc/wordpress/wp-config.php ${RPM_BUILD_ROOT}%{_datadir}/wordpress/wp-config.php

/bin/cp %{SOURCE2} ./README.fedora
/bin/cp %{SOURCE3} ./README.fedora-multiuser

# Create additional wp-content directories so we can own them
install -d ${RPM_BUILD_ROOT}%{wp_content}/{plugins,themes,upgrade,uploads}

# Remove empty files to make rpmlint happy
find ${RPM_BUILD_ROOT} -type f -empty -exec rm -vf {} \;
# These are docs, remove them from here, docify them later
rm -f ${RPM_BUILD_ROOT}%{_datadir}/wordpress/{license.txt,readme.html}

# Remove bundled ca-bundle.crt
rm ${RPM_BUILD_ROOT}%{_datadir}/wordpress/wp-includes/certificates/ca-bundle.crt
ln -s %{_sysconfdir}/pki/ca-trust/extracted/pem/tls-ca-bundle.pem \
   ${RPM_BUILD_ROOT}%{_datadir}/wordpress/wp-includes/certificates/ca-bundle.crt

# Remove backup copies of patches
find ${RPM_BUILD_ROOT} \( -name \*.dolly -o -name \*.rhbz522897 -o -name \*.orig \) \
    -print -delete

%pretrans -p <lua>
-- Remove link to system library
path = "%{_datadir}/wordpress/wp-includes/PHPMailer"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files
%config(noreplace) %{_sysconfdir}/httpd/conf.d/wordpress.conf
%config(noreplace) %{_sysconfdir}/nginx/default.d/wordpress.conf
%dir %{_datadir}/wordpress
%{_datadir}/wordpress/wp-admin
%{_datadir}/wordpress/wp-includes
%{_datadir}/wordpress/index.php
%dir %{wp_content}/
%{wp_content}/index.php
%dir %attr(2775,apache,ftp) %{wp_content}/plugins
%dir %attr(2775,apache,ftp) %{wp_content}/themes
%dir %attr(2775,apache,ftp) %{wp_content}/upgrade
%dir %attr(2775,apache,ftp) %{wp_content}/uploads
%{wp_content}/plugins/*
%{wp_content}/themes/*
%{!?_licensedir:%global license %%doc}
%license license.txt
%doc readme.html
%doc README.fedora
%doc README.fedora-multiuser
%{_datadir}/wordpress/wp-*.php
%attr(750,root,apache) %dir               %{_sysconfdir}/wordpress
%attr(640,root,apache) %config(noreplace) %{_sysconfdir}/wordpress/wp-config.php
%{_datadir}/wordpress/xmlrpc.php

%changelog
%autochangelog
