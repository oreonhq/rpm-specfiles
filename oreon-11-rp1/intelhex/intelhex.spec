%global source0_hash b580f23c0b70a93da7830769c57466ae6fbbf894ed36bee426aef3ba8f259bd1
Name:          intelhex
Version:       2.3.0
Release:        1%{?dist}
Summary:        Utilities for manipulating Intel HEX file format
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/python-intelhex/intelhex
Source0:        https://github.com/python-intelhex/intelhex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-intelhex = %{version}-%{release}
# /oreon:deps
%description
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard for representation of code
to be programmed into microelectronic devices.

This work implements an intelhex Python library and a number of utilities to 
read, write, create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" hex2bin and bin2hex converters and more, those based on the
library itself. Check the docs to know more.

%package -n python3-intelhex
Summary:  A python3 library for manipulating Intel HEX file format
%{?python_provide:%python_provide python3-intelhex}
%description -n python3-intelhex
The Intel HEX file format is widely used in microprocessors and microcontrollers
area (embedded systems etc) as the de facto standard for representation of code
to be programmed into microelectronic devices.

This work implements an intelhex Python library and a number of utilities to 
read, write, create from scratch and manipulate data from Intel HEX file format.

The distribution package also includes several convenience Python scripts,
including "classic" hex2bin and bin2hex converters and more, those based on the
library itself. Check the docs to know more.

%package docs
Summary:  Manuak for the IntelHex python library
%description docs
User manual for IntelHex

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
dos2unix README.rst
dos2unix NEWS.rst
sed -i '1d' intelhex/bench.py

%build

%pyproject_wheel
pushd docs/manual/
make html
popd 
%install
%pyproject_install
%oreon_autofiles python3-intelhex usr/lib/python3*/site-packages/intelhex* usr/lib64/python3*/site-packages/intelhex* usr/bin/*
%oreon_autofiles main usr/lib/python3*/site-packages/intelhex* usr/lib64/python3*/site-packages/intelhex* usr/bin/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files
%files -n python3-intelhex -f %{oreon_filedir}/python3-intelhex.list
%files -n intelhex-docs -f %{oreon_filedir}/intelhex-docs.list

%changelog

%autochangelog
