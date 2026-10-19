%global source0_hash 23d43c15580e6a3863b76798d7e3ac93b99ff5bd2cbf78a8abc6ca7e3a136a02
Name:           gattlib
Version:        0.7.2
Release:        1%{?dist}
Summary:        Library to access GATT information from BLE (Bluetooth Low Energy) devices
License:        GPL-2.0-or-later AND BSD-3-Clause
URL:            https://github.com/labapart/gattlib
Source0:        https://github.com/labapart/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:         https://github.com/labapart/gattlib/commit/a074af0d6a21665d3dfbd785ffd788146afeacef.patch
Patch1:         https://github.com/labapart/gattlib/commit/0d2d629b84573f2e7f2186c973a3124c4db5c630.patch
Patch2:         https://github.com/labapart/gattlib/commit/fec94997dde6a1f33efbd15f920eb7566c7be72a.patch
Patch3:         https://github.com/labapart/gattlib/commit/1580056bce260f0d8ad7ccc8b105c34057cd1fbd.patch
Patch4:         %{name}-docs.patch
Patch5:         https://patch-diff.githubusercontent.com/raw/labapart/gattlib/pull/292.patch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(bluez)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libpcre2-8)
BuildRequires:  python3-breathe
BuildRequires:  python3-sphinx
BuildRequires:  sed
# /oreon:deps
%description
GattLib is a library used to access Generic Attribute Profile (GATT) protocol of
BLE (Bluetooth Low Energy) devices.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconf-pkg-config      
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        examples
Summary:        Example programs using %{name}
%description    examples
This package provides various demonstration programs that leverage %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

# Remove bluez source:
rm -fr bluez

# Set shared library version
sed -i dbus/CMakeLists.txt \
  -e '/add_library(%{name} SHARED/a\ \ set_target_properties(%{name} PROPERTIES VERSION 0 SOVERSION %{version})'

%build

%cmake \
  -DCMAKE_SKIP_RPATH=YES \
  -DGATTLIB_BUILD_EXAMPLES=YES \
  -DGATTLIB_SHARED_LIB=YES \
  -DGATTLIB_BUILD_DOCS=YES \
  -DGATTLIB_PYTHON_INTERFACE=NO
%cmake_build
mv %{_vpath_builddir}/docs/docs/gattlib/sphinx/ html
%install
%cmake_install
for p in %{_vpath_builddir}/examples/*; do
  install -Dpm0755 ${p}/$(basename $p) %{buildroot}%{_bindir}/gatt_$(basename $p)
done
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n gattlib-devel -f %{oreon_filedir}/gattlib-devel.list
%files -n gattlib-examples -f %{oreon_filedir}/gattlib-examples.list

%changelog

%autochangelog
