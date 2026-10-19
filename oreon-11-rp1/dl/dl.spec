%global source0_hash 1a2c4837ce229589423855a4476fc73e67cb314372c58485918e2d7871a3721e
Summary:        Download Ticket Service
URL:        http://www.thregr.org/~wavexx/software/dl/
Name:       dl
Version:    0.19
Release:        1%{?dist}
License:    GPL-2.0-or-later
Source0:        http://www.thregr.org/~wavexx/software/dl/releases/dl-%{version}.zip
Source1:    dl-httpd-conf
Source2:    README.fedora.dl
BuildArch:  noarch
Requires:   php >= 7.0
Requires:   php-mbstring
Requires:   php-openssl
Requires:   php-pdo
Requires:   php-zip
Requires:   sqlite
Requires:   webserver
Requires(post):     policycoreutils-python-utils
Requires(postun):   policycoreutils-python-utils
# oreon:deps

# /oreon:deps
%description
dl is a file exchange service that allows you to upload any file to a web
server and generate a unique ticket for others to download. The ticket is
automatically expired according to the specified rules, so that you don't need
to keep track or cleanup afterward. dl also allows you to grant an anonymous,
one-time upload for others to send *you* a file, without the requirement of
account management.

dl is usually installed as a "email attachments replacement" due to its
simplicity (though can be used in other ways).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

rm -f client/thunderbird-filelink-dl/.gitignore
rm -f htdocs/include/.htaccess
rm -f htdocs/style/include/.htaccess
%install
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/dl
cp -pr htdocs/* ${RPM_BUILD_ROOT}%{_datadir}/dl/.
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/dl
cp -p htdocs/include/config.php.dist ${RPM_BUILD_ROOT}%{_sysconfdir}/dl/config.php
sed -i -e 's:dl.example.com:localhost/dl:g' ${RPM_BUILD_ROOT}%{_sysconfdir}/dl/config.php
ln -sf ../../../../etc/dl/config.php ${RPM_BUILD_ROOT}%{_datadir}/dl/include/config.php
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d
cp -p %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/httpd/conf.d/dl.conf
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/spool/dl
mkdir -p ${RPM_BUILD_ROOT}%{_localstatedir}/spool/dl/data
cp -p %{SOURCE2} ./README.fedora
%oreon_autofiles main

%post

semanage fcontext -a -t httpd_sys_rw_content_t "%{_localstatedir}/spool/dl(/.*)?"
restorecon -R -v %{_localstatedir}/spool/dl > /dev/null
if [ ! -f %{_localstatedir}/spool/dl/data.sdb ]; then
    su -c 'sqlite3 %{_localstatedir}/spool/dl/data.sdb' -s /bin/sh apache < %{_datadir}/dl/include/scripts/db/sqlite.sql
fi
:
%postun

if [ $1 -eq 0 ]; then
    semanage fcontext -d -t httpd_sys_rw_content_t "%{_localstatedir}/spool/dl(/.*)?"
    restorecon -R -v %{_localstatedir}/spool/dl > /dev/null
fi
:
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
