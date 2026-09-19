%global source0_hash 5d84dec684c27b97b921d2f3b73218cb773cf4ea915caee317ac8fc73cef8136

Name:           hidapi
Version:        0.15.0
Release:        3%{?dist}
Summary:        Library for communicating with USB and Bluetooth HID devices

License:        GPL-3.0-only OR BSD-3-Clause
URL:            https://github.com/libusb/hidapi

Source0:        %{url}/archive/%{name}-%{version}.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: libudev-devel
BuildRequires: libusb1-devel

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc
BuildRequires: mingw32-binutils

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc
BuildRequires: mingw64-binutils

%global _description %{expand:
HIDAPI is a multi-platform library which allows an application to interface
with USB and Bluetooth HID-class devices on Windows, Linux, FreeBSD and Mac OS
X.  On Linux, either the hidraw or the libusb back-end can be used. There are
trade-offs and the functionality supported is slightly different.}

%description %_description

%package devel
Summary: Development files for hidapi
Requires: %{name}%{?_isa} = %{version}-%{release}

%description -n hidapi-devel
This package contains development files for hidapi which provides access to
USB and Bluetooth HID-class devices.

%package -n mingw32-hidapi
Summary:        %{summary}
Obsoletes:      mingw32-hidapi-static < 0.11.2-6

%description -n mingw32-hidapi %_description

%package -n mingw64-hidapi
Summary:        %{summary}
Obsoletes:      mingw64-hidapi-static < 0.11.2-6

%description -n mingw64-hidapi %_description

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{name}-%{version}

%build
%cmake
%cmake_build

%mingw_cmake
%mingw_make_build

%install
%cmake_install

%mingw_make_install
%mingw_debug_install_post

%files
%doc AUTHORS.txt README.md LICENSE*.txt
%{_libdir}/libhidapi-*.so.*

%files devel
%{_includedir}/hidapi
%{_libdir}/cmake/hidapi
%{_libdir}/libhidapi-hidraw.so
%{_libdir}/libhidapi-libusb.so
%{_libdir}/pkgconfig/hidapi-hidraw.pc
%{_libdir}/pkgconfig/hidapi-libusb.pc

%files -n mingw32-hidapi
%doc AUTHORS.txt README.md LICENSE*.txt
%{mingw32_libdir}/cmake/hidapi
%{mingw32_bindir}/libhidapi.dll
%{mingw32_libdir}/libhidapi.dll.a
%{mingw32_libdir}/pkgconfig/hidapi.pc
%{mingw32_includedir}/hidapi

%files -n mingw64-hidapi
%doc AUTHORS.txt README.md LICENSE*.txt
%{mingw64_libdir}/cmake/hidapi
%{mingw64_bindir}/libhidapi.dll
%{mingw64_libdir}/libhidapi.dll.a
%{mingw64_libdir}/pkgconfig/hidapi.pc
%{mingw64_includedir}/hidapi

%changelog
%autochangelog
