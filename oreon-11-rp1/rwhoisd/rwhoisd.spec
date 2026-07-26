%global source0_hash 66793f02bc9370914ca3f579409e8f79b6a394b8a981168ead7b1a6654a83a2a

# Disable TCP Wrappers connection filter
%bcond_with rwhoisd_enables_tcpwrappers

Name:       rwhoisd 
Version:    1.5.9.6
Release:    38%{?dist}
Summary:    ARIN's Referral WHOIS server
# common/strerror.c:                GPL-2.0-or-later (libiberty)
# LICENSE:                          GPL-2.0 text
# mkdb/metaphon.c:                  LicenseRef-Fedora-Public-Domain
# mkdb/y.tab.c:                     GPL-2.0-or-later WITH Bison-exception-1.24
# regexp/COPYRIGHT:                 Spencer-86
## Not in any binary package
# configure:                        FSFUL
## Unbundled
# tools/tcpd_wrapper/DISCLAIMER:    TCP-wrappers
# tools/tcpd_wrapper/strcasecmp.c:  BSD-4.3TAHOE
License:    GPL-2.0-or-later AND GPL-2.0-or-later WITH Bison-exception-1.24 AND Spencer-86 AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND FSFUL AND TCP-wrappers AND BSD-4.3TAHOE
URL:        https://projects.arin.net/rwhois/
Source0:    %{url}ftp/%{name}-%{version}.tar.gz
Source1:    %{name}.service
# Install database to /var
Patch0:     %{name}-1.5.9.6-Install-database-to-var.patch
# Fix configure script
Patch1:     %{name}-1.5.9.5-Use-configure-options-instead-of-GCC-test.patch
# Fix configure script
Patch2:     %{name}-1.5.9.5-Use-AC_SYS_LARGEFILE-for-large-file-support-check.patch
# Fix configure script
Patch3:     %{name}-1.5.9.5-Respect-without-local-libwrap.patch
# Use system tcpd.h
Patch4:     %{name}-1.5.9.5-Do-not-include-bundled-tcpd.h.patch
# GNU sort requires new syntax
Patch5:     %{name}-1.5.9.5-Select-which-way-to-call-sort.patch
# Change default configuration
Patch6:     %{name}-1.5.9.5-Adjust-sample-configuration.patch
# Disable TCP wrappers, bug #1518781
Patch7:     %{name}-1.5.9.6-Allow-disabling-TCP-wrappers.patch
# Fix building with GCC 13, proposed to na upstream,
# <https://github.com/arineng/rwhoisd/pull/2>
Patch8:     %{name}-1.5.9.6-c99.patch
# Fix a signal handler return value, proposed to an upstream,
# <https://github.com/arineng/rwhoisd/pull/3>
Patch9:     %{name}-1.5.9.6-Fix-a-return-value-of-signal-handlers.patch
# Fix building with GCC 15, bug #2341316, proposed upstream
# <https://github.com/arineng/rwhoisd/pull/5>
Patch10:    %{name}-1.5.9.6-Adapt-to-ISO-C23.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libxcrypt-devel
%if %{with rwhoisd_enables_tcpwrappers}
BuildRequires:  tcp_wrappers-devel
%endif
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# cat executed by rwhois_repack
Requires:       %{_bindir}/cat
# sort executed by rwhois_indexer
Requires:       %{_bindir}/sort
%{?systemd_requires}
%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
Requires(pre):  shadow-utils
%endif

%description
This server is a reference implementation of the server side of the RWhois
protocol, first described in RFC 1714.  This server attempts to implement
concepts and practices in accordance with version 1.5 of the protocol,
described in RFC 2167.

%package example
License:    GPL-2.0-or-later
Summary:    Sample data for %{name} WHOIS server
BuildArch:  noarch
Requires:   %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description example
This package delivers example configuration and data for %{name} WHOIS server.
Recommended how-to is <http://www.unixadmin.cc/rwhois/>.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# Remove bundled tcp_wrappers for sure
find tools/tcpd_wrapper -depth -mindepth 1 \! -name Makefile.in -delete
# Keep System V8 regexp library
# TODO: port to GNU glibc
autoreconf

# Create a sysusers.d config file
cat >sysusers.conf <<EOF
u rwhoisd - 'rwhoisd daemon' %{_localstatedir}/%{name} -
EOF

%build
%global _hardened_build 1
%configure \
    --disable-gcc-debug \
    --disable-gprof \
    --enable-ipv6 \
    --enable-largefile \
    --enable-newsort \
    --enable-syslock \
%if %{with rwhoisd_enables_tcpwrappers}
    --enable-tcpwrappers \
%else
    --disable-tcpwrappers \
%endif
    --enable-warnings \
    --without-local-libwrap

# Does not support parallel build
make

%install
%{make_install}
install -d '%{buildroot}%{_mandir}/man8'
install -m 0644 -t '%{buildroot}%{_mandir}/man8' doc/*.8
install -d '%{buildroot}%{_unitdir}'
install -m 0644 -t '%{buildroot}%{_unitdir}' '%{SOURCE1}'
# Default empty configuration
install -d '%{buildroot}%{_sysconfdir}'
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.conf
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.x.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.root
install -m 0644 -t '%{buildroot}%{_localstatedir}/%{name}/' \
    sample.data/rwhoisd.auth_area
install -d -m 0775 "%{buildroot}%{_localstatedir}/%{name}/register-spool"
install -m0644 -D sysusers.conf %{buildroot}%{_sysusersdir}/%{name}.conf

%if (0%{?fedora} && 0%{?fedora} < 42) || (0%{?rhel} && 0%{?rhel} < 11)
%pre
getent group %{name} >/dev/null || groupadd -r %{name}
getent passwd %{name} >/dev/null || \
    useradd -r -g %{name} -d %{_localstatedir}/%{name} -s /sbin/nologin \
    -c "rwhoisd daemon" %{name}
exit 0
%endif

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service 

%files
%license LICENSE regexp/COPYRIGHT
%doc doc/operations_guide.txt doc/security.txt doc/TODO doc/UPGRADE README
%{_bindir}/rwhois_deleter
%{_bindir}/rwhois_indexer
%{_bindir}/rwhois_repack
%{_sbindir}/rwhoisd
%{_mandir}/man8/rwhois_indexer.*
%{_mandir}/man8/rwhoisd.*
%{_unitdir}/%{name}.service
%config(noreplace) %{_sysconfdir}/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}.dir
%config(noreplace) %{_sysconfdir}/%{name}.x.dir
%config(noreplace) %{_sysconfdir}/%{name}.root
%dir %{_localstatedir}/%{name}
%config(noreplace) %{_localstatedir}/%{name}/%{name}.auth_area
%attr(775,root,rwhoisd) %dir %{_localstatedir}/%{name}/register-spool
%{_sysusersdir}/%{name}.conf

%files example
%{_localstatedir}/%{name}/samples

%changelog
%autochangelog
