%global source0_hash 075920b826834ac4ddf97661cc73491047855859affd671d52079c6867c1c6c0

%{?mingw_package_header}

# Build the programs like cjpeg, etc.
# https://bugzilla.redhat.com/show_bug.cgi?id=467401#c7
%global build_programs 0

Name:           mingw-libjpeg-turbo
Version:        3.1.3
Release:        1%{?dist}
Summary:        MinGW Windows Libjpeg-turbo library

License:        Zlib AND BSD-3-Clause AND MIT AND IJG
URL:            https://github.com/libjpeg-turbo/libjpeg-turbo
Source0:        https://github.com/libjpeg-turbo/libjpeg-turbo/releases/download/3.1.3/libjpeg-turbo-3.1.3.tar.gz
#Patch1:         libjpeg-turbo-CET.patch

BuildArch:      noarch

BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils

BuildRequires:  nasm
BuildRequires:  cmake
BuildRequires:  make


%description
MinGW Windows cross compiled Libjpeg-turbo library.


# Win32
%package -n mingw32-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      mingw32-libjpeg < 7-4
Provides:       mingw32-libjpeg = 7-4

%description -n mingw32-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.


%package -n mingw32-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       mingw32-libjpeg-turbo = %{version}-%{release}
Obsoletes:      mingw32-libjpeg-static < 7-4
Provides:       mingw32-libjpeg-static = 7-4

%description -n mingw32-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.


%package -n mingw32-turbojpeg
Summary:        MinGW Windows turbojpeg library

%description -n mingw32-turbojpeg
MinGW Windows cross compiled turbojpeg library.


%package -n mingw32-turbojpeg-static
Summary:        Static version of the MinGW Windows turbojpeg library
Requires:       mingw32-turbojpeg = %{version}-%{release}

%description -n mingw32-turbojpeg-static
Static version of the MinGW Windows turbojpeg library.


# Win64
%package -n mingw64-libjpeg-turbo
Summary:        MinGW Windows Libjpeg-turbo library
Obsoletes:      mingw64-libjpeg < 8a-2%{?dist}
Provides:       mingw64-libjpeg = 8a-2%{?dist}

%description -n mingw64-libjpeg-turbo
MinGW Windows cross compiled Libjpeg-turbo library.


%package -n mingw64-libjpeg-turbo-static
Summary:        Static version of the MinGW Windows Libjpeg-turbo library
Requires:       mingw64-libjpeg-turbo = %{version}-%{release}
Obsoletes:      mingw64-libjpeg-static < 8a-2%{?dist}
Provides:       mingw64-libjpeg-static = 8a-2%{?dist}

%description -n mingw64-libjpeg-turbo-static
Static version of the MinGW Windows cross compiled Libjpeg-turbo library.


%package -n mingw64-turbojpeg
Summary:        MinGW Windows turbojpeg library

%description -n mingw64-turbojpeg
MinGW Windows cross compiled turbojpeg library.


%package -n mingw64-turbojpeg-static
Summary:        Static version of the MinGW Windows turbojpeg library
Requires:       mingw64-turbojpeg = %{version}-%{release}

%description -n mingw64-turbojpeg-static
Static version of the MinGW Windows turbojpeg library.


%{?mingw_debug_package}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n libjpeg-turbo-%{version} -p1


%build
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install

# Remove manual pages and docs which duplicate Fedora native.
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}

# The CMake build system also installed some docs
rm -rf %{buildroot}%{mingw32_prefix}/doc
rm -rf %{buildroot}%{mingw64_prefix}/doc

# Remove win32 native binaries if wanted
%if %build_programs == 0
rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe
%endif

# Fix perms
chmod -x README.md


# Win32
%files -n mingw32-libjpeg-turbo
%license LICENSE.md
%doc README.* ChangeLog.md
%if %build_programs
%{mingw32_bindir}/*.exe
%endif
%{mingw32_bindir}/libjpeg-62.dll
%{mingw32_includedir}/jconfig.h
%{mingw32_includedir}/jerror.h
%{mingw32_includedir}/jmorecfg.h
%{mingw32_includedir}/jpeglib.h
%{mingw32_libdir}/cmake/libjpeg-turbo/
%{mingw32_libdir}/libjpeg.dll.a
%{mingw32_libdir}/pkgconfig/libjpeg.pc

%files -n mingw32-libjpeg-turbo-static
%{mingw32_libdir}/libjpeg.a

%files -n mingw32-turbojpeg
%{mingw32_bindir}/libturbojpeg.dll
%{mingw32_includedir}/turbojpeg.h
%{mingw32_libdir}/libturbojpeg.dll.a
%{mingw32_libdir}/pkgconfig/libturbojpeg.pc

%files -n mingw32-turbojpeg-static
%{mingw32_libdir}/libturbojpeg.a

# Win64
%files -n mingw64-libjpeg-turbo
%license LICENSE.md
%doc README.* ChangeLog.md
%if %build_programs
%{mingw64_bindir}/*.exe
%endif
%{mingw64_bindir}/libjpeg-62.dll
%{mingw64_includedir}/jconfig.h
%{mingw64_includedir}/jerror.h
%{mingw64_includedir}/jmorecfg.h
%{mingw64_includedir}/jpeglib.h
%{mingw64_libdir}/cmake/libjpeg-turbo/
%{mingw64_libdir}/libjpeg.dll.a
%{mingw64_libdir}/pkgconfig/libjpeg.pc

%files -n mingw64-libjpeg-turbo-static
%{mingw64_libdir}/libjpeg.a

%files -n mingw64-turbojpeg
%{mingw64_bindir}/libturbojpeg.dll
%{mingw64_includedir}/turbojpeg.h
%{mingw64_libdir}/libturbojpeg.dll.a
%{mingw64_libdir}/pkgconfig/libturbojpeg.pc

%files -n mingw64-turbojpeg-static
%{mingw64_libdir}/libturbojpeg.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.1.3-1
- Prepare for Oreon 11 (RP1)
