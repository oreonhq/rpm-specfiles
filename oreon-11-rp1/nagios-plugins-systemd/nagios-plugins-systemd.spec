%global source0_hash 65d84d5a54dc2c951302da4e138bd8c3477306f46e9589ee5457910a2077d0d4
%global nagiospluginsdir %{_libdir}/nagios/plugins
Name:           nagios-plugins-systemd
Version:        5.0.0
Release:        1%{?dist}
Summary:        Nagios Plugin - check_systemd
License:        LGPL-2.1-only
URL:            https://exchange.icinga.com/joseffriedrich/check_systemd
Source0:        https://github.com/Josef-Friedrich/check_systemd/archive/v%{version}/%{name}-%{version}.tar.gz
Requires: nagios-common
%global debug_package %{nil}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(poetry-core) >= 1.0.0
Requires:       python3-nagios-plugins-systemd = %{version}-%{release}
# /oreon:deps
%description
This systemd check for nagios compatible monitoring systems will report a
degraded systemd to your monitoring solution. It can also be used to monitor
individual systemd services and timers units.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n check_systemd-%{version}
# Do not pin test dependencies to exact versions; we cannot respect these!
sed -r -i 's/==/>=/' tox.ini

%build

%pyproject_wheel
%install
%pyproject_install
mkdir -p %{buildroot}/%{nagiospluginsdir}
mv %{buildroot}/%{_bindir}/check_systemd %{buildroot}/%{nagiospluginsdir}
%oreon_autofiles main

%check

PYTHONPATH=%{buildroot}/%{nagiospluginsdir}:${PYTHONPATH} PATH=%{buildroot}/%{nagiospluginsdir}:${PATH} %tox
%files

%changelog

%autochangelog
