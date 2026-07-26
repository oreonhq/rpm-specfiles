%global source0_hash c90b53949c767f049733b442cd6e0a48648b55d99d4df5ef3f852d985f45e880

%{?mingw_package_header}

Name:           mingw-hamlib
Version:        3.3
Release:        16%{?dist}
Summary:        Run-time library to control radio transceivers and receivers

# Automatically converted from old format: GPLv2+ and LGPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later AND LicenseRef-Callaway-LGPLv2+
URL:            http://hamlib.sourceforge.net
Source0:        http://downloads.sourceforge.net/hamlib/hamlib-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-libusbx

BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-binutils

%description
Hamlib provides a standardized programming interface that applications
can use to send the appropriate commands to a radio.

Also included in the package is a simple radio control program 'rigctl',
which lets one control a radio transceiver or receiver, either from
command line interface or in a text-oriented interactive interface.

%package -n mingw32-hamlib
Summary:        Run-time library to control radio transceivers and receivers for Win32

%description -n mingw32-hamlib

%package -n mingw64-hamlib
Summary:        Run-time library to control radio transceivers and receivers for Win64

%description -n mingw64-hamlib

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n hamlib-%{version}

%build
%mingw_configure --disable-static
%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=%{buildroot}

find %{buildroot} -name "*.la" -delete

rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -rf %{buildroot}%{mingw32_datadir}/{doc,info,man}
rm -f %{buildroot}%{mingw64_bindir}/*.exe
rm -rf %{buildroot}%{mingw64_datadir}/{doc,info,man}

%files -n mingw32-hamlib
%{mingw32_bindir}/libhamlib-2.dll
%{mingw32_bindir}/libhamlib++-2.dll
%{mingw32_libdir}/libhamlib.dll.a
%{mingw32_libdir}/libhamlib++.dll.a
%{mingw32_libdir}/pkgconfig/hamlib.pc
%{mingw32_includedir}/hamlib/
%{mingw32_datadir}/aclocal/

%files -n mingw64-hamlib
%{mingw64_bindir}/libhamlib-2.dll
%{mingw64_bindir}/libhamlib++-2.dll
%{mingw64_libdir}/libhamlib.dll.a
%{mingw64_libdir}/libhamlib++.dll.a
%{mingw64_libdir}/pkgconfig/hamlib.pc
%{mingw64_includedir}/hamlib/
%{mingw64_datadir}/aclocal/

%changelog
%autochangelog
