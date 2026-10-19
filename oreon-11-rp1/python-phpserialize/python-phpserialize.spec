%global source0_hash bf672d312d203d09a84c26366fab8f438a3ffb355c407e69974b7ef2d39a0fa7
%global pypi_name phpserialize
Name:           python-%{pypi_name}
Version:        1.3
Release:        28%{?dist}
Summary:        A port of the serialize and unserialize functions of php to python
License:        LicenseRef-Callaway-BSD
URL:            http://github.com/mitsuhiko/phpserialize
Source0:        https://files.pythonhosted.org/packages/source/p/python-phpserialize/python-phpserialize-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
phpserialize a port of the serialize and unserialize functions of php to
python. This module implements the python serialization interface (eg: provides
dumps, loads and similar functions).

%package -n     python3-%{pypi_name}
Summary:        A port of the serialize and unserialize functions of php to python
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
phpserialize a port of the serialize and unserialize functions of php to
python. This module implements the python serialization interface (eg: provides
dumps, loads and similar functions).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%files -f %{oreon_filedir}/main.list
%files -n python3-phpserialize -f %{oreon_filedir}/python3-phpserialize.list

%changelog

%autochangelog
