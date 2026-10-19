%global source0_hash cd47d3d9a72579b470dd73d85cd3fec606fa5659c728ff3c1c57e970f4da72a2
Name:               conman
Version:            0.3.1
Release:        1%{?dist}
Summary:        ConMan - The Console Manager
License:            GPL-3.0-or-later AND ISC
URL:                https://dun.github.io/conman/
Source0:        https://github.com/dun/%{name}/archive/%{name}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires:           logrotate
Requires(post):     systemd
Requires(preun):    systemd
Requires(postun):   systemd
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  freeipmi-devel
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  systemd
# /oreon:deps
%description
ConMan is a serial console management program designed to support a large
number of console devices and simultaneous users.  It currently supports
local serial devices and remote terminal servers (via the telnet protocol).
Its features include:

  - mapping symbolic names to console devices
  - logging all output from a console device to file
  - supporting monitor (R/O), interactive (R/W), and
    broadcast (W/O) modes of console access
  - allowing clients to join or steal console "write" privileges
  - executing Expect scripts across multiple consoles in parallel

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

sh ./bootstrap

%build

%configure
%make_build
%install
%make_install
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}.old
%oreon_autofiles main

%post

%systemd_post conman.service
%preun

%systemd_preun conman.service
%postun

%systemd_postun_with_restart conman.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
