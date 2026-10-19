%global source0_hash 44d45d7d8344290c259c989d3af3f614c7837cbd85052d486adfa46a1c777164
%global gitver 0
%if 0%{?gitver}
%global  commit      f0a089a12dca9e2fd9543c8e8086ac70f7058513
%global  date        .20210630git
%global  shortcommit %(c=%{commit}; echo ${c:0:8})
%else
%global  commit      %{nil}
%global  date        %{nil}
%global  shortcommit %{nil}
%endif
Name: python-dmidecode
Summary:        Python module to access DMI data
Version: 3.12.3
Release:        16%{?dist}
License: GPL-2.0-only
URL: https://github.com/nima/python-dmidecode
Source0:        https://github.com/nima/python-dmidecode/archive/refs/tags/v3.12.3.tar.gz#/python-dmidecode-3.12.3.tar.gz
Patch0: python-dmidecode-rhbz2154949.patch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-dmidecode = %{version}-%{release}
# /oreon:deps
%description

%package -n python3-dmidecode
Summary: Python 3 module to access DMI data
Requires: libxml2-python3
%description -n python3-dmidecode

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{version} -N
%patch 0 -p1 -b .backup
# upstream Makefile calls src/setup.py which imports src/setup_common.py
# we need the setup.py file in PWD to make the setuptools build backend see it
mv src/setup*.py .

%build

export PYTHON_BIN=%{__python3}
export CFLAGS="%{build_cflags} -std=gnu89"
export CXXFLAGS="%{build_cxxflags} -std=gnu89"
export CC=gcc
export CXX=g++
%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-dmidecode usr/lib/python3*/site-packages/dmidecode* usr/lib64/python3*/site-packages/dmidecode* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/dmidecode* usr/lib64/python3*/site-packages/dmidecode* usr/bin/*

%check

%pyproject_check_import
export PYTHONPATH=%{buildroot}%{python3_sitearch}
export PYTHON_BIN=%{__python3}
make -C unit-tests
%files
%files -n python3-dmidecode -f %{oreon_filedir}/python3-dmidecode.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.12.3-16
- Import
