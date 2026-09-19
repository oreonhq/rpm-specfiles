%global source0_hash 987e8c8b4afcff87553833b6f0fa255b5556a0ecc617b45ee1882e10c1b5ec14

%{?mingw_package_header}

Name:           mingw-jasper
Version:        4.2.8
Release:        2%{?dist}
Summary:        MinGW Windows Jasper library

License:        JasPer-2.0

URL:            http://www.ece.uvic.ca/~frodo/jasper/
Source0:        https://github.com/mdadams/jasper/archive/version-%{version}/jasper-%{version}.tar.gz

# MinGW-specific patches.
# Version the library
Patch1:         jasper-libversion.patch
# Add some missing exports, needed by mingw-gdal
Patch2:         jasper-exports.patch

BuildArch:      noarch

BuildRequires:  make

BuildRequires:  cmake
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libjpeg

BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libjpeg

%description
MinGW Windows Jasper library.

%package -n mingw32-jasper
Summary:        MinGW Windows Jasper library

%description -n mingw32-jasper
MinGW Windows Jasper library.

%package -n mingw32-jasper-static
Summary:        Static version of the MinGW Windows Jasper library
Requires:       mingw32-jasper = %{version}-%{release}

%description -n mingw32-jasper-static
Static version of the MinGW Windows Jasper library.

%package -n mingw64-jasper
Summary:        MinGW Windows Jasper library

%description -n mingw64-jasper
MinGW Windows Jasper library.

%package -n mingw64-jasper-static
Summary:        Static version of the MinGW Windows Jasper library
Requires:       mingw64-jasper = %{version}-%{release}

%description -n mingw64-jasper-static
Static version of the MinGW Windows Jasper library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n jasper-version-%{version}

%build
jasper_cmake_args="-DJAS_ENABLE_DOC=OFF -DJAS_ENABLE_OPENGL=OFF -DJAS_ENABLE_AUTOMATIC_DEPENDENCIES=OFF -DJAS_STDC_VERSION=201112L -DALLOW_IN_SOURCE_BUILD=ON"
# Build static
MINGW_BUILDDIR_SUFFIX=-static %mingw_cmake -DJAS_ENABLE_SHARED=OFF $jasper_cmake_args
MINGW_BUILDDIR_SUFFIX=-static %mingw_make_build
# Build shared
MINGW_BUILDDIR_SUFFIX=-shared %mingw_cmake -DJAS_ENABLE_SHARED=ON $jasper_cmake_args
MINGW_BUILDDIR_SUFFIX=-shared %mingw_make_build

%install
MINGW_BUILDDIR_SUFFIX=-static %mingw_make_install
MINGW_BUILDDIR_SUFFIX=-shared %mingw_make_install

# Remove documentation
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
rm -rf %{buildroot}%{mingw32_docdir}
rm -rf %{buildroot}%{mingw64_docdir}
rmdir %{buildroot}%{mingw32_datadir}
rmdir %{buildroot}%{mingw64_datadir}

%files -n mingw32-jasper
%license COPYRIGHT.txt LICENSE.txt
%{mingw32_bindir}/imgcmp.exe
%{mingw32_bindir}/imginfo.exe
%{mingw32_bindir}/jasper.exe
%{mingw32_bindir}/libjasper-7.dll
%{mingw32_libdir}/libjasper.dll.a
%{mingw32_libdir}/pkgconfig/jasper.pc
%{mingw32_includedir}/jasper/

%files -n mingw32-jasper-static
%{mingw32_libdir}/libjasper.a

%files -n mingw64-jasper
%license COPYRIGHT.txt LICENSE.txt
%{mingw64_bindir}/imgcmp.exe
%{mingw64_bindir}/imginfo.exe
%{mingw64_bindir}/jasper.exe
%{mingw64_bindir}/libjasper-7.dll
%{mingw64_libdir}/libjasper.dll.a
%{mingw64_libdir}/pkgconfig/jasper.pc
%{mingw64_includedir}/jasper/

%files -n mingw64-jasper-static
%{mingw64_libdir}/libjasper.a

%changelog
%autochangelog
