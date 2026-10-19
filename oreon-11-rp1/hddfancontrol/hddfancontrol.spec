%global source0_hash d32b53794041579bea27c4398fae3b87fab5c772272818b82ddcf53417b91812
%global pypi_name hddfancontrol
Name:           %{pypi_name}
Version:        2.1.2
Release:        1%{?dist}
Summary:        Control system fan speed by monitoring hard drive temperature
License:        LGPL-3.0-only
URL:            https://github.com/desbma/hddfancontrol
Source0:        https://github.com/desbma/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       hdparm
Requires:       hddtemp
Requires:       python3-docutils
%py_provides    python3-%{pypi_name}
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hddfancontrol = %{version}-%{release}
# /oreon:deps
%description
HDD Fan control is a command line tool to dynamically control fan speed
according to hard drive temperature on Linux.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version} -p1

%build

%pyproject_wheel
%install
%pyproject_install
cp %{buildroot}/%{_bindir}/hddfancontrol %{buildroot}/%{_bindir}/hddfancontrol-3
ln -sf %{_bindir}/hddfancontrol-3 %{buildroot}/%{_bindir}/hddfancontrol-%{python3_version}
rm -rf %{buildroot}%{python3_sitelib}/tests
mkdir -p %{buildroot}%{_unitdir}/
mkdir -p %{buildroot}%{_sysconfdir}/
sed 's,conf.d/hddfancontrol,hddfancontrol.conf,' -i systemd/hddfancontrol.service
cp -a systemd/hddfancontrol.service %{buildroot}%{_unitdir}/
cp -a systemd/hddfancontrol.conf %{buildroot}%{_sysconfdir}/
%oreon_autofiles main

%check

%pyproject_check_import
%py3_test_envvars %{python3} -m unittest -v
%license LICENSE
%doc README.md
%{_bindir}/hddfancontrol
%{_bindir}/hddfancontrol-3
%{_bindir}/hddfancontrol-%{python3_version}
%{_unitdir}/hddfancontrol.service
%config(noreplace) %{_sysconfdir}/hddfancontrol.conf
%files

%changelog

%autochangelog
