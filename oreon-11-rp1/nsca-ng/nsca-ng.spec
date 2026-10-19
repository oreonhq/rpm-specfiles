%global source0_hash 215e9e06293e46ca825d6dbc9f57e74180dc928d98d3f24b234086d3face75c2
Name:           nsca-ng
Version:        1.6
Release:        1%{?dist}
Summary:        Add-on for transferring check results (and other commands) to Nagios or Icinga
License:        LicenseRef-Callaway-BSD
URL:            https://nsca-ng.org
Source0:        https://github.com/weiss/nsca-ng/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libbsd-devel
BuildRequires:  libconfuse-devel
BuildRequires:  libev-devel
BuildRequires:  make
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%make_build check
%files -f %{oreon_filedir}/main.list
%files -n nsca-ng-client -f %{oreon_filedir}/nsca-ng-client.list
%files -n nsca-ng-server -f %{oreon_filedir}/nsca-ng-server.list

%changelog

%autochangelog
