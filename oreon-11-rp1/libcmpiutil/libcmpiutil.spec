%global source0_hash ca0391fe2188dcc25c963f4fa5758744e6525252867c91dea6356c169c0e1deb

# -*- rpm-spec -*-

Summary: CMPI Utility Library
Name: libcmpiutil
Version: 0.5.7
Release: 29%{?dist}%{?extra_release}
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License: LicenseRef-Callaway-LGPLv2+
Source: ftp://libvirt.org/libvirt-cim/libcmpiutil-%{version}.tar.gz
Patch0: libcmpiutil-0.5.6-cast-align.patch
URL: http://libvirt.org/CIM/
BuildRequires:  gcc
BuildRequires: tog-pegasus-devel
BuildRequires: flex
BuildRequires: bison
BuildRequires: libxml2-devel
BuildRequires: make
BuildConflicts: sblim-cmpi-devel

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
# FIXME: Package has c11 inline compatibility issues.
# Work-around by appending -std=gnu89 to CFLAGS.
# Proper fix would be to fix the sources.
%configure --enable-static=no --disable-silent-rules CFLAGS="${RPM_OPT_FLAGS} -std=gnu89"
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p" install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

%ldconfig_scriptlets

%files
%doc doc/doxygen.conf doc/mainpage README
%license COPYING
%{_libdir}/lib*.so.*

%files devel
%{_libdir}/lib*.so
%dir %{_includedir}/libcmpiutil
%{_includedir}/libcmpiutil/*.h
%{_libdir}/pkgconfig/libcmpiutil.pc

%doc doc/SubmittingPatches

%changelog
%autochangelog
