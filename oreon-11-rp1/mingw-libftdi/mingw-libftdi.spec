%global source0_hash 7c7091e9c86196148bd41177b4590dccb1510bfe6cea5bf7407ff194482eb049

%?mingw_package_header

%global name1 libftdi
Name:           mingw-%{name1}
Version:        1.5
Release:        4%{?dist}
Summary:        MinGW library to program and control the FTDI USB controller

# Automatically converted from old format: LGPLv2 and GPLv2 - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2 AND GPL-2.0-only
URL:            https://www.intra2net.com/en/developer/libftdi/
Source0:        https://www.intra2net.com/en/developer/%{name1}/download/%{name1}1-%{version}.tar.bz2
# http://developer.intra2net.com/git/?p=libftdi;a=commitdiff;h=cdb28383402d248dbc6062f4391b038375c52385;hp=5c2c58e03ea999534e8cb64906c8ae8b15536c30
Patch0:         libftdi-1.5-fix_pkgconfig_path.patch
# http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00003.html
Patch1:         libftdi-1.5-no-distutils.patch
# http://developer.intra2net.com/mailarchive/html/libftdi/2023/msg00005.html
Patch2:         libftdi-1.5-cmake-deps.patch
# Fix for SWIG 4.3.0
# https://bugzilla.redhat.com/show_bug.cgi?id=2319133
# http://developer.intra2net.com/mailarchive/html/libftdi/2024/msg00024.html
Patch3:         libftdi-1.5-swig-4.3.patch
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw32-libconfuse
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-libusbx
BuildRequires:  mingw64-libconfuse
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  swig

%description
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package -n mingw32-%{name1}
Summary:        MinGW library to program and control the FTDI USB controller

%description -n mingw32-%{name1}
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%package -n mingw64-%{name1}
Summary:        MinGW library to program and control the FTDI USB controller

%description -n mingw64-%{name1}
A library (using libusb) to talk to FTDI's FT2232C,
FT232BM and FT245BM type chips including the popular bitbang mode.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name1}1-%{version}

%build
# TODO: Please submit an issue to upstream (rhbz#2380906)
export CMAKE_POLICY_VERSION_MINIMUM=3.5
%mingw_cmake -DSTATICLIBS=off -DFTDIPP=on -DPYTHON_BINDINGS=off -DDOCUMENTATION=on -DEXAMPLES=off .

%mingw_make %{?_smp_mflags}

%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -f $RPM_BUILD_ROOT/%{mingw32_libdir}/{libftdi1.a,libftdipp1.a}
rm -f $RPM_BUILD_ROOT/%{mingw64_libdir}/{libftdi1.a,libftdipp1.a}
rm -f $RPM_BUILD_ROOT/%{mingw32_datadir}/doc/libftdi1/example.conf
rm -f $RPM_BUILD_ROOT/%{mingw64_datadir}/doc/libftdi1/example.conf
rm -rf $RPM_BUILD_ROOT/build_win32/doc/html
rm -rf $RPM_BUILD_ROOT/build_win64/doc/html
rm -rf $RPM_BUILD_ROOT/build_win32/examples
rm -rf $RPM_BUILD_ROOT/build_win64/examples

%files -n mingw32-%{name1}
%license COPYING.LIB COPYING.GPL LICENSE
%doc AUTHORS ChangeLog README
%{mingw32_bindir}/ftdi_eeprom.exe      
%{mingw32_bindir}/libftdi1-config
%{mingw32_bindir}/libftdi1.dll
%{mingw32_bindir}/libftdipp1.dll
%{mingw32_includedir}/libftdi1
%{mingw32_libdir}/libftdi1.dll.a
%{mingw32_libdir}/libftdipp1.dll.a
%{mingw32_libdir}/cmake/libftdi1
%{mingw32_libdir}/pkgconfig/libftdi1.pc
%{mingw32_libdir}/pkgconfig/libftdipp1.pc

%files -n mingw64-%{name1}
%license COPYING.LIB COPYING.GPL LICENSE
%doc AUTHORS ChangeLog README
%{mingw64_bindir}/ftdi_eeprom.exe      
%{mingw64_bindir}/libftdi1-config
%{mingw64_bindir}/libftdi1.dll
%{mingw64_bindir}/libftdipp1.dll
%{mingw64_includedir}/libftdi1
%{mingw64_libdir}/libftdi1.dll.a
%{mingw64_libdir}/libftdipp1.dll.a
%{mingw64_libdir}/cmake/libftdi1
%{mingw64_libdir}/pkgconfig/libftdi1.pc
%{mingw64_libdir}/pkgconfig/libftdipp1.pc

%changelog
%autochangelog
