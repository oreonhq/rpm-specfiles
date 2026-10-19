%global source0_hash 66793f02bc9370914ca3f579409e8f79b6a394b8a981168ead7b1a6654a83a2a
%bcond_with rwhoisd_enables_tcpwrappers
Name:       rwhoisd 
Version:    1.5.9.6
Release:        1%{?dist}
Summary:        ARIN's Referral WHOIS server
License:    GPL-2.0-or-later AND GPL-2.0-or-later WITH Bison-exception-1.24 AND Spencer-86 AND LicenseRef-Fedora-Public-Domain
SourceLicense:  %{license} AND FSFUL AND TCP-wrappers AND BSD-4.3TAHOE
URL:        https://projects.arin.net/rwhois/
Source0:        https://projects.arin.net/rwhois/ftp/%{name}-%{version}.tar.gz
Source1:    %{name}.service
Patch0:     %{name}-1.5.9.6-Install-database-to-var.patch
Patch1:     %{name}-1.5.9.5-Use-configure-options-instead-of-GCC-test.patch
Patch2:     %{name}-1.5.9.5-Use-AC_SYS_LARGEFILE-for-large-file-support-check.patch
Patch3:     %{name}-1.5.9.5-Respect-without-local-libwrap.patch
Patch4:     %{name}-1.5.9.5-Do-not-include-bundled-tcpd.h.patch
Patch5:     %{name}-1.5.9.5-Select-which-way-to-call-sort.patch
Patch6:     %{name}-1.5.9.5-Adjust-sample-configuration.patch
Patch7:     %{name}-1.5.9.6-Allow-disabling-TCP-wrappers.patch
Patch8:     %{name}-1.5.9.6-c99.patch
Patch9:     %{name}-1.5.9.6-Fix-a-return-value-of-signal-handlers.patch
Patch10:    %{name}-1.5.9.6-Adapt-to-ISO-C23.patch
%if %{with rwhoisd_enables_tcpwrappers}
%endif
Requires:       %{_bindir}/cat
Requires:       %{_bindir}/sort
%{?systemd_requires}
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
# /oreon:deps
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
make
%install
%{make_install}
install -d '%{buildroot}%{_mandir}/man8'
install -m 0644 -t '%{buildroot}%{_mandir}/man8' doc/*.8
install -d '%{buildroot}%{_unitdir}'
install -m 0644 -t '%{buildroot}%{_unitdir}' '%{SOURCE1}'
install -d '%{buildroot}%{_sysconfdir}'
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.conf
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.x.dir
install -m 0644 -t '%{buildroot}%{_sysconfdir}' sample.data/rwhoisd.root
install -m 0644 -t '%{buildroot}%{_localstatedir}/%{name}/' \
    sample.data/rwhoisd.auth_area
install -d -m 0775 "%{buildroot}%{_localstatedir}/%{name}/register-spool"
install -m0644 -D sysusers.conf %{buildroot}%{_sysusersdir}/%{name}.conf
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%post

%systemd_post %{name}.service
%preun

%systemd_preun %{name}.service
%postun

%systemd_postun_with_restart %{name}.service 
%files -f %{oreon_filedir}/main.list
%files -n rwhoisd-example -f %{oreon_filedir}/rwhoisd-example.list

%changelog

%autochangelog
