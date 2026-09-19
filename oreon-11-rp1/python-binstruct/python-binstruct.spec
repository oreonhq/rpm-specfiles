%global source0_hash 6238b637c18e5889a1977d0c9c72b14cc3ca56b4ab7f0e9d4c40cad5bfbdd056

%global pypi_name binstruct
%global global_desc %{expand:
The binstruct library allows you to access binary data using a
predefined structure.  The binary data can be provided in any form
that allows an indexed access to single bytes.  This could for example
be a memory-mapped file.  The data structure itself is defined in way
similar to Django database table definitions by declaring a new class
with its fields.}

Name:           python-%{pypi_name}
Version:        1.0.1
Release:        37%{?dist}
Summary:        Library for read/write access of binary data via structures

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %{pypi_source %{pypi_name} %{version} zip}

# Drop nose.
Patch0:         binstruct-1.0.1-pytest.patch

BuildArch:      noarch

BuildRequires:  dos2unix
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)

%description
%{global_desc}

%package -n python3-%{pypi_name}
Summary:        Library for read/write access of binary data via structures

%description -n python3-%{pypi_name}
%{global_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1 -n %{pypi_name}-%{version}
rm -rf *.egg-info
find . -type f -print0 |          \
  xargs -0 dos2unix -ascii -k -s

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}

%check
%pyproject_check_import
%pytest

%files -n python3-%{pypi_name} -f %{pyproject_files}
%doc PKG-INFO README.rst

%changelog
%autochangelog
