%global source0_hash 73122701037c6c3ab953a79fb9accdd79155b3878abc0e4430c5cc6f6c25e41b
%global gh_commit    368f286ce53a13e887daa973fb87333af94dad93
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_owner     yrutschle
%global gh_project   sslh
%global with_tests   0
%define _default_patch_fuzz 3
Name:    sslh
Version: 2.3.1
Release:        1%{?dist}
Summary:        Applicative protocol(SSL/SSH) multiplexer
License: GPL-2.0-only
URL:     https://github.com/%{gh_owner}/%{gh_project}
Source0:        https://github.com/%{gh_owner}/%{name}/archive/%{gh_commit}/%{name}-%{version}-%{gh_short}.tar.gz
Patch0:  00-systemd-tuning.patch
Patch1:  01-remove-lcov-testing.patch
%if 0%{?fedora} >= 28 || 0%{?rhel} > 7 || 0%{?oreon} >= 11
%global use_libwrap 0
%else
%global use_libwrap 1
%endif
%{?systemd_requires}
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Pod::Man)
BuildRequires:  pkgconfig(libcap)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(libpcre)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  systemd
# /oreon:deps
%description
sslh accepts connections on specified ports, and forwards them further
based on tests performed on the first data packet sent by the remote
client.

Probes for HTTP, SSL, SSH, OpenVPN, tinc, XMPP are implemented, and
any other protocol that can be tested using a regular expression, can
be recognized. A typical use case is to allow serving several services
on port 443 (e.g. to connect to ssh from inside a corporate firewall,
which almost never block port 443) while still serving HTTPS on that port.

Hence sslh acts as a protocol multiplexer, or a switchboard. Its name
comes from its original function to serve SSH and HTTPS on the same port.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{gh_commit} -p1

# Create a sysusers.d config file
cat >sslh.sysusers.conf <<EOF
u sslh - 'SSLH daemon' /dev/null -
EOF

%build

./genver.sh >version.h
  make %{?_smp_mflags} USELIBWRAP=1 USELIBCAP=1 USESYSTEMD=1 sslh echosrv
pod2man --section=8 --release=%{version} --center=" " %{name}.pod > %{name}.8
iconv --from=ISO-8859-1 --to=UTF-8 ChangeLog > ChangeLog.conv && \
touch -r ChangeLog ChangeLog.conv && \
mv ChangeLog.conv ChangeLog
%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
mkdir -p %{buildroot}%{_pkgdocdir}
mkdir -p %{buildroot}%{_mandir}/man8
mkdir -p %{buildroot}%{_unitdir}
cp -p %{name}-fork %{buildroot}%{_sbindir}/%{name}
cp -p %{name}-select %{buildroot}%{_sbindir}/%{name}-select
cp -p basic.cfg %{buildroot}/etc/%{name}.cfg
cp -p %{name}.8 %{buildroot}%{_mandir}/man8/
cp -p scripts/systemd.sslh.service %{buildroot}%{_unitdir}/%{name}.service
cat > %{buildroot}%{_sysconfdir}/sysconfig/%{name} << EOF
DAEMON_OPTS="-F/etc/sslh.cfg"
EOF
cat > %{buildroot}%{_unitdir}/%{name}.socket << EOF
[Unit]
Description=Socket support for sslh
Before=sslh.service
[Socket]
FreeBind=true
[Install]
WantedBy=sockets.target
EOF
install -m0644 -D sslh.sysusers.conf %{buildroot}%{_sysusersdir}/sslh.conf
%oreon_autofiles main

%check

%post

%systemd_post sslh.service
%preun

%systemd_preun sslh.service
%postun

%systemd_postun_with_restart sslh.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
