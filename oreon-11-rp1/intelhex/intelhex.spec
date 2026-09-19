%global source0_hash b580f23c0b70a93da7830769c57466ae6fbbf894ed36bee426aef3ba8f259bd1

Name:          intelhex
Version:       2.3.0
Release:       22%{?dist}
Summary:       Utilities for manipulating Intel HEX file format
# Automatically converted from old format: BSD - review is highly recommended.
License:       LicenseRef-Callaway-BSD
URL:           https://github.com/python-intelhex/intelhex
Source0:       https://github.com/python-intelhex/intelhex/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRequires: dos2unix
BuildRequires: python3-devel
BuildRequires: python3-sphinx
BuildRequires: make

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

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel
pushd docs/manual/
make html
popd 

%install
%pyproject_install

%files
%doc NEWS.rst README.rst
%{_bindir}/*.py

%files -n python3-intelhex
%license LICENSE.txt
%{python3_sitelib}/intelhex*

%files docs
%doc docs/intelhex.pdf docs/manual.txt
%doc docs/manual/.build/html/*.html
%doc docs/manual/.build/html/searchindex.js

%changelog
%autochangelog
