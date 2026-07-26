%global source0_hash none

%define moodlewebdir %{_var}/www/moodle/public
%define moodledatadir %{_var}/www/moodle/data

# Suppress finding Perl libraries supplied by filter/algebra/*.p?
%define __perl_requires %{nil}
%define __perl_provides %{nil}

Name:           moodle
Version:        5.1.3
Release:       	1%{?dist}
Summary:        A Course Management System

License:        GPL-2.0-or-later
URL:            https://moodle.org/
Source0:        https://download.moodle.org/download.php/direct/stable501/%{name}-%{version}.tgz
Source1:        moodle.conf
Source2:        moodle-config.php
Source3:        moodle.cron
Source4:        moodle-cron
Source5:        moodle.service
Source6:        moodle-README-rpm
BuildArch:      noarch

BuildRequires:  perl-generators
BuildRequires:  unzip
Requires:       php-gd dailyjobs mimetex perl(lib) php-mysqlnd
Requires:       perl(Encode) hunspell perl(HTML::Parser) php
Requires:       perl(HTML::Entities) perl(CGI)
Requires:	php-adodb
Requires:	gnu-free-sans-fonts
Requires:	php-markdown
Requires:       php-simplepie
Requires:       php-soap
Requires:	php-pear-OLE
Requires:       php-pecl-xmlrpc
Requires:	crontabs

BuildRequires:  systemd-rpm-macros

Provides: bundled(php-tcpdf)
Provides: bundled(php-google-apiclient1)

Provides: php-google-apiclient1 = 1.1.7-14
Obsoletes: php-google-apiclient1 < 1.1.7-14

%description
Moodle is a course management system (CMS) - a free, Open Source software
package designed using sound pedagogical principles, to help educators create
effective online learning communities.

%prep
%setup -q -n %{name}
cp %{SOURCE6} README-rpm

find . -type f \! -name \*.pl -exec chmod a-x {} \;
find . -name \*.cgi -exec chmod a+x {} \;

%build
rm config-dist.php

#Drop precompiled flash
find . -type f -name '*.swf' | xargs rm -f

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{moodlewebdir}
mkdir -p %{buildroot}%{moodledatadir}
cp -a * %{buildroot}%{_var}/www/moodle/
install -p -D -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/moodle.conf
install -p -D -m 0644 %{SOURCE2} %{buildroot}/var/www/moodle/config.php
install -p -D -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/cron.d/moodle
install -p -D -m 0755 %{SOURCE4} %{buildroot}%{_sbindir}/moodle-cron
install -p -D -m 0644 %{SOURCE5} %{buildroot}%{_unitdir}/moodle.service
find %{buildroot} -name \*.mimetex-\* -exec rm {} \;
rm -f %{buildroot}${moodlewebdir}/pix/.cvsignore

#use system adodb
rm -rf %{buildroot}%{moodlewebdir}/lib/adodb
ln -s /usr/share/php/adodb/ %{buildroot}%{moodlewebdir}/lib/adodb

#Symlink to FreeSans, to save space.
rm -f %{buildroot}%{moodlewebdir}/lib/default.ttf
ln -s /usr/share/fonts/gnu-free/FreeSans.ttf %{buildroot}%{moodlewebdir}/lib/default.ttf

#use system markdown
rm -rf %{buildroot}%{moodlewebdir}/lib/markdown.php
ln -s /usr/share/php/markdown.php %{buildroot}%{moodlewebdir}/lib/markdown.php

#use system php-pear-OLE
rm -rf %{buildroot}%{moodlewebdir}/lib/pear/OLE
ln -s /usr/share/pear/OLE %{buildroot}%{moodlewebdir}/lib/pear/OLE

#use system php-simplepie
cp -p %{buildroot}%{moodlewebdir}/lib/simplepie/moodle_simplepie.php .
rm -rf %{buildroot}%{moodlewebdir}/lib/simplepie
mkdir -p %{buildroot}%{_datadir}/php/php-simplepie
ln -s /usr/share/php/php-simplepie/ %{buildroot}%{moodlewebdir}/simplepie
cp -p moodle_simplepie.php %{buildroot}%{_datadir}/php/php-simplepie

%post
%systemd_post moodle.service

if [ -d %{moodlewebdir}/lib/adodb -a ! -L %{moodlewebdir}/lib/adodb ]; then
  mv %{moodlewebdir}/lib/adodb %{moodlewebdir}/adodb.rpmbak && \
  ln -s /usr/share/php/adodb/ %{moodlewebdir}/lib/adodb
  rm -rf %{moodlewebdir}/lib/adodb.rpmbak
fi

if [ ! -L %{moodlewebdir}/lib/adodb ]; then
  ln -s /usr/share/php/adodb/ %{moodlewebdir}/lib/adodb
fi

if [ ! -L %{moodlewebdir}/lib/pear/OLE ]; then
  ln -s /usr/share/pear/OLE %{moodlewebdir}/lib/pear/OLE
fi

%preun
%systemd_preun moodle.service

%postun
%systemd_postun_with_restart moodle.service

%pretrans -p <lua>
-- Remove symlinks that will become directories
dirs = {"%{moodlewebdir}/lib/magpie", "%{moodlewebdir}/lib/google", "%{moodlewebdir}/auth/cas", "%{moodlewebdir}/auth/cas/CAS"}
for i, path in ipairs(dirs) do
  st = posix.stat(path)
  if st and st.type == "link" then
    os.remove(path)
  end
end

-- Remove directories that will become symlinks
dirs = {"%{moodlewebdir}/auth/cas/CAS"}
for i, path in ipairs(dirs) do
  st = posix.stat(path)
  if st and st.type == "directory" then
    status = os.rename(path, path .. ".rpmmoved")
    if not status then
      suffix = 0
      while not status do
        suffix = suffix + 1
        status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
      end
      os.rename(path, path .. ".rpmmoved")
    end
  end
end

%files
%license COPYING.txt
%doc README* TRADEMARK.txt public/local/readme.txt
%{_var}/www/moodle/
%config(noreplace) %{moodlewebdir}/config.php
%attr(-,apache,apache) %{moodledatadir}
%attr(-,apache,apache) %{moodlewebdir}
%config(noreplace) %{_sysconfdir}/cron.d/%{name}
%config(noreplace) %{_sysconfdir}/httpd/conf.d/moodle.conf
%{_unitdir}/%{name}.service
%{_sbindir}/%{name}-cron
%ghost %{moodlewebdir}/lib/adodb
%ghost /var/www/moodle/auth/cas/CAS.rpmmoved
%{_datadir}/php/php-simplepie/moodle_simplepie.php

%changelog
%autochangelog
