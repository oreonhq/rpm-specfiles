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
Source0:        https://files.pythonhosted.org/packages/source/z/zstandard/zstandard-0.25.0.tar.gz
Patch0: %{name}-py313.patch
# oreon url source checksums begin
%global source0_sha256 7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b
%global source0_file zstandard-0.25.0.tar.gz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/zstandard-0.25.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b" || { echo "oreon: Source0 SHA256 mismatch for zstandard-0.25.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
