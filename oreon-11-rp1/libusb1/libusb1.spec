# Copyright (C) 2026 Oreon HQ
# SPDX-License-Identifier: GPL-2.0-or-later

%global source0_hash fea36f34f9156400209595e300840767ab1a385ede1dc7ee893015aea9c6dbaf
%global source2_hash aec028b1e736a566b62b4d149c281aef661369f6a124fbe87277cba2e2ef1ab9

%{!?oreon_bootstrap:%global oreon_bootstrap %{nil}}
%bcond bootstrap 0
%oreon_bootstrap
%bcond mingw 1

Summary:        Library for accessing USB devices
Name:           libusb1
Version:        1.0.30
Release:        1%{?dist}
Source0:        https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2
Source1:        libusb-1.0.30.tar.bz2.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xc68187379b23de9efc46651e2c80ff56c6830a0e#/libusb1.keyring
License:        LGPL-2.1-or-later
URL:            http://libusb.info
BuildRequires:  systemd-devel doxygen libtool
BuildRequires:  umockdev-devel
BuildRequires:  make
BuildRequires:  gcc
BuildRequires:  gnupg2
# libusbx was removed in F34
Provides:       libusbx = %{version}-%{release}
Obsoletes:      libusbx < %{version}-%{release}

%if %{with mingw}
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc-c++
BuildRequires:  oreon-rpm-macros
# mingw-libusbx was removed in F42
Provides:       mingw-libusbx = %{version}-%{release}
Obsoletes:      mingw-libusbx < %{version}-%{release}
%endif

%description
This package provides a way for applications to access USB devices.

libusb is a library for USB device access from Linux, macOS,
Windows, OpenBSD/NetBSD, Haiku and Solaris userspace.

libusb is abstracted internally in such a way that it can hopefully
be ported to other operating systems.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusbx-devel = %{version}-%{release}
Obsoletes:      libusbx-devel < %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%package devel-doc
Summary:        Development files for %{name}
Requires:       libusb1-devel = %{version}-%{release}
Provides:       libusbx-devel-doc = %{version}-%{release}
Obsoletes:      libusbx-devel-doc < %{version}-%{release}
BuildArch:      noarch

%description devel-doc
This package contains API documentation for %{name}.


%package        tests-examples
Summary:        Tests and examples for %{name}
# The fxload example is GPL-2.0-or-later, the rest is LGPL-2.1-or-later, like libusb itself.
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Requires:       %{name}%{?_isa} = %{version}-%{release}
Provides:       libusbx-tests-examples = %{version}-%{release}
Obsoletes:      libusbx-tests-examples < %{version}-%{release}

%description tests-examples
This package contains tests and examples for %{name}.

%if %{with mingw}
%package -n mingw32-%{name}
Summary:       MinGW Windows %{name} library
Provides:      mingw32-libusbx = %{version}-%{release}
Obsoletes:     mingw32-libusbx < %{version}-%{release}

%description -n mingw32-%{name}
MinGW Windows %{name} library.

%package -n mingw64-%{name}
Summary:       MinGW Windows %{name} library
Provides:      mingw64-libusbx = %{version}-%{release}
Obsoletes:     mingw64-libusbx < %{version}-%{release}

%description -n mingw64-%{name}
MinGW Windows %{name} library.
%endif

%prep
%oreon_sha256
echo '%{source2_hash}  %{SOURCE2}' | sha256sum -c -

%oreon_gpgverify --key %{SOURCE2} --sig %{SOURCE1} --data %{SOURCE0}
%autosetup -p1 -n libusb-%{version}

%build
mkdir %{_target_os}
pushd %{_target_os}
%define _configure ../configure
%configure --disable-static --enable-examples-build
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
%{make_build}
pushd doc
make docs
popd
pushd tests
make
popd
popd

%if %{with mingw}
# MinGW build
%mingw_configure --disable-static
%mingw_make_build
%endif


%install
pushd %{_target_os}
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 tests/init_context $RPM_BUILD_ROOT%{_bindir}/libusb-test-init_context
install -m 755 tests/set_option $RPM_BUILD_ROOT%{_bindir}/libusb-test-set_option
install -m 755 tests/stress $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
install -m 755 tests/stress_mt $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress_mt
install -m 755 tests/.libs/umockdev $RPM_BUILD_ROOT%{_bindir}/libusb-test-umockdev
install -m 755 examples/.libs/testlibusb \
    $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
# Some examples are very device-specific / require specific hw and miss --help
# So we only install a subset of more generic / useful examples
for i in fxload listdevs xusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-example-$i
done
rm $RPM_BUILD_ROOT%{_libdir}/*.la
popd

%if %{with mingw}
%mingw_make_install
%endif


%check
pushd %{_target_os}
LD_LIBRARY_PATH=libusb/.libs ldd $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-init_context
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-set_option
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-umockdev
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
LD_LIBRARY_PATH=libusb/.libs $RPM_BUILD_ROOT%{_bindir}/libusb-example-listdevs
popd


%ldconfig_scriptlets


%files
%license COPYING
%doc AUTHORS README ChangeLog
%{_libdir}/*.so.*

%files devel
%{_includedir}/libusb-1.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/libusb-1.0.pc

%files devel-doc
%doc %{_target_os}/doc/api-1.0 examples/*.c

%files tests-examples
%{_bindir}/libusb-example-fxload
%{_bindir}/libusb-example-listdevs
%{_bindir}/libusb-example-xusb
%{_bindir}/libusb-test-init_context
%{_bindir}/libusb-test-set_option
%{_bindir}/libusb-test-stress
%{_bindir}/libusb-test-stress_mt
%{_bindir}/libusb-test-umockdev
%{_bindir}/libusb-test-libusb

%if %{with mingw}
%files -n mingw32-libusb1
%license COPYING
%doc AUTHORS README ChangeLog
%{mingw32_bindir}/libusb-1.0.dll
%{mingw32_includedir}/libusb-1.0
%{mingw32_libdir}/*.dll.a
%{mingw32_libdir}/pkgconfig/libusb-1.0.pc

%files -n mingw64-libusb1
%license COPYING
%doc AUTHORS README ChangeLog
%{mingw64_bindir}/libusb-1.0.dll
%{mingw64_includedir}/libusb-1.0
%{mingw64_libdir}/*.dll.a
%{mingw64_libdir}/pkgconfig/libusb-1.0.pc
%endif

