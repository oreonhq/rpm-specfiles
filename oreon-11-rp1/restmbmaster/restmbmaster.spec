%global source0_hash 74c997e6c820ba885e4aefa70af84b4a3e42dc5e79cec0a5e3105283c31adcc3
Name: restmbmaster
Version: 5
Release:        1%{?dist}
Summary:        Rest API gateway to Modbus slaves
License: GPL-2.0-or-later
URL: https://github.com/jpirko/%{name}/
Source0:        https://github.com/jpirko/%{name}/raw/files/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libmicrohttpd-devel
BuildRequires:  libmodbus-devel
BuildRequires:  make
BuildRequires:  systemd
# /oreon:deps
%description
This package contains a tool called %{name} which
is a simple daemon that allows user to access Modbus slaves
over Rest API. The slaves could be either connected over
serial line (Modbus RTU protocol), or over TCP (Modbus TCP protocol).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
%{make_build}
%install
%{make_install}
mkdir -p %{buildroot}%{_unitdir}
install -p systemd/%{name}@.service %{buildroot}%{_unitdir}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
