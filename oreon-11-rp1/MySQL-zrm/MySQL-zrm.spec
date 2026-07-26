%global source0_hash 05e0342b190b6475f220014a126ed213442e24af7b6e3295fa914fcb47b1b931

Name:           MySQL-zrm
Version:        3.0
Release:        46%{?dist}
Summary:        MySQL backup manager

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
URL:            http://www.zmanda.com/backup-mysql.html
Source0:        http://www.zmanda.com/downloads/community/ZRM-MySQL/3.0/Source/MySQL-zrm-%{version}-release.tar.gz
Source1:        MySQL-zrm.service
Source2:        MySQL-zrm.socket
# Really make --quiet quiet
Patch0:         MySQL-zrm-quiet.patch
# Abort if out of space on restore
# https://forums.zmanda.com/showthread.php?5347-mysql-zrm-restore-does-not-check-for-running-out-of-disk-space&p=17076#post17076
Patch1:         MySQL-zrm-tmpwrite.patch
# Enable exclude-pattern with logical backups
# https://forums.zmanda.com/showthread.php?5371-Support-exclude-patter-for-logical-backups-exclude-information_schema
Patch2:         MySQL-zrm-exclude.patch
# Do not fail if mysqldump emits warnings
# https://forums.zmanda.com/showthread.php?5102-How-to-report-bugs
Patch3:         MySQL-zrm-mysqldump-warnings.patch
# Do not use --same-order with -c
# https://bugzilla.redhat.com/show_bug.cgi?id=1458038
Patch4:         MySQL-zrm-taropt.patch
# Check exit status of all commands in pipes
# https://bugzilla.redhat.com/show_bug.cgi?id=1151623
Patch5:         MySQL-zrm-pipestatus.patch
# Remove duplicate command logging
Patch6:         MySQL-zrm-command-log.patch
# Avoid "tar: .: file changed as we read it" by touching the output file first
Patch7:         MySQL-zrm-tar.patch

BuildArch:      noarch
BuildRequires:  perl-generators
BuildRequires:  systemd

Requires:       logrotate
Requires:       /usr/bin/mail
Requires:       perl(DBI)
Requires:       perl(XML::Parser)
Requires:       perl(Data::Report) >= 0.05 
Requires:       perl(Data::Report::Plugin::Html) 
Requires:       perl(Data::Report::Plugin::Text) 
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd

%description
Easy-to-use yet flexible and robust backup and recovery solution for MySQL 
server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c
# Cannot do backups, they get installed
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1
%patch -P6 -p1
%patch -P7 -p1
# FIx permissions
find -name \*.pm -o -name \*.smf | xargs chmod -x
# Fix FSF address
find -type f | xargs sed -i \
  -e 's/59 Temple Place/51 Franklin Street/' -e 's/Suite 330/Fifth Floor/' \
  -e 's/MA  02111-1307/MA  02110-1301/'

%build
# we should use modules from repo
rm -rf usr/lib/mysql-zrm/Data
rm -rf usr/lib/mysql-zrm/XML

# get rid of zero-length files
rm -rf var/log/mysql-zrm/*

%install
mkdir -p %{buildroot}%{perl_vendorlib}
mkdir -p %{buildroot}%{_docdir}
mkdir -p %{buildroot}%{_mandir}/man{1,5}
mkdir -p %{buildroot}%{_sharedstatedir}
mkdir -p %{buildroot}%{_var}/log
mkdir -p %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_sysconfdir}/logrotate.d
mkdir -p %{buildroot}%{_sysconfdir}/mysql-zrm
mkdir -p %{buildroot}%{_unitdir}

# install ourselves in correct locations
cp -rp usr/lib/mysql-zrm/ZRM                    %{buildroot}%{perl_vendorlib}
cp -rp usr/share/doc/%{name}-%{version}         %{buildroot}%{_docdir}/%{name}
cp -rp usr/share/man/man1/*                     %{buildroot}%{_mandir}/man1/
cp -rp usr/share/man/man5/*                     %{buildroot}%{_mandir}/man5/
cp -rp var/lib/*                                %{buildroot}%{_sharedstatedir}
cp -rp var/log/*                                %{buildroot}%{_var}/log/
cp -rp usr/share/mysql-zrm                      %{buildroot}%{_datadir}/
cp -rp usr/bin/*                                %{buildroot}%{_bindir}/
cp -rp etc/mysql-zrm                            %{buildroot}%{_sysconfdir}/
# name logrotate job as package name
cp -rp etc/logrotate.d/mysql-zrm                %{buildroot}%{_sysconfdir}/logrotate.d/%{name}
cp -p %SOURCE1 %SOURCE2                         %{buildroot}%{_unitdir}

# This will store passwords, restrict permissions
chmod 640 %{buildroot}%{_sysconfdir}/mysql-zrm/mysql-zrm.conf

%post
%systemd_post MySQL-zrm.service

%preun
%systemd_preun MySQL-zrm.service

%postun
%systemd_postun_with_restart MySQL-zrm.service

%files
%attr(-,mysql,mysql) %dir %{_var}/log/mysql-zrm
%config(noreplace) %{_sysconfdir}/logrotate.d/%{name}
%config(noreplace) %{_sysconfdir}/mysql-zrm/
%{_sharedstatedir}/mysql-zrm/
%{_datadir}/mysql-zrm/
%attr(0755,root,root) %{_bindir}/*
%{perl_vendorlib}/ZRM
%attr(0644,root,root) %{_unitdir}/*
%{_docdir}/%{name}/
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
%autochangelog
