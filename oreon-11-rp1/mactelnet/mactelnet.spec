%global source0_hash 1b685568bddfe8d41cf70242a8db98968154334647b2c98c389596604e3fc38a
Name:           mactelnet
Version:        0.6.3
Release:        1%{?dist}
Summary:        MikroTik MAC-Telnet protocol tools
License:        GPL-2.0-or-later
URL:            https://github.com/haakonnessjoen/MAC-Telnet
Source0:        https://github.com/haakonnessjoen/MAC-Telnet/archive/refs/tags/v%{version}/MAC-Telnet-%{version}.tar.gz
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  coreutils
BuildRequires:  gcc
BuildRequires:  gettext-devel
BuildRequires:  libbsd-devel
BuildRequires:  make
BuildRequires:  openssl-devel
# /oreon:deps
%description
Console tools for connecting to, and serving, devices 
using MikroTik RouterOS MAC-Telnet protocol.
(Avoiding packaging mactelnetd for now)

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir MAC-Telnet-%{version}
%oreon_prep
%build

autoreconf -i
%configure --without-mactelnetd --without-config
%make_build
%install
%make_install
%find_lang %{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
