%global source0_hash 382b30416d95b0a5e8502b214810dcac2a56432917e2651447d3abe253e3cc42

%global pypi_name cppheaderparser

Name:           python-%{pypi_name}
Version:        2.7.4
Release:        23%{?dist}
Summary:        Parse C++ header files and generate a data structure

License:        BSD-3-Clause
URL:            http://senexcanis.com/open-source/cppheaderparser/
Source0:        %{pypi_source CppHeaderParser}
Patch0:         0001-cppheaderparser-silence-invalid-escape-sequence.patch

BuildArch:      noarch

%description
Parse C++ header files and generate a data structure representing the
class.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files CppHeaderParser

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc README.txt README.html

%changelog
%autochangelog
