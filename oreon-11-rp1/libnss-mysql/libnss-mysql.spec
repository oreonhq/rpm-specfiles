%global source0_hash 67ee67857ab549d2769750aecdc804d440517edfd482b5dde2b41a6c9d81ccae

Summary:   NSS library for MySQL
Name:      libnss-mysql
Version:   1.7.1
Release:   3%{?dist}

License:   GPL-2.0-or-later
URL:       https://github.com/saknopper/libnss-mysql
Source0:   https://github.com/saknopper/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:   nsswitch.conf

BuildRequires: mariadb-connector-c-devel
BuildRequires: libtool, autoconf, automake
BuildRequires: make
BuildRequires: authselect, authselect-libs

%description
Store your UNIX user accounts in MySQL. "libnss-mysql" enables the following:

* System-wide authentication and name service using a MySQL database.
  Applications do not need to be MySQL-aware or modified in any way.

* Storing authentication information in a database instead of text files.

* Creation of a single authentication database for multiple servers.
  This is often referred to as the "Single Sign-on" problem.

* Writing data-modification routines (IE self-management web interface).

libnss-mysql is similar to NIS or LDAP. It provides the same centralized
authentication service through a database. What does this mean? Username,
uid, gid, password, etc comes from a MySQL database instead of
/etc/password, /etc/shadow, and /etc/group. A user configured in MySQL will
look and behave just like a user configured in /etc/passwd. Your
applications such as ls, finger, sendmail, qmail, exim, postfix, proftpd,
X, sshd, etc. will all 'see' these users!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
libtoolize -f
autoreconf -f -i
%configure
%make_build
# remove non linux samples
rm -rf sample/freebsd sample/solaris

%install
mkdir -p $RPM_BUILD_ROOT/{etc,lib}
%make_install

# install authselect files
%define authselect_vendor %{_datadir}/authselect/vendor/%{name}
mkdir -p $RPM_BUILD_ROOT%{authselect_vendor}
# Base on minimal or nis profile
if [ -d %{_datadir}/authselect/default/nis ]; then
  cp -ar %{_datadir}/authselect/default/nis/* \
    $RPM_BUILD_ROOT%{authselect_vendor}/
elif [ -d %{_datadir}/authselect/default/minimal ]; then
  cp -ar %{_datadir}/authselect/default/minimal/* \
    $RPM_BUILD_ROOT%{authselect_vendor}/
elif [ -d %{_datadir}/authselect/default/local ]; then
  cp -ar %{_datadir}/authselect/default/local/* \
    $RPM_BUILD_ROOT%{authselect_vendor}/
else
  echo "Missing authselect default profile!"
  exit 1
fi
cp -af %{SOURCE1} $RPM_BUILD_ROOT%{authselect_vendor}/

%ldconfig_scriptlets

%files
%exclude %{_libdir}/libnss_mysql.a
%exclude %{_libdir}/*.so
%{_libdir}/*.so.*
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/libnss-mysql.cfg
%attr(0600,root,root) %config(noreplace) %{_sysconfdir}/libnss-mysql-root.cfg
%doc README ChangeLog AUTHORS THANKS NEWS FAQ DEBUGGING UPGRADING
%doc sample
%license COPYING
%dir %{_datadir}/authselect/vendor/%{name}
%{_datadir}/authselect/vendor/%{name}/*

%changelog
%autochangelog
