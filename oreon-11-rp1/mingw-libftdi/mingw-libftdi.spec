%global source0_hash 7c7091e9c86196148bd41177b4590dccb1510bfe6cea5bf7407ff194482eb049
%?mingw_package_header
%global name1 libftdi
Name:           mingw-%{name1}
Version:        1.5
Release:        1%{?dist}
Summary:        MinGW library to program and control the FTDI USB controller
License:        LicenseRef-Callaway-LGPLv2 AND GPL-2.0-only
URL:            https://www.intra2net.com/en/developer/libftdi/
Source0:        https://www.intra2net.com/en/developer/%{name1}/download/%{name1}1-%{version}.tar.bz2
Patch0:         libftdi-1.5-fix_pkgconfig_path.patch
Patch1:         libftdi-1.5-no-distutils.patch
Patch2:         libftdi-1.5-cmake-deps.patch
Patch3:         libftdi-1.5-swig-4.3.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-boost
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-libconfuse
BuildRequires:  mingw32-libusbx
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-boost
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-libconfuse
BuildRequires:  mingw64-libusbx
BuildRequires:  swig
# /oreon:deps
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
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libftdi -f %{oreon_filedir}/mingw32-libftdi.list
%files -n mingw64-libftdi -f %{oreon_filedir}/mingw64-libftdi.list

%changelog

%autochangelog
