%global source0_hash 2f4d4191cd196c1fba131daec03b621db75129d8255c832fc66b259d9fc46e7b

Name: libmodbus
Version: 3.1.12
Release: 1%{?dist}
Summary: A Modbus library
License: LGPL-2.1-or-later
URL: http://www.libmodbus.org/

Source0: https://github.com/stephane/libmodbus/releases/download/v%{version}/libmodbus-%{version}.tar.gz
Patch 0: libmodbus-revert-CFLAGS-changes.patch

BuildRequires: gcc
BuildRequires: xmlto
BuildRequires: asciidoc
BuildRequires: make

%description
libmodbus is a C library designed to provide a fast and robust implementation of
the Modbus protocol. It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains the libmodbus shared library.

%package devel
Summary: Development files for libmodbus
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
libmodbus is a C library designed to provide a fast and robust implementation of
the Modbus protocol. It runs on Linux, Mac OS X, FreeBSD, QNX and Windows.

This package contains libraries, header files and developer documentation needed
for developing software which uses the libmodbus library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete

%ldconfig_scriptlets

%files
%license COPYING*
%doc AUTHORS NEWS.md README.md
%{_libdir}/libmodbus.so.*

%files devel
%{_includedir}/modbus/
%{_libdir}/pkgconfig/libmodbus.pc
%{_libdir}/libmodbus.so

%changelog
%autochangelog
