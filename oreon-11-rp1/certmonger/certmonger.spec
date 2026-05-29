%global source0_hash none

%if 0%{?fedora} > 15 || 0%{?rhel} > 6 || 0%{?oreon}
%global systemd 1
%global	sysvinit 0
%else
%global systemd 0
%global	sysvinit 1
%endif

%if 0%{?fedora} > 15 && 0%{?fedora} < 20 || 0%{?oreon}
%global systemdsysv 1
%else
%global systemdsysv 0
%endif

%if 0%{?fedora} > 14 || 0%{?rhel} > 6 || 0%{?oreon}
%global tmpfiles 1
%else
%global tmpfiles 0
%endif

%if 0%{?fedora} > 9 || 0%{?rhel} > 5 || 0%{?oreon}
%global sysvinitdir %{_initddir}
%else
%global sysvinitdir %{_initrddir}
%endif

%bcond_with xmlrpc

Name:		certmonger
Version:	0.79.21
Release:	4%{?dist}
Summary:	Certificate status monitor and PKI enrollment client

License:	GPL-3.0-or-later
URL:		http://pagure.io/certmonger/
Source0:        http://releases.pagure.org/certmonger/certmonger-0.79.21.tar.gz
#Source1:	http://releases.pagure.org/certmonger/certmonger-%%{version}.tar.gz.sig

Patch0001:	0001-Replace-deprecated-OpenSSL-3.0.0-function-calls.patch
Patch0002:	0002-Add-initial-ML-DSA-support-with-OpenSSL-3.5.0.patch
Patch0003:	0003-Add-initial-ML-DSA-support-with-NSS-3.112.0-4.patch
Patch0004:	0004-Test-for-PQ-support-in-NSS-print-summary-at-end-of-c.patch
Patch0005:	0005-Implement-more-PQ-testing-for-both-NSS-and-OpenSSL.patch
Patch0006:	0006-Allow-requesting-a-ML-DSA-key-using-a-strength.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gcc
BuildRequires:	openldap-devel
BuildRequires:	krb5-devel
BuildRequires:	libidn2-devel
BuildRequires:	dbus-devel, nspr-devel, nss-devel, openssl-devel
%if 0%{?fedora} >= 12 || 0%{?rhel} >= 6 || 0%{?oreon}
BuildRequires:	libuuid-devel
%else
BuildRequires:	e2fsprogs-devel
%endif
BuildRequires:	libtalloc-devel, libtevent-devel
%if 0%{?rhel} >= 6 || 0%{?fedora} >= 9 || 0%{?oreon}
BuildRequires:	libcurl-devel
%else
BuildRequires:	curl-devel
%endif
BuildRequires:	libxml2-devel
%if %{with xmlrpc}
BuildRequires:  xmlrpc-c-devel
%endif
BuildRequires:  jansson-devel
%if 0%{?rhel} && 0%{?rhel} < 6 || 0%{?oreon}
BuildRequires:	bind-libbind-devel
BuildRequires:	mktemp
%endif
# Required for 'make check':
#  for diff and cmp
BuildRequires:	diffutils
#  for expect
BuildRequires:	expect
#  for certutil and pk12util
BuildRequires:	nss-tools
#  for openssl
BuildRequires:	openssl
#  for dbus-launch
BuildRequires:	/usr/bin/dbus-launch
#  for dos2unix
BuildRequires:	/usr/bin/dos2unix
BuildRequires:	/usr/bin/unix2dos
#  for which
BuildRequires:	/usr/bin/which
#  for dbus tests
BuildRequires:	python3-dbus
BuildRequires:	popt-devel

# we need a running system bus
Requires:	dbus
Requires(post):	%{_bindir}/dbus-send

%if %{systemd}
BuildRequires:	systemd-units
BuildRequires: make
Requires(post):	systemd-units
Requires(preun):	systemd-units, dbus, sed
Requires(postun):	systemd-units
%endif

%if %{systemdsysv}
Requires(post):	systemd-sysv
%global systemdsysvsave \
# Save the current service runlevel info, in case the user wants \
# to apply the enabled status manually later, by running \
#   "systemd-sysv-convert --apply certmonger". \
%{_bindir}/systemd-sysv-convert --save certmonger >/dev/null 2>&1 ||:
%else
%global systemdsysvsave %{nil}
%endif

%if %{sysvinit}
Requires(post):	/sbin/chkconfig, /sbin/service
Requires(preun):	/sbin/chkconfig, /sbin/service, dbus, sed
%endif

%if 0%{?fedora} >= 15 || 0%{?oreon}
# Certain versions of libtevent have incorrect internal ABI versions.
Conflicts: libtevent < 0.9.13
%endif

%description
Certmonger is a service which is primarily concerned with getting your
system enrolled with a certificate authority (CA) and keeping it enrolled.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1

%if 0%{?rhel} > 0 || 0%{?oreon}
# Enabled by default for RHEL for bug #765600, still disabled by default for
# Fedora pending a similar bug report there.
sed -i 's,^# chkconfig: - ,# chkconfig: 345 ,g' sysvinit/certmonger.in
%endif

%build
autoreconf -i -f
%configure \
%if %{systemd}
	--enable-systemd \
%endif
%if %{sysvinit}
	--enable-sysvinit=%{sysvinitdir} \
%endif
%if %{tmpfiles}
	--enable-tmpfiles \
%endif
	--with-homedir=/run/certmonger \
%if %{with xmlrpc}
    --with-xmlrpc \
%endif
	--disable-dsa \
	--with-tmpdir=/run/certmonger --enable-pie --enable-now
%if %{with xmlrpc}
# For some reason, some versions of xmlrpc-c-config in Fedora and RHEL just
# tell us about libxmlrpc_client, but we need more.  Work around.
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

%check
make check

%post
if test $1 -eq 1 ; then
	%{_bindir}/dbus-send --system --type=method_call --dest=org.freedesktop.DBus / org.freedesktop.DBus.ReloadConfig 2>&1 || :
fi
%if %{without xmlrpc}
# remove any existing certmaster CA configuration
if test $1 -gt 1 ; then
    %{_bindir}/getcert remove-ca -c certmaster 2>&1 || :
fi
%endif
%if %{systemd}
if test $1 -eq 1 ; then
	/bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif
%if %{sysvinit}
/sbin/chkconfig --add certmonger
%endif

%triggerin -- certmonger < 0.58
if test $1 -gt 1 ; then
	# If the daemon is running, remove knowledge of the dogtag renewer.
	objpath=`dbus-send --system --reply-timeout=10000 --dest=org.fedorahosted.certmonger --print-reply=o /org/fedorahosted/certmonger org.fedorahosted.certmonger.find_ca_by_nickname string:dogtag-ipa-renew-agent 2> /dev/null | sed -r 's,^ +,,g' || true`
	if test -n "$objpath" ; then
		dbus-send --system --dest=org.fedorahosted.certmonger --print-reply /org/fedorahosted/certmonger org.fedorahosted.certmonger.remove_known_ca objpath:"$objpath" >/dev/null 2> /dev/null
	fi
	# Remove the data file, in case it isn't running.
	for cafile in %{_localstatedir}/lib/certmonger/cas/* ; do
		if grep -q '^id=dogtag-ipa-renew-agent$' "$cafile" ; then
			rm -f "$cafile"
		fi
	done
fi
exit 0

%postun
%if %{systemd}
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ] ; then
	/bin/systemctl try-restart certmonger.service >/dev/null 2>&1 || :
fi
%endif
%if %{sysvinit}
if test $1 -gt 0 ; then
	/sbin/service certmonger condrestart 2>&1 > /dev/null
fi
%endif
exit 0

%preun
%if %{systemd}
if test $1 -eq 0 ; then
	/bin/systemctl --no-reload disable certmonger.service > /dev/null 2>&1 || :
	/bin/systemctl stop certmonger.service > /dev/null 2>&1 || :
fi
%endif
%if %{sysvinit}
if test $1 -eq 0 ; then
	/sbin/service certmonger stop 2>&1 > /dev/null
	/sbin/chkconfig --del certmonger
fi
%endif
exit 0

%if %{systemd}
%triggerun -- certmonger < 0.43
%{systemdsysvsave}
# Do this because the old package's %%postun doesn't know we need to do it.
/sbin/chkconfig --del certmonger >/dev/null 2>&1 || :
# Do this because the old package's %%postun wouldn't have tried.
/bin/systemctl try-restart certmonger.service >/dev/null 2>&1 || :
exit 0
%endif

%files -f %{name}.lang
%doc README.md LICENSE STATUS doc/*.txt
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/*
%{_datadir}/dbus-1/services/*
%dir %{_sysconfdir}/certmonger
%config(noreplace) %{_sysconfdir}/certmonger/certmonger.conf
%dir /run/certmonger
%{_bindir}/*
%{_sbindir}/certmonger
%{_mandir}/man*/*
%{_libexecdir}/%{name}
%{_localstatedir}/lib/certmonger
%if %{sysvinit}
%{sysvinitdir}/certmonger
%endif
%if %{tmpfiles}
%attr(0644,root,root) %config(noreplace) %{_tmpfilesdir}/certmonger.conf
%endif
%if %{systemd}
%{_unitdir}/*
%{_datadir}/dbus-1/system-services/*
%endif

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.79.21-4
- Import
