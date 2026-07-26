%global source0_hash 924dfb5c78328fae45a4c93a01bc83bb72c1310abeed119109255627a8baa332

%{?mingw_package_header}

Name:           mingw-usbredir
Version:        0.14.0
Release:        5%{?dist}
Summary:        MinGW USB network redirection protocol libraries

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://spice-space.org/page/UsbRedir
Source0:        http://spice-space.org/download/usbredir/usbredir-%{version}.tar.xz
Source1:        http://spice-space.org/download/usbredir/usbredir-%{version}.tar.xz.sig
Source2:        victortoso-E37A484F.keyring
Patch0001:      0001-Fix-Wincompatible-pointer-types-on-mingw32.patch

BuildArch:      noarch
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-libusbx >= 1.0.9
BuildRequires:  mingw64-libusbx >= 1.0.9
BuildRequires:  mingw32-glib2
BuildRequires:  mingw64-glib2
BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  gnupg2

%description
The usbredir libraries allow USB devices to be used on remote and/or virtual
hosts over TCP.  The following libraries are provided:

usbredirparser:
A library containing the parser for the usbredir protocol

usbredirhost:
A library implementing the USB host side of a usbredir connection.
All that an application wishing to implement a USB host needs to do is:
* Provide a libusb device handle for the device
* Provide write and read callbacks for the actual transport of usbredir data
* Monitor for usbredir and libusb read/write events and call their handlers

%package -n mingw32-usbredir
Summary:        MinGW USB network redirection protocol libraries
Requires:       pkgconfig

%description -n mingw32-usbredir
This package contains the header files and libraries needed to develop
applications that use usbredir with MinGW.

%package -n mingw32-usbredir-static
Summary:        MinGW USB network redirection protocol static libraries
Requires:       mingw32-usbredir = %{version}-%{release}

%description -n mingw32-usbredir-static
This package contains the static libraries needed to develop
applications that use usbredir with MinGW.

%package -n mingw64-usbredir
Summary:        MinGW USB network redirection protocol libraries
Requires:       pkgconfig

%description -n mingw64-usbredir
This package contains the header files and libraries needed to develop
applications that use usbredir with MinGW.

%package -n mingw64-usbredir-static
Summary:        MinGW USB network redirection protocol static libraries
Requires:       mingw64-usbredir = %{version}-%{release}

%description -n mingw64-usbredir-static
This package contains the static libraries needed to develop
applications that use usbredir with MinGW.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

gpgv2 --quiet --keyring %{SOURCE2} %{SOURCE1} %{SOURCE0}
%autosetup -S git_am -p1 -n usbredir-%{version}

%build
%mingw_meson \
    -Dgit_werror=disabled \
    -Dtools=enabled \
    -Dfuzzing=disabled

%mingw_ninja

%install
%mingw_ninja_install

# Libtool files don't need to be bundled
find $RPM_BUILD_ROOT -name "*.la" -delete

%files -n mingw32-usbredir
%doc ChangeLog.md COPYING.LIB README.md TODO
%{mingw32_bindir}/libusbredirhost-1.dll
%{mingw32_bindir}/libusbredirparser-1.dll
%{mingw32_bindir}/usbredirect.exe
%{mingw32_libdir}/libusbredirhost.dll.a
%{mingw32_libdir}/libusbredirparser.dll.a
%{mingw32_includedir}/usbredirfilter.h
%{mingw32_includedir}/usbredirhost.h
%{mingw32_includedir}/usbredirparser.h
%{mingw32_includedir}/usbredirproto.h
%{mingw32_libdir}/pkgconfig/libusbredirhost.pc
%{mingw32_libdir}/pkgconfig/libusbredirparser-0.5.pc
%{mingw32_mandir}/man1/usbredirect.1

%files -n mingw32-usbredir-static
%{mingw32_libdir}/libusbredirhost.dll.a
%{mingw32_libdir}/libusbredirparser.dll.a

%files -n mingw64-usbredir
%doc ChangeLog.md COPYING.LIB README.md TODO
%{mingw64_bindir}/libusbredirhost-1.dll
%{mingw64_bindir}/libusbredirparser-1.dll
%{mingw64_bindir}/usbredirect.exe
%{mingw64_libdir}/libusbredirhost.dll.a
%{mingw64_libdir}/libusbredirparser.dll.a
%{mingw64_includedir}/usbredirfilter.h
%{mingw64_includedir}/usbredirhost.h
%{mingw64_includedir}/usbredirparser.h
%{mingw64_includedir}/usbredirproto.h
%{mingw64_libdir}/pkgconfig/libusbredirhost.pc
%{mingw64_libdir}/pkgconfig/libusbredirparser-0.5.pc
%{mingw64_mandir}/man1/usbredirect.1

%files -n mingw64-usbredir-static
%{mingw64_libdir}/libusbredirhost.dll.a
%{mingw64_libdir}/libusbredirparser.dll.a

%changelog
%autochangelog
