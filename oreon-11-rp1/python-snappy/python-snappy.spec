%global source0_hash 40216c1badfb2d38ac781ecb162a1d0ec40f8ee9747e610bcfefdfa79486cee3

%global pypi_name python-snappy

Name:           python-snappy
Version:        0.7.3
Release:        5%{?dist}
Summary:        Python library for the snappy compression library from Google
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://pypi.python.org/pypi/%{pypi_name}
Source0:        %pypi_source

BuildRequires:  gcc-c++
BuildRequires:  snappy-devel
BuildArch:      noarch

%description
Python bindings for the snappy compression library from Google.

%package -n     python3-snappy
Summary:        Python library for the snappy compression library from Google
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-cffi
BuildRequires:  python3-cramjam
BuildRequires:  snappy-devel
Requires:       python3-cffi
Requires:       snappy
# Don't use %%pypi_name here to avoid a python-python-snappy provide

%description -n python3-snappy
Python bindings for the snappy compression library from Google.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn python_snappy-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l snappy

%check
%pyproject_check_import

%files -n python3-snappy -f %{pyproject_files}
%doc README.rst AUTHORS
%license LICENSE

%changelog
%autochangelog
