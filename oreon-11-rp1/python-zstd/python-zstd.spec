%global source0_hash 403e5205f4ac04b92e6b0cda654be2f51de268228a0db0067bc087faacf2f495

%global pypi_name zstd

Name:           python-%{pypi_name}
Version:        1.5.7.3
# see also:
# grep "^VERSION = " zstd-*/setup.py
%global zstd_version %(echo %{version} | cut -d. -f1,2,3 --output-delimiter .)

Release:        %autorelease
Summary:        Zstd Bindings for Python

# original zstd bits are GPL-2.0-or-later OR BSD-2-Clause
License:        BSD-2-Clause AND (GPL-2.0-or-later OR BSD-2-Clause)
URL:            https://github.com/sergey-dryabzhinsky/python-zstd
Source:        https://files.pythonhosted.org/packages/source/p/python-zstd/python-zstd-1.5.7.3.tar.gz
# Patches to fix test execution
Patch:          python-zstd-1.5.5.1-test-external.patch

BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
BuildRequires:  pkgconfig(libzstd) >= %{zstd_version}

%description
Simple Python bindings for the Zstd compression library.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
# The library does not do symbol versioning to fully match automatically on
Requires:       libzstd%{?_isa} >= %{zstd_version}

%description -n python3-%{pypi_name}
Simple Python bindings for the Zstd compression library.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
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

%check
%{py3_test_envvars} %{python3} -m unittest -v

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{python3_sitearch}/%{pypi_name}*.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.5.7.3-1
- Prepare for Oreon 11 (RP1)
