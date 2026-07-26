%global source0_hash f557911bf6171621e1f72ff35f5b1825bb35b52ed45325dcdee931e5d3c0787a

%?mingw_package_header

Summary:        MinGW Windows Internationalized Domain Name 2008 support library
Name:           mingw-libidn2
Version:        2.3.8
Release:        3%{?dist}
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/libidn/#libidn2

Source0:        https://ftp.gnu.org/gnu/libidn/libidn2-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/libidn/libidn2-%{version}.tar.gz.sig
Source2:        https://keys.openpgp.org/vks/v1/by-fingerprint/B1D2BD1375BECB784CF4F8C4D73CF638C53C06BE

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-binutils

BuildRequires:  gnupg2
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig

# mingw32-gcc and mingw64-gcc are not available on s390x builders
%if 0%{?rhel}
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

# Win32
%package -n mingw32-libidn2
Summary:        MinGW Windows IDN 2008 library the win32 target
Requires:       pkgconfig

%description -n mingw32-libidn2
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

%package -n mingw32-libidn2-static
Summary:        Static version of the MinGW Windows IDN 2008 library
Requires:       mingw32-libidn2 = %{version}-%{release}

%description -n mingw32-libidn2-static
Static version of the MinGW Windows IDN 2008 library.

# Win64
%package -n mingw64-libidn2
Summary:        MinGW Windows IDN 2008 library the win64 target
Requires:       pkgconfig

%description -n mingw64-libidn2
Libidn2 is an implementation of the IDNA2008 specifications in RFC
5890, 5891, 5892, 5893 and TR46 for internationalized domain names
(IDN). It is a standalone library, without any dependency on libidn.

%package -n mingw64-libidn2-static
Summary:        Static version of the MinGW Windows IDN 2008 library
Requires:       mingw64-libidn2 = %{version}-%{release}

%description -n mingw64-libidn2-static
Static version of the MinGW Windows IDN 2008 library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%setup -q -n libidn2-%{version}

%build
%mingw_configure --disable-nls --enable-static --enable-shared
%mingw_make %{?_smp_mflags}

%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install

# Remove documentation which duplicates native Fedora package.
rm -r $RPM_BUILD_ROOT%{mingw32_infodir}
rm -r $RPM_BUILD_ROOT%{mingw64_infodir}
rm -r $RPM_BUILD_ROOT%{mingw32_mandir}/man*
rm -r $RPM_BUILD_ROOT%{mingw64_mandir}/man*

# The .def file isn't interesting for other libraries/applications
rm -f $RPM_BUILD_ROOT%{mingw32_libdir}/libidn2-*.def
rm -f $RPM_BUILD_ROOT%{mingw64_libdir}/libidn2-*.def

# The executables are not useful in this build
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/lookup.exe
rm -f $RPM_BUILD_ROOT%{mingw32_bindir}/register.exe

rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/lookup.exe
rm -f $RPM_BUILD_ROOT%{mingw64_bindir}/register.exe

# Drop all .la files
find $RPM_BUILD_ROOT -name "*.la" -delete

# Win32
%files -n mingw32-libidn2
%license COPYING COPYING.LESSERv3 COPYING.unicode COPYINGv2
%{mingw32_bindir}/idn2.exe
%{mingw32_bindir}/libidn2-0.dll
%{mingw32_libdir}/libidn2.dll.a
%{mingw32_libdir}/pkgconfig/libidn2.pc
%{mingw32_includedir}/idn2.h

%files -n mingw32-libidn2-static
%{mingw32_libdir}/libidn2.a

# Win64
%files -n mingw64-libidn2
%license COPYING COPYING.LESSERv3 COPYING.unicode COPYINGv2
%{mingw64_bindir}/idn2.exe
%{mingw64_bindir}/libidn2-0.dll
%{mingw64_libdir}/libidn2.dll.a
%{mingw64_libdir}/pkgconfig/libidn2.pc
%{mingw64_includedir}/idn2.h

%files -n mingw64-libidn2-static
%{mingw64_libdir}/libidn2.a

%changelog
%autochangelog
