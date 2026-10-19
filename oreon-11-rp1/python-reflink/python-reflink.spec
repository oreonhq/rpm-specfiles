%global source0_hash 882375ee7319275ae5f6a6a1287406365dac1e9643b91ad10e5187d3f84253bd
%global pypi_name reflink
%global pypi_version 0.2.2
Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        1%{?dist}
Summary:        Python wrapper around the reflink system calls
License:        MIT
URL:            https://gitlab.com/rubdos/pyreflink
Source0:        https://files.pythonhosted.org/packages/source/p/python-reflink/python-reflink-%{version}.tar.gz
Patch:          reflink-0.2.2-no-pytest-runner.patch
# oreon:deps
BuildRequires:  btrfs-progs
BuildRequires:  gcc
BuildRequires:  python3-devel
BuildRequires:  python3dist(cffi)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
# /oreon:deps
%description
Python wrapper around the reflink system calls.

%package -n     python3-%{pypi_name}
Summary:        Python wrapper around the reflink system calls
%{?python_provide:%python_provide python3-%{pypi_name}}
Requires:       python3dist(cffi)
%description -n python3-%{pypi_name}
 Python reflink :alt: Documentation Status

%package -n python-%{pypi_name}-doc
Summary:        reflink documentation
%description -n python-%{pypi_name}-doc
Documentation for reflink

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
PYTHONPATH=${PWD} sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-reflink -f %{oreon_filedir}/python3-reflink.list
%files -n python-reflink-doc -f %{oreon_filedir}/python-reflink-doc.list

%changelog

%autochangelog
