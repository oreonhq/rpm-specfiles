%global source0_hash dbcb3fc33f93da7d34542e7cd649f513cbe3cae7ad23f797c97499fc4ccba91e
%global pypi_name columnize
Name:           pycolumnize
Version:        3.11
Release:        1%{?dist}
Summary:        Python module to align in columns a simple list
License:        MIT
URL:            https://github.com/rocky/pycolumnize
Source0:        https://github.com/rocky/%{name}/archive/%{version}/%{pypi_name}-%{version}.tar.gz
Patch0:         pycolumnize-rm-python-mock-usage.diff
BuildArch:      noarch
# oreon:deps
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
A Python module to format a simple (i.e. not nested) list into aligned columns.
A string with embedded newline characters is returned.

%package -n python3-%{pypi_name}
Summary:        Python module to align in columns a simple list
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(pytest)
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
A Python module to format a simple (i.e. not nested) list into aligned columns.
A string with embedded newline characters is returned.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove the dependency on nose
sed -i /nose/d setup.py

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v test_columnize.py
%files -f %{oreon_filedir}/main.list
%files -n python3-columnize -f %{oreon_filedir}/python3-columnize.list

%changelog

%autochangelog
