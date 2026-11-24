# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash 51aaac41391a915bd9bad07710957424b046410a276e7deaff24a870929d33ce
%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap

Name:           gavl
Version:        1.4.0
Release:        %{autorelease}
Summary:        A library for handling uncompressed audio and video data

License:        GPL-3.0-or-later
URL:            http://gmerlin.sourceforge.net/
Source0:        http://downloads.sourceforge.net/gmerlin/gavl-%{version}.tar.gz
Patch1:         gavl-1.1.1-system_libgdither.patch
Patch2: gavl-configure-c99.patch
Patch3: gavl-c99.patch

BuildRequires: oreon-rpm-macros
BuildRequires: clang
BuildRequires:  libtool

BuildRequires:  doxygen

BuildRequires:  libpng-devel >= 1.0.8
BuildRequires:  libgdither-devel
BuildRequires: make

%description
Gavl is a library for handling and converting uncompressed audio and
video data. It provides datatypes for audio/video formats and standardized
structures to store the data. It supports converting between all formats.
Some conversion functions are available in multiple versions (MMX...),
which are selected by compile time configuration, CPU autodetection and
user options.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%oreon_sha256
%setup -q
%patch -P1 -p1 -b .gdither
%patch -P2 -p1
%patch -P3 -p1

sed -i -i 's/LQT_TRY_CFLAGS/dnl LQT_TRY_CFLAGS/g' configure.ac
sed -i -i 's/LQT_OPT_CFLAGS/dnl LQT_OPT_CFLAGS/g' configure.ac

sh autogen.sh

%build
%configure \
  --disable-static \
  --disable-cpu-clip \
  --enable-libgdither

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

touch -r include/gavl/gavl.h $RPM_BUILD_ROOT%{_includedir}/gavl/gavl_version.h

%ldconfig_scriptlets

%files
%doc AUTHORS COPYING README TODO
%exclude %{_docdir}/gavl/apiref
%{_libdir}/*.so.*

%files devel
%doc %{_docdir}/gavl/apiref/
%{_includedir}/gavl/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gavl.pc

%changelog
%autochangelog
