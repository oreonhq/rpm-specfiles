%global source0_hash 382b30416d95b0a5e8502b214810dcac2a56432917e2651447d3abe253e3cc42
%global pypi_name cppheaderparser
Name:           python-%{pypi_name}
Version:        2.7.4
Release:        1%{?dist}
Summary:        Parse C++ header files and generate a data structure
License:        BSD-3-Clause
URL:            http://senexcanis.com/open-source/cppheaderparser/
Source0:        https://files.pythonhosted.org/packages/source/C/CppHeaderParser/CppHeaderParser-%{version}.tar.gz
Patch0:         0001-cppheaderparser-silence-invalid-escape-sequence.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-cppheaderparser = %{version}-%{release}
# /oreon:deps
%description
Parse C++ header files and generate a data structure representing the
class.

%package -n     python3-%{pypi_name}
Summary:        Parse C++ header files and generate a data structure
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
Parse C++ header files and generate a data structure representing the
class.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n CppHeaderParser-%{version}
rm -rf %{pypi_name}.egg-info
# Remove outdated parts (Python 2.x)
rm -rf CppHeaderParser/{examples,docs}
sed -i -e '/^#!\//, 1d' CppHeaderParser/CppHeaderParser.py

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/cppheaderparser* usr/lib64/python3*/site-packages/cppheaderparser* usr/bin/*

%files
%files -n python3-cppheaderparser -f %{oreon_filedir}/python3-cppheaderparser.list

%changelog

%autochangelog
