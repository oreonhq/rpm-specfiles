%global source0_hash a74a2e68303d3b9219f82318f935b28c5c4abd7f2c9f7dbf8faa4997c9038305

%{?mingw_package_header}

%global pkgname LibRaw

Name:          mingw-%{pkgname}
Version:       0.21.5
Release:       2%{?dist}
Summary:       Library for reading RAW files obtained from digital photo cameras

# LibRaw base package is dual licensed (actually triple licensed LGPLv2+, CDDL, LibRaw Software License)
# LibRaw-%%{version}/internal/dcb_demosaicing.c is BSD (3 clause)
License:       BSD-3-Clause AND (CDDL-1.0 OR LGPL-2.1-only)
BuildArch:     noarch
URL:           http://www.libraw.org
Source0:       http://www.libraw.org/data/%{pkgname}-%{version}.tar.gz

BuildRequires: make
BuildRequires: autoconf automake libtool

BuildRequires: mingw32-filesystem >= 95
BuildRequires: mingw32-gcc-c++
BuildRequires: mingw32-lcms2
BuildRequires: mingw32-jasper

BuildRequires: mingw64-filesystem >= 95
BuildRequires: mingw64-gcc-c++
BuildRequires: mingw64-lcms2
BuildRequires: mingw64-jasper

Provides: bundled(dcraw)

%description
MinGW Windows %{pkgname} library.

%package -n mingw32-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw32-%{pkgname}
%{summary}.

%package -n mingw32-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-static
%{summary}.

%package -n mingw32-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw32-%{pkgname} = %{version}-%{release}

%description -n mingw32-%{pkgname}-tools
%{summary}.

%package -n mingw64-%{pkgname}
Summary:       MinGW Windows %{pkgname} library

%description -n mingw64-%{pkgname}
%{summary}.

%package -n mingw64-%{pkgname}-static
Summary:       Static version of the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-static
%{summary}.

%package -n mingw64-%{pkgname}-tools
Summary:       Tools for the MinGW Windows %{pkgname} library
Requires:      mingw64-%{pkgname} = %{version}-%{release}

%description -n mingw64-%{pkgname}-tools
%{summary}.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{pkgname}-%{version}

# Remove executable bit on license files
chmod -x LICENSE.CDDL
chmod -x LICENSE.LGPL

%build
autoreconf -ifv
%mingw_configure --enable-jasper --enable-lcms CPPFLAGS=-DLIBRAW_NODLL
%mingw_make_build

%install
%mingw_make_install

# Delete *.la files
find %{buildroot} -name '*.la' -delete

# Install doc through %%doc
rm -rf %{buildroot}%{mingw32_datadir}
rm -rf %{buildroot}%{mingw64_datadir}

%files -n mingw32-%{pkgname}
%license LICENSE.CDDL LICENSE.LGPL COPYRIGHT
%{mingw32_bindir}/libraw-23.dll
%{mingw32_bindir}/libraw_r-23.dll
%{mingw32_includedir}/libraw/
%{mingw32_libdir}/libraw.dll.a
%{mingw32_libdir}/libraw_r.dll.a
%{mingw32_libdir}/pkgconfig/libraw.pc
%{mingw32_libdir}/pkgconfig/libraw_r.pc

%files -n mingw32-%{pkgname}-static
%{mingw32_libdir}/libraw_r.a
%{mingw32_libdir}/libraw.a

%files -n mingw32-%{pkgname}-tools
%{mingw32_bindir}/*.exe

%files -n mingw64-%{pkgname}
%license LICENSE.CDDL LICENSE.LGPL COPYRIGHT
%{mingw64_bindir}/libraw-23.dll
%{mingw64_bindir}/libraw_r-23.dll
%{mingw64_includedir}/libraw/
%{mingw64_libdir}/libraw.dll.a
%{mingw64_libdir}/libraw_r.dll.a
%{mingw64_libdir}/pkgconfig/libraw.pc
%{mingw64_libdir}/pkgconfig/libraw_r.pc

%files -n mingw64-%{pkgname}-static
%{mingw64_libdir}/libraw_r.a
%{mingw64_libdir}/libraw.a

%files -n mingw64-%{pkgname}-tools
%{mingw64_bindir}/*.exe

%changelog
%autochangelog
