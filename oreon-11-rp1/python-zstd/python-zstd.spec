%global source0_hash 403e5205f4ac04b92e6b0cda654be2f51de268228a0db0067bc087faacf2f495
%global pypi_name zstd
Name:           python-%{pypi_name}
Version:        1.5.7.3
%global zstd_version %(echo %{version} | cut -d. -f1,2,3 --output-delimiter .)
Release:        1%{?dist}
Summary:        Zstd Bindings for Python
License:        BSD-2-Clause AND (GPL-2.0-or-later OR BSD-2-Clause)
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source0:        https://files.pythonhosted.org/packages/source/p/python-zstd/python-zstd-1.5.7.3.tar.gz
Patch:          python-zstd-1.5.5.1-test-external.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
Simple Python bindings for the Zstd compression library.

%package -n     python3-%{pypi_name}
Summary:        Zstd Bindings for Python
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       libzstd%{?_isa} >= %{zstd_version}
%description -n python3-%{pypi_name}
Simple Python bindings for the Zstd compression library.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf src/%{pypi_name}.egg-info
# Remove precompiled files
find . -name '*.pyc' -delete
# Remove bundled zstd library
rm -rf zstd/
# do not test the version matching, we don't really need exact version of
# zstd here
rm tests/test_version.py
sed -i -e '/tests\.test_version/d' setup.py
sed -i -e '/test_version/d' tests/__init__.py

%build

%py3_build -- --legacy --external
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%{py3_test_envvars} %{python3} -m unittest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-zstd -f %{oreon_filedir}/python3-zstd.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.7.3-1
- Prepare for Oreon 11 (RP1)
