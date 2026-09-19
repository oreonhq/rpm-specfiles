%global source0_hash 215e9e06293e46ca825d6dbc9f57e74180dc928d98d3f24b234086d3face75c2

Name:           nsca-ng
Version:        1.6
Release:        16%{?dist}
Summary:        Add-on for transferring check results (and other commands) to Nagios or Icinga

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://nsca-ng.org
Source:         https://github.com/weiss/nsca-ng/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  make
BuildRequires:  gcc
# Common
BuildRequires:  openssl-devel
BuildRequires:  libev-devel
BuildRequires:  libbsd-devel

%description
%{summary}.

%package client
Summary:        %{SUMMARY} (client)
Conflicts:      nsca-client

%description client
%{summary}.

%package server
Summary:        %{SUMMARY} (server)
BuildRequires:  libconfuse-devel
BuildRequires:  systemd-devel
Requires:       user(nagios)

%description server
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
# Bundled stuff
sed -i -e "/lib\/ev\/libev.m4/d" m4/ev.m4
sed -r -i -e "/lib\/(ev|pidfile)\/Makefile/d" configure.ac
sed -r -i -e "/^MAYBE_(EV|PIDFILE)/d" lib/Makefile.am
rm -vr lib/{pidfile,ev}

%build
autoreconf -vfi
%configure \
  --enable-client \
  --enable-server \
  --with-ev=external \
  %{nil}
%make_build

%install
%make_install
install -Dpm0644 -t %{buildroot}%{_unitdir} etc/nsca-ng.{service,socket}

%check
%make_build check

%files client
%license COPYING
%doc README NEWS PROTOCOL
%{_sbindir}/send_nsca
%{_mandir}/man8/send_nsca.8*
%config(noreplace) %{_sysconfdir}/send_nsca.cfg
%{_mandir}/man5/send_nsca.cfg.5*

%files server
%license COPYING
%doc README NEWS PROTOCOL
%{_unitdir}/nsca-ng.{socket,service}
%{_sbindir}/nsca-ng
%{_mandir}/man8/nsca-ng.8*
%attr(0640,nagios,nagios) %config(noreplace) %{_sysconfdir}/nsca-ng.cfg
%{_mandir}/man5/nsca-ng.cfg.5*

%changelog
%autochangelog
