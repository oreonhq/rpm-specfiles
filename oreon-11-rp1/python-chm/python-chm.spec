%global source0_hash 23cdc3bbbeb97b57b472a67a0c7c96c6f1ec2d684a73a69fa84aaaeb195cab6c
%global pypi_name pychm
%global desc %{expand: \
The python chm package provides three modules, chm, chmlib and extra,\
which provide access to the API implemented by the C library chmlib\
and some additional classes and functions. They are used to access\
MS-ITSS encoded files - Compressed Html Help files (.chm).}
Name:           python-chm
Version:        0.8.6
Release:        21%{?dist}
Summary:        Python package for CHM files handling
License:        GPL-2.0-or-later
URL:            https://github.com/dottedmag/%{pypi_name}/
Source0:        https://github.com/dottedmag/%{pypi_name}//archive/v%{version}/%{pypi_name}-%{version}.tar.gz
%{?python_enable_dependency_generator}
# oreon:deps
BuildRequires:  chmlib
BuildRequires:  chmlib-devel
BuildRequires:  gcc-c++
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# /oreon:deps
%description
%{desc}

%package -n python3-%{pypi_name}            
Summary:        Python package for CHM files handling
%{?python_provide:%python_provide python3-%{pypi_name}}
%description -n python3-%{pypi_name}
%{desc}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build

%py3_build
%install
%py3_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n python3-pychm -f %{oreon_filedir}/python3-pychm.list

%changelog

%autochangelog
