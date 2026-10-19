%global source0_hash f74bff7c42407413ed97a2f887496acfcc3b951aa480bfcd2857992bebeb007c
Name:		python-hwdata
Version:	2.4.3
Release:        1%{?dist}
Summary:        Python bindings to hwdata package
BuildArch:  noarch
License:	GPL-2.0-or-later
URL:		https://github.com/xsuchy/python-hwdata
Source0:        https://github.com/xsuchy/python-hwdata/archive/refs/tags/python-hwdata-%{version}-1.tar.gz#/python-hwdata-%{version}.tar.gz
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-hwdata = %{version}-%{release}
# /oreon:deps
%description
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

%package -n python3-hwdata
Summary:	Python bindings to hwdata package
BuildRequires:	python3-devel
%{?python_provide:%python_provide python3-hwdata}
%description -n python3-hwdata
Provide python interface to database stored in hwdata package.
It allows you to get human readable description of USB and PCI devices.

This is the Python 3 build of the module.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -n python-hwdata-python-hwdata-%{version}-1 -q

%build

%pyproject_wheel
%install
%pyproject_install
%oreon_autofiles python3-hwdata usr/lib/python3*/site-packages/hwdata* usr/lib64/python3*/site-packages/hwdata* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/hwdata* usr/lib64/python3*/site-packages/hwdata* usr/bin/*

%check

%py3_check_import hwdata
%files
%files -n python3-hwdata -f %{oreon_filedir}/python3-hwdata.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.4.3-6
- Import
