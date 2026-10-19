%global source0_hash 7713e1179d162cf5c7906da876ec2ccb9c3a9dcbdffef0cc7f70c3667a205f0b
%bcond_without check
%global pypi_name zstandard
%global desc This project provides Python bindings for interfacing with the Zstandard\
compression library. A C extension and CFFI interface are provided.
Name: python-%{pypi_name}
Version: 0.25.0
Release:        1%{?dist}
Summary:        Zstandard bindings for Python
License: (BSD-3-Clause OR GPL-2.0-only) AND MIT
URL: https://github.com/indygreg/python-zstandard
Source0:        https://files.pythonhosted.org/packages/source/z/zstandard/zstandard-0.25.0.tar.gz
Patch0: %{name}-py313.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi) >= 1.17
BuildRequires:  python3dist(cffi) >= 2.0.0b
BuildRequires:  python3dist(setuptools) >= 77.0.0
Requires:       python3-zstandard = %{version}-%{release}
# /oreon:deps
%package -n       python3-zstandard+cffi
Summary:        Metapackage for python3-zstandard cffi extras
Requires:       python3-zstandard = %{version}-%{release}
Requires:       python3dist(cffi) >= 1.17
Requires:       python3dist(cffi) >= 2.0.0b
Provides:       python3dist(zstandard[cffi]) = %{version}-%{release}

%description -n python3-zstandard+cffi
Metapackage for python3-zstandard cffi extras.

%description
%{desc}

%package -n python3-%{pypi_name}
Summary:        Zstandard bindings for Python
BuildRequires: gcc
BuildRequires: libzstd-devel
BuildRequires: python3-devel
%if %{with check}
BuildRequires: python3dist(pytest)
BuildRequires: python3dist(pytest-xdist)
%endif
Provides: bundled(zstd) = 1.5.7
%description -n python3-%{pypi_name}
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pypi_name}-%{version}
rm -r %{pypi_name}.egg-info

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles main usr/lib/python3*/site-packages/zstandard* usr/lib64/python3*/site-packages/zstandard* usr/bin/*

%check

%pyproject_check_import
%if %{with check}
mv zstandard{,.src}
export ZSTD_SLOW_TESTS=1
%pytest -v\
        --numprocesses=auto
mv zstandard{.src,}
%endif
%files
%files -n python3-zstandard -f %{oreon_filedir}/python3-zstandard.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.25.0-2
- Prepare for Oreon 11 (RP1)
