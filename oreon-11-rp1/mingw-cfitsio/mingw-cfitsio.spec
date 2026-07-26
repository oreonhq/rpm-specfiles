%global source0_hash fad44fff274fdda5ffcc0c0fff3bc3c596362722b9292fc8944db91187813600

%{?mingw_package_header}

%global pkgname cfitsio

Name:          mingw-%{pkgname}
# NOTE: sync SOVER in cfitsio_build.patch with the one in configure.in
Version:       4.6.3
Release:       2%{?dist}
Summary:       MinGW Windows CFITSIO library

License:       CFITSIO
BuildArch:     noarch
URL:           https://heasarc.gsfc.nasa.gov/fitsio/
Source0:       https://heasarc.gsfc.nasa.gov/FTP/software/fitsio/c/%{pkgname}-%{version}.tar.gz
# Install headers to include/cfitsio
Patch0:        cfitsio_cmake.patch

BuildRequires: make
BuildRequires: cmake

BuildRequires: mingw32-filesystem
BuildRequires: mingw32-curl
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-zlib

BuildRequires: mingw64-filesystem
BuildRequires: mingw64-curl
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-zlib

%description
MinGW Windows CFITSIO library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows CFITSIO library

%description -n mingw32-%{pkgname}
MinGW Windows CFITSIO library.

%package -n mingw32-%{pkgname}-tools
Summary:       MinGW Windows CFITSIO library

%description -n mingw32-%{pkgname}-tools
MinGW Windows CFITSIO library.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows CFITSIO library

%description -n mingw64-%{pkgname}
MinGW Windows CFITSIO library.

%package -n mingw64-%{pkgname}-tools
Summary:       MinGW Windows CFITSIO library

%description -n mingw64-%{pkgname}-tools
MinGW Windows CFITSIO library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

%build
%mingw_cmake -DUTILS=ON -DCMAKE_DLL_NAME_WITH_SOVERSION=ON -DTESTS=OFF
%mingw_make_build

%install
%mingw_make_install

%files -n mingw32-%{pkgname}
%license licenses/License.txt
%{mingw32_bindir}/libcfitsio-10.dll
%{mingw32_libdir}/libcfitsio.dll.a
%{mingw32_libdir}/pkgconfig/cfitsio.pc
%{mingw32_libdir}/cmake/%{pkgname}/
%{mingw32_includedir}/cfitsio/

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/fitscopy.exe
%{mingw32_bindir}/fitsverify.exe
%{mingw32_bindir}/fpack.exe
%{mingw32_bindir}/funpack.exe
%{mingw32_bindir}/imcopy.exe
%{mingw32_bindir}/speed.exe

%files -n mingw64-%{pkgname}
%license licenses/License.txt
%{mingw64_bindir}/libcfitsio-10.dll
%{mingw64_libdir}/libcfitsio.dll.a
%{mingw64_libdir}/pkgconfig/cfitsio.pc
%{mingw64_libdir}/cmake/%{pkgname}/
%{mingw64_includedir}/cfitsio/

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/fitscopy.exe
%{mingw64_bindir}/fitsverify.exe
%{mingw64_bindir}/fpack.exe
%{mingw64_bindir}/funpack.exe
%{mingw64_bindir}/imcopy.exe
%{mingw64_bindir}/speed.exe

%changelog
%autochangelog
