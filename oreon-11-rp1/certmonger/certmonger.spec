%global source0_hash 4674649d087496bb2868f0b4c5859a62e39fc4e31cec5795a76f41530cdc5196
%if 0%{?fedora} > 15 || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global systemd 1
%global	sysvinit 0
%else
%global systemd 0
%global	sysvinit 1
%endif
%if 0%{?fedora} > 15 && 0%{?fedora} < 20 || (0%{?oreon} >= 11)
%global systemdsysv 1
%else
%global systemdsysv 0
%endif
%if 0%{?fedora} > 14 || 0%{?rhel} > 6 || (0%{?oreon} >= 11)
%global tmpfiles 1
%else
%global tmpfiles 0
%endif
%if 0%{?fedora} > 9 || 0%{?rhel} > 5 || (0%{?oreon} >= 11)
%global sysvinitdir %{_initddir}
%else
%global sysvinitdir %{_initrddir}
%endif
%bcond_with xmlrpc
Name:		certmonger
Version:	0.79.21
Release:        4%{?dist}
Summary:        Certificate status monitor and PKI enrollment client
License:	GPL-3.0-or-later
URL:		http://pagure.io/certmonger/
Source0:        https://deb.debian.org/debian/pool/main/c/certmonger/certmonger_%{version}.orig.tar.gz#/certmonger-%{version}.tar.gz
Patch0001:	0001-Replace-deprecated-OpenSSL-3.0.0-function-calls.patch
Patch0002:	0002-Add-initial-ML-DSA-support-with-OpenSSL-3.5.0.patch
Patch0003:	0003-Add-initial-ML-DSA-support-with-NSS-3.112.0-4.patch
Patch0004:	0004-Test-for-PQ-support-in-NSS-print-summary-at-end-of-c.patch
Patch0005:	0005-Implement-more-PQ-testing-for-both-NSS-and-OpenSSL.patch
Patch0006:	0006-Allow-requesting-a-ML-DSA-key-using-a-strength.patch
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6 || (0%{?oreon} >= 11)
%else
%endif
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 9 || (0%{?oreon} >= 11)
%else
%endif
%if %{with xmlrpc}
%endif
%if 0%{?rhel} && 0%{?rhel} < 6 || (0%{?oreon} >= 11)
%endif
Requires:	dbus
Requires(post):	%{_bindir}/dbus-send
%global systemdsysvsave %{nil}
Requires(post):	/sbin/chkconfig, /sbin/service
Requires(preun):	/sbin/chkconfig, /sbin/service, dbus, sed
%if 0%{?fedora} >= 15 || (0%{?oreon} >= 11)
Conflicts: libtevent < 0.9.13
%endif
# oreon:deps
BuildRequires:  /usr/bin/dbus-launch
BuildRequires:  /usr/bin/dos2unix
BuildRequires:  /usr/bin/unix2dos
BuildRequires:  /usr/bin/which
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  dbus-devel
BuildRequires:  diffutils
BuildRequires:  expect
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  jansson-devel
BuildRequires:  krb5-devel
BuildRequires:  libcurl-devel
BuildRequires:  libidn2-devel
BuildRequires:  libtalloc-devel
BuildRequires:  libtevent-devel
BuildRequires:  libuuid-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  nspr-devel
BuildRequires:  nss-devel
BuildRequires:  nss-tools
BuildRequires:  openldap-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  popt-devel
BuildRequires:  python3-dbus
BuildRequires:  systemd-units
# /oreon:deps
%description
Certmonger is a service which is primarily concerned with getting your
system enrolled with a certificate authority (CA) and keeping it enrolled.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%if 0%{?rhel} > 0 || (0%{?oreon} >= 11)
# Enabled by default for RHEL for bug #765600, still disabled by default for
# Fedora pending a similar bug report there.
sed -i 's,^# chkconfig: - ,# chkconfig: 345 ,g' sysvinit/certmonger.in
%endif

%build

autoreconf -i -f
%configure \
	--enable-sysvinit=%{sysvinitdir} \
	--with-homedir=/run/certmonger \
%if %{with xmlrpc}
    --with-xmlrpc \
%endif
	--disable-dsa \
	--with-tmpdir=/run/certmonger --enable-pie --enable-now
%if %{with xmlrpc}
make %{?_smp_mflags} XMLRPC_LIBS="-lxmlrpc_client -lxmlrpc_util -lxmlrpc"
%else
make %{?_smp_mflags}
%endif
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/certmonger/{cas,requests}
install -m755 -d $RPM_BUILD_ROOT/run/certmonger
%{find_lang} %{name}
%oreon_autofiles main

%check

make check
%post

if test $1 -eq 1 ; then
	%{_bindir}/dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig 2>&1 || :
fi
%if %{without xmlrpc}
if test $1 -gt 1 ; then
    %{_bindir}/getcert remove-ca -c certmaster 2>&1 || :
fi
%endif
/sbin/chkconfig --add certmonger
%triggerin -- certmonger < 0.58

if test $1 -gt 1 ; then
	objpath=`dbus-send --system --reply-timeout=10000 --dest=org.fedorahosted.certmonger --print-reply=o /org/fedorahosted/certmonger org.fedorahosted.certmonger.find_ca_by_nickname string:dogtag-ipa-renew-agent 2> /dev/null | sed -r 's,^ +,,g' || true`
	if test -n "$objpath" ; then
		dbus-send --system --dest=org.fedorahosted.certmonger --print-reply /org/fedorahosted/certmonger org.fedorahosted.certmonger.remove_known_ca objpath:"$objpath" >/dev/null 2> /dev/null
	fi
	for cafile in %{_localstatedir}/lib/certmonger/cas/* ; do
		if grep -q '^id=dogtag-ipa-renew-agent$' "$cafile" ; then
			rm -f "$cafile"
		fi
	done
fi
exit 0
%postun

if test $1 -gt 0 ; then
	/sbin/service certmonger condrestart 2>&1 > /dev/null
fi
exit 0
%preun

if test $1 -eq 0 ; then
	/sbin/service certmonger stop 2>&1 > /dev/null
	/sbin/chkconfig --del certmonger
fi
exit 0
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.79.21-4
- Import
