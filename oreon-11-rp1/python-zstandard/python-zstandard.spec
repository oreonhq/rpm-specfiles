%if 0%{?rhel}
%bcond_with check
%else
%bcond_without check
%endif

%global pypi_name zstandard

%global desc This project provides Python bindings for interfacing with the Zstandard\
compression library. A C extension and CFFI interface are provided.

Name: python-%{pypi_name}
Version: 0.25.0
Release: 2%{?dist}
Summary: Zstandard bindings for Python
License: (BSD-3-Clause OR GPL-2.0-only) AND MIT
URL: https://github.com/indygreg/python-zstandard
Source0: %{pypi_source}
Patch0: %{name}-py313.patch

%description
%{desc}

%package -n python3-%{pypi_name}
Summary: %{summary}
BuildRequires: gcc
BuildRequires: libzstd-devel
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-xdist)
%endif
# https://github.com/indygreg/python-zstandard/issues/48
Provides: bundled(zstd) = 1.5.7

%description -n python3-%{pypi_name}
%{desc}

%pyproject_extras_subpkg -n python3-%{pypi_name} cffi

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -r %{pypi_name}.egg-info

%generate_buildrequires
%pyproject_buildrequires -x cffi

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -L %{pypi_name}

%check
%pyproject_check_import
%if %{with check}
mv zstandard{,.src}
export ZSTD_SLOW_TESTS=1
%pytest -v\
        --numprocesses=auto
mv zstandard{.src,}
%endif

%files -n python3-%{pypi_name} -f %{pyproject_files}
%license LICENSE zstd/COPYING
%doc README.rst

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.25.0-2
- Prepare for Oreon 11 (RP1)
