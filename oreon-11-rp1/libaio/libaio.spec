%global source0_hash 62cf871ad8fd09eb3418f00aca7a7d449299b8e1de31c65f28bf6a2ef1fa502a

Name: libaio
Version: 0.3.111
Release: 23%{?dist}
Summary: Linux-native asynchronous I/O access library
License: LGPL-2.0-or-later
Source: http://releases.pagure.org/libaio/libaio-0.3.111.tar.gz

Patch1: libaio-install-to-destdir-slash-usr.patch
Patch2: libaio-remove-nostartfiles-nostdlib-from-build-flags.patch

BuildRequires: gcc
BuildRequires: make

%description
The Linux-native asynchronous I/O facility ("async I/O", or "aio") has a
richer API and capability set than the simple POSIX async I/O facility.
This library, libaio, provides the Linux-native API for async I/O.
The POSIX async I/O facility requires this library in order to provide
kernel-accelerated async I/O capabilities, as do applications which
require the Linux-native async I/O API.

%define libdir /%{_lib}
%define usrlibdir %{_prefix}/%{_lib}

%package devel
Summary: Development files for Linux-native asynchronous I/O access
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
This package provides header files to include and libraries to link with
for the Linux-native asynchronous I/O facility ("async I/O", or "aio").

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -a 0
%patch -P1 -p0 -b .install-to-destdir-slash-usr
%patch -P1 -p1 -b .install-to-destdir-slash-usr
%patch -P2 -p0 -b .nostdlib
%patch -P2 -p1 -b .nostdlib
mv %{name}-%{version} compat-%{name}-%{version}

%build
# This package uses ASMs to implement symbol versioning and is thus
# incompatible with LTO
%define _lto_cflags %{nil}

# A library with a soname of 1.0.0 was inadvertantly released.  This
# build process builds a version of the library with the broken soname in
# the compat-libaio-0.3.103 directory, and then builds the library again
# with the correct soname.
%set_build_flags
cd compat-%{name}-%{version}
make soname='libaio.so.1.0.0' libname='libaio.so.1.0.0'
cd ..
make

%install
cd compat-%{name}-%{version}
install -D -m 755 src/libaio.so.1.0.0 \
  $RPM_BUILD_ROOT/%{usrlibdir}/libaio.so.1.0.0
cd ..
make destdir=$RPM_BUILD_ROOT prefix=/ libdir=%{libdir} usrlibdir=%{usrlibdir} \
	includedir=%{_includedir} install

find %{buildroot} -name '*.a' -delete

%ldconfig_scriptlets

%files
%license COPYING
%attr(0755,root,root) %{usrlibdir}/libaio.so.*

%files devel
%attr(0644,root,root) %{_includedir}/*
%attr(0755,root,root) %{usrlibdir}/libaio.so

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.3.111-23
- Prepare for Oreon 11 (RP1)
