%global source0_hash 66c44463d81ab21045fd9a1f9815bd165882c2ae90e0863c8872d687056afdbc
%define moddir	%(apxs -q LIBEXECDIR || echo be_happy_mock)
%define svn	20070129svn713
Summary:        NTLM authentication for the Apache web server using winbind daemon
Name: mod_auth_ntlm_winbind
Version: 0.0.0
Release:        1%{?dist}
License: Apache-2.0
URL: http://viewcvs.samba.org/cgi-bin/viewcvs.cgi/trunk/mod_auth_ntlm_winbind/?root=lorikeet
Source0:        %{name}-%{version}-%{svn}.tar.gz
Source1: auth_ntlm_winbind.conf
Requires: httpd >= 2.0.40
Requires: httpd-mmn = %(cat %{_includedir}/httpd/.mmn || echo missing)
Requires: samba-common
Requires(post): shadow-utils
Patch0: mod_auth_ntlm_winbind-20060510-connect_http10.patch
Patch1: mod_auth_ntlm_winbind-20070129-64bit.patch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  httpd-devel
BuildRequires:  make
# /oreon:deps
%description
The %{name} module allows authentication and authorisation over
the Web against a Windows NT/AD domain controllers, using Samba on the same
machine Apache is running on.
It uses "ntlm_auth" helper utility to operate with local winbindd(8) daemon,
which are standard parts of the Samba distribution.

The same way Squid does NTLM authentication now.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n mod_auth_ntlm_winbind
%patch -P0 -p1
%patch -P1 -p1
autoconf

%build

%configure
make
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{moddir}
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
install -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/httpd/conf.d
%oreon_autofiles main

%post

/usr/sbin/usermod -a -G wbpriv apache >/dev/null 2>&1 || :
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
