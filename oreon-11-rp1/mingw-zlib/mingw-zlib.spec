%global source0_hash d7a0654783a4da529d1bb793b7ad9c3318020af77667bcae35f95d0e42a792f3

%global mingw_build_ucrt64 1
%{?mingw_package_header}

Name:           mingw-zlib
Version:        1.3.2
Release:        1%{?dist}
Summary:        MinGW Windows zlib compression library

License:        Zlib
URL:            https://www.zlib.net/
Source0:        https://www.zlib.net/zlib-1.3.2.tar.xz
# Use UNIX naming convention for libraries
Patch0:         mingw-zlib-cmake.patch

BuildArch:      noarch

BuildRequires:  cmake
BuildRequires:  make

BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc

BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc

BuildRequires:  ucrt64-filesystem
BuildRequires:  ucrt64-gcc


%description
MinGW Windows zlib compression library.


# Win32
%package -n mingw32-zlib
Summary:        MinGW Windows zlib compression library for the win32 target

%description -n mingw32-zlib
MinGW Windows zlib compression library for the win32 target.


%package -n mingw32-zlib-static
Summary:        Static libraries for mingw32-zlib development.
Requires:       mingw32-zlib = %{version}-%{release}

%description -n mingw32-zlib-static
The mingw32-zlib-static package contains static library for mingw32-zlib development.


# Win64
%package -n mingw64-zlib
Summary:        MinGW Windows zlib compression library for the win64 target

%description -n mingw64-zlib
MinGW Windows zlib compression library for the win64 target.

%package -n mingw64-zlib-static
Summary:        Static libraries for mingw64-zlib development
Requires:       mingw64-zlib = %{version}-%{release}

%description -n mingw64-zlib-static
The mingw64-zlib-static package contains static library for mingw64-zlib development.


# UCRT64
%package -n ucrt64-zlib
Summary:        MinGW Windows zlib compression library for the ucrt64 target

%description -n ucrt64-zlib
MinGW Windows zlib compression library for the ucrt64 target.

%package -n ucrt64-zlib-static
Summary:        Static libraries for ucrt64-zlib development
Requires:       ucrt64-zlib = %{version}-%{release}

%description -n ucrt64-zlib-static
The ucrt64-zlib-static package contains static library for ucrt64-zlib development.


%{?mingw_debug_package}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n zlib-%{version}


%build
MINGW32_CMAKE_ARGS=-DINSTALL_PKGCONFIG_DIR=%{mingw32_libdir}/pkgconfig \
MINGW64_CMAKE_ARGS=-DINSTALL_PKGCONFIG_DIR=%{mingw64_libdir}/pkgconfig \
UCRT64_CMAKE_ARGS=-DINSTALL_PKGCONFIG_DIR=%{ucrt64_libdir}/pkgconfig \
%mingw_cmake
%mingw_make_build


%install
%mingw_make_install

# Drop the man pages
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{ucrt64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rm -rf %{buildroot}%{ucrt64_docdir}


# Win32
%files -n mingw32-zlib
%{mingw32_includedir}/zconf.h
%{mingw32_includedir}/zlib.h
%{mingw32_libdir}/libz.dll.a
%{mingw32_bindir}/zlib1.dll
%{mingw32_libdir}/pkgconfig/zlib.pc
%{mingw32_libdir}/cmake/zlib/

%files -n mingw32-zlib-static
%{mingw32_libdir}/libz.a

# Win64
%files -n mingw64-zlib
%{mingw64_includedir}/zconf.h
%{mingw64_includedir}/zlib.h
%{mingw64_libdir}/libz.dll.a
%{mingw64_bindir}/zlib1.dll
%{mingw64_libdir}/pkgconfig/zlib.pc
%{mingw64_libdir}/cmake/zlib/

%files -n mingw64-zlib-static
%{mingw64_libdir}/libz.a

# UCRT64
%files -n ucrt64-zlib
%{ucrt64_includedir}/zconf.h
%{ucrt64_includedir}/zlib.h
%{ucrt64_libdir}/libz.dll.a
%{ucrt64_bindir}/zlib1.dll
%{ucrt64_libdir}/pkgconfig/zlib.pc
%{ucrt64_libdir}/cmake/zlib/

%files -n ucrt64-zlib-static
%{ucrt64_libdir}/libz.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.2-1
- Prepare for Oreon 11 (RP1)
