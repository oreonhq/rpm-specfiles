%global source0_hash 2c5234a27d8bd560c65eee73d0b72e65ddfdf018b256b4eccab0680d577db1d5

Name:           pybluez
Version:        0.23
Release:        23%{?dist}
Summary:        Python API for the BlueZ bluetooth stack 

License:        GPL-2.0-only
URL:            https://github.com/pybluez/pybluez/wiki
Source0:        https://github.com/pybluez/pybluez/archive/%{version}.tar.gz
Patch0:         pybluez-py310.patch
Patch1:         no-2to3.patch
Patch2:         427.patch

BuildRequires:  bluez-libs-devel gcc
BuildRequires:  python3-devel
BuildRequires:  python3-gattlib
                   
%description
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create Bluetooth
applications.

%package -n     python3-bluez
Summary:        A Python interface to bluez for Python 3
Requires:       python3-gattlib

%description -n python3-bluez
PyBluez is an effort to create python wrappers around system Bluetooth
resources to allow Python developers to easily and quickly create Bluetooth
applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p0
%patch -P2 -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
# This file shouldn't be executable - it's going into %doc
chmod a-x examples/bluezchat/bluezchat.py
%pyproject_install
%pyproject_save_files -l '*'

%check
%pyproject_check_import -t

%files -n python3-bluez -f %{pyproject_files}
%{!?_licensedir:%global license %%doc}

%changelog
%autochangelog
