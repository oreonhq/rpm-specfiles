%global source0_hash 50435aec6fdd976934b791e808993160113ad19ca53a5634a9b64ccbe55874cc

%?mingw_package_header

Name:           mingw-cairomm
Version:        1.12.0
Release:        26%{?dist}
Summary:        MinGW Windows C++ API for the cairo graphics library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.cairographics.org
Source0:        http://www.cairographics.org/releases/cairomm-%{version}.tar.gz
Patch0:         0001-Fix-the-build-with-MinGW-headers.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-cairo
BuildRequires:  mingw64-cairo
BuildRequires:  mingw32-libsigc++20
BuildRequires:  mingw64-libsigc++20

%description
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the 
Standard Template Library where it makes sense.

# Win32
%package -n mingw32-cairomm
Summary:        MinGW Windows C++ API for the cairo graphics library

%description -n mingw32-cairomm
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the
Standard Template Library where it makes sense.

%package -n mingw32-cairomm-static
Summary:        Static cross compiled version of the cairomm library
Requires:       mingw32-cairomm = %{version}-%{release}

%description -n mingw32-cairomm-static
Static cross compiled version of the cairomm library.

%package -n mingw64-cairomm
Summary:        MinGW Windows C++ API for the cairo graphics library

%description -n mingw64-cairomm
Cairomm is the C++ API for the cairo graphics library. It offers all the power
of cairo with an interface familiar to C++ developers, including use of the
Standard Template Library where it makes sense.

%package -n mingw64-cairomm-static
Summary:        Static cross compiled version of the cairomm library
Requires:       mingw64-cairomm = %{version}-%{release}

%description -n mingw64-cairomm-static
Static cross compiled version of the cairomm library.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n cairomm-%{version}
%patch -P0 -p1

%build
export lt_cv_deplibs_check_method="pass_all"
%mingw_configure --enable-static --disable-documentation
%mingw_make %{?_smp_mflags}

%install
%mingw_make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{mingw32_datadir}/{devhelp,doc}
rm -rf $RPM_BUILD_ROOT/%{mingw64_datadir}/{devhelp,doc}
rm $RPM_BUILD_ROOT%{mingw32_libdir}/*.la
rm $RPM_BUILD_ROOT%{mingw64_libdir}/*.la

# Win32
%files -n mingw32-cairomm
%license COPYING
%{mingw32_bindir}/libcairomm-1.0-1.dll
%{mingw32_libdir}/libcairomm-1.0.dll.a
%{mingw32_libdir}/pkgconfig/cairomm-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-ft-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-pdf-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-png-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-ps-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-svg-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-win32-1.0.pc
%{mingw32_libdir}/pkgconfig/cairomm-win32-font-1.0.pc
%{mingw32_includedir}/cairomm-1.0
%{mingw32_libdir}/cairomm-1.0/

%files -n mingw32-cairomm-static
%{mingw32_libdir}/libcairomm-1.0.a

# Win64
%files -n mingw64-cairomm
%license COPYING
%{mingw64_bindir}/libcairomm-1.0-1.dll
%{mingw64_libdir}/libcairomm-1.0.dll.a
%{mingw64_libdir}/pkgconfig/cairomm-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-ft-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-pdf-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-png-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-ps-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-svg-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-win32-1.0.pc
%{mingw64_libdir}/pkgconfig/cairomm-win32-font-1.0.pc
%{mingw64_includedir}/cairomm-1.0
%{mingw64_libdir}/cairomm-1.0/

%files -n mingw64-cairomm-static
%{mingw64_libdir}/libcairomm-1.0.a

%changelog
%autochangelog
