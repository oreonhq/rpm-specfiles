%global source0_hash 65d84d5a54dc2c951302da4e138bd8c3477306f46e9589ee5457910a2077d0d4

%global nagiospluginsdir %{_libdir}/nagios/plugins
Name:           nagios-plugins-systemd
Version:        5.0.0
Release:        %autorelease
Summary:        Nagios Plugin - check_systemd

License:        LGPL-2.1-only
URL:            https://exchange.icinga.com/joseffriedrich/check_systemd
Source:         https://github.com/Josef-Friedrich/check_systemd/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  python3-devel

# Require the package that owns the plugins dir, as we install the plugin there.
Requires: nagios-common

# The package does not contain any architecture-dependent things, but installs
# into an arch-dependend directory. Thus, it cannot be noarch, but it does not
# provide any debuginfo.
%global debug_package %{nil}

%description
This systemd check for nagios compatible monitoring systems will report a
degraded systemd to your monitoring solution. It can also be used to monitor
individual systemd services and timers units.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n check_systemd-%{version}
# Do not pin test dependencies to exact versions; we cannot respect these!
sed -r -i 's/==/>=/' tox.ini

%generate_buildrequires
%pyproject_buildrequires -t

%build
%pyproject_wheel

%install
%pyproject_install

%pyproject_save_files check_systemd

# The nagios plugin binaries must be in the nagiospluginsdir.
mkdir -p %{buildroot}/%{nagiospluginsdir}
mv %{buildroot}/%{_bindir}/check_systemd %{buildroot}/%{nagiospluginsdir}

%check
PYTHONPATH=%{buildroot}/%{nagiospluginsdir}:${PYTHONPATH} PATH=%{buildroot}/%{nagiospluginsdir}:${PATH} %tox

%files -f %{pyproject_files}
%doc README.*
%license LICENSE
%{nagiospluginsdir}/check_systemd

%changelog
%autochangelog
