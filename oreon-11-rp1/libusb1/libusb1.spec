%global source2_hash aec028b1e736a566b62b4d149c281aef661369f6a124fbe87277cba2e2ef1ab9
%global source1_hash 7e8916e689a399b98df1087cfc48eab33a6bfd8027291c5af00c3fbba90a2cec
%global source0_hash fea36f34f9156400209595e300840767ab1a385ede1dc7ee893015aea9c6dbaf
%global source2_key_fpr C68187379B23DE9EFC46651E2C80FF56C6830A0E
%bcond mingw %[0%{?fedora} && !0%{?flatpak}]
Summary:        Library for accessing USB devices
Name:           libusb1
Version:        1.0.30
Release:        1%{?dist}
Source0:        https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2
Source1:        https://github.com/libusb/libusb/releases/download/v%{version}/libusb-%{version}.tar.bz2.asc
Source2:        https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xc68187379b23de9efc46651e2c80ff56c6830a0e#/%{name}.keyring
License:        LGPL-2.1-or-later
URL:            http://libusb.info
Provides:       libusbx = %{version}-%{release}
Obsoletes:      libusbx < %{version}-%{release}
%if %{with mingw}
Provides:       mingw-libusbx = %{version}-%{release}
Obsoletes:      mingw-libusbx < %{version}-%{release}
%endif
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gnupg2
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc-c++
BuildRequires:  systemd-devel
BuildRequires:  umockdev-devel
# /oreon:deps
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

%(test -z "%{source2_key_fpr}" || { f="%{SOURCE2}"; test -f "$f" || { echo "oreon: missing Source2 key $f" >&2; exit 1; }; fpr=$(GNUPGHOME=$(mktemp -d); export GNUPGHOME; trap 'rm -rf "$GNUPGHOME"' EXIT; gpg --batch --with-colons --import-options show-only --import "$f" | awk -F: '/^fpr:/ {print toupper($10); exit}'); test "$fpr" = "%{source2_key_fpr}" || { echo "oreon: Source2 key fingerprint mismatch" >&2; exit 1; }; })
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup -p1 -n libusb-%{version}
chmod -x examples/*.c
mkdir -p m4
sed -i \
    -e '/AM_LDFLAGS = -static/d' \
    -e 's/test_static_link_flag = -static/test_static_link_flag =/' \
    tests/Makefile.am
autoscan
aclocal
autoconf
automake --add-missing

%build

mkdir %{_target_os}
pushd %{_target_os}
%define _configure ../configure
%configure --disable-static --enable-examples-build
%{make_build}
pushd doc
make docs
popd
pushd tests
make
popd
popd
%if %{with mingw}
%mingw_configure --disable-static
%mingw_make_build
%endif
%install
pushd %{_target_os}
%{make_install}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
install -m 755 tests/.libs/init_context $RPM_BUILD_ROOT%{_bindir}/libusb-test-init_context
install -m 755 tests/.libs/set_option $RPM_BUILD_ROOT%{_bindir}/libusb-test-set_option
install -m 755 tests/.libs/stress $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress
install -m 755 tests/.libs/stress_mt $RPM_BUILD_ROOT%{_bindir}/libusb-test-stress_mt
install -m 755 tests/.libs/umockdev $RPM_BUILD_ROOT%{_bindir}/libusb-test-umockdev
install -m 755 examples/.libs/testlibusb \
    $RPM_BUILD_ROOT%{_bindir}/libusb-test-libusb
for i in fxload listdevs xusb; do
    install -m 755 examples/.libs/$i \
        $RPM_BUILD_ROOT%{_bindir}/libusb-example-$i
done
rm $RPM_BUILD_ROOT%{_libdir}/*.la
popd
%if %{with mingw}
%mingw_make_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/*/lib*.so.* usr/*/lib*.so.* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
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
%files -f %{oreon_filedir}/main.list
%files -n libusb1-devel -f %{oreon_filedir}/libusb1-devel.list
%files -n libusb1-devel-doc -f %{oreon_filedir}/libusb1-devel-doc.list
%files -n libusb1-tests-examples -f %{oreon_filedir}/libusb1-tests-examples.list
%files -n mingw32-libusb1 -f %{oreon_filedir}/mingw32-libusb1.list
%files -n mingw64-libusb1 -f %{oreon_filedir}/mingw64-libusb1.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0.29-1
- Prepare for Oreon 11 (RP1)
