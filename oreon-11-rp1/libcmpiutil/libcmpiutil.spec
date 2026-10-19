%global source0_hash ca0391fe2188dcc25c963f4fa5758744e6525252867c91dea6356c169c0e1deb
Summary:        CMPI Utility Library
Name: libcmpiutil
Version: 0.5.7
Release:        29%{?dist}
License: LicenseRef-Callaway-LGPLv2+
Source0:        ftp://libvirt.org/libvirt-cim/libcmpiutil-%{version}.tar.gz
Patch0: libcmpiutil-0.5.6-cast-align.patch
URL: http://libvirt.org/CIM/
BuildConflicts: sblim-cmpi-devel
# oreon:deps
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  libxml2-devel
BuildRequires:  make
BuildRequires:  tog-pegasus-devel
# /oreon:deps
%description
Libcmpiutil is a library of utility functions for CMPI providers.
The goal is to reduce the amount of repetitive work done in
most CMPI providers by encapsulating common procedures with more
"normal" APIs.  This extends from operations like getting typed
instance properties to standardizing method dispatch and argument checking.

%package devel
Summary: Libraries, includes, etc. to use the CMPI utility library
Requires: tog-pegasus-devel
Requires: pkgconfig
Requires: %{name} = %{version}-%{release}
%description devel
Includes and documentations for the CMPI utility library
The goal is to reduce the amount of repetitive work done in
most CMPI providers by encapsulating common procedures with more
"normal" APIs.  This extends from operations like getting typed
instance properties to standardizing method dispatch and argument checking.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
chmod -x *.c *.y *.h *.l

%patch -P0 -p0

%build

%configure --enable-static=no --disable-silent-rules CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
make %{?_smp_mflags}
%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libcmpiutil-devel -f %{oreon_filedir}/libcmpiutil-devel.list

%changelog

%autochangelog
