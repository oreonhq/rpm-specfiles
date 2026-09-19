%global source0_hash 3bba1749aafe1db9b915f00e0dd166cba613b6f788ffd63060ac3485dc9be231

# Created by pyp2rpm-3.3.5
%global pypi_name backrefs

Name:           python-%{pypi_name}
Version:        6.1
Release:        2%{?dist}
Summary:        A wrapper around re and regex that adds additional back references

License:        MIT
URL:            https://github.com/facelessuser/backrefs
Source0:        %{pypi_source %{pypi_name} %{version}}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(regex)
BuildRequires:  python3dist(setuptools)

%description
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. The supported back references actually vary depending
on the regular expression engine being used as the engine may already have
support for some.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name}
Backrefs is a wrapper around Python's built-in Re and the 3rd party Regex
library. Backrefs adds various additional back references (and a couple other
features) that are known to some regular expression engines, but not to
Python's Re and/or Regex. The supported back references actually vary depending
on the regular expression engine being used as the engine may already have
support for some.

%{?python_extras_subpkg:%python_extras_subpkg -n python3-%{pypi_name} -i %{python3_sitelib}/%{pypi_name}-%{version}.dist-info extras}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{pypi_name}

%check
%pyproject_check_import
py.test-3

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE.md
%doc README.md

%changelog
%autochangelog
