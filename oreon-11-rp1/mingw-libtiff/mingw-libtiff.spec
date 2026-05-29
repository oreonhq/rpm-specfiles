%global source0_hash b92017489bdc1db3a4c97191aa4b75366673cb746de0dce5d7a749d5954681ba

%{?mingw_package_header}

Summary:        MinGW Windows port of the LibTIFF library
Name:           mingw-libtiff
Version:        4.7.1
Release:        2%{?dist}
License:        libtiff
URL:            http://www.simplesystems.org/libtiff/
Source:        https://download.osgeo.org/libtiff/tiff-4.7.1.tar.xz

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  mingw32-zlib
BuildRequires:  mingw32-libjpeg-turbo
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-binutils

BuildRequires:  mingw64-zlib
BuildRequires:  mingw64-libjpeg-turbo
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-binutils


%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.


# Win32
%package -n mingw32-libtiff
Summary:        MinGW Windows port of the LibTIFF library

%description -n mingw32-libtiff
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package -n mingw32-libtiff-static
Summary:        Static version of the MinGW Windows LibTIFF library
Requires:       mingw32-libtiff = %{version}-%{release}

%description -n mingw32-libtiff-static
Static version of the MinGW Windows LibTIFF library.

# Win64
%package -n mingw64-libtiff
Summary:        MinGW Windows port of the LibTIFF library

%description -n mingw64-libtiff
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package -n mingw64-libtiff-static
Summary:        Static version of the MinGW Windows LibTIFF library
Requires:       mingw64-libtiff = %{version}-%{release}

%description -n mingw64-libtiff-static
Static version of the MinGW Windows LibTIFF library.


%{?mingw_debug_package}


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n tiff-%{version}


%build
export MINGW32_CFLAGS="%{mingw32_cflags} -fno-strict-aliasing"
export MINGW64_CFLAGS="%{mingw64_cflags} -fno-strict-aliasing"
%mingw_configure --enable-static --enable-shared --enable-ld-version-script
%mingw_make %{?_smp_mflags}


%install
%mingw_make_install DESTDIR=%{buildroot}

# remove docs
rm -rf %{buildroot}%{mingw32_datadir}/doc
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_datadir}/doc
rm -rf %{buildroot}%{mingw64_mandir}

# remove binaries
rm -f %{buildroot}%{mingw32_bindir}/*.exe
rm -f %{buildroot}%{mingw64_bindir}/*.exe

# Drop all .la files
find %{buildroot} -name "*.la" -delete


# Win32
%files -n mingw32-libtiff
%doc README.md RELEASE-DATE VERSION TODO ChangeLog
%license LICENSE.md
%{mingw32_bindir}/libtiff-6.dll
%{mingw32_bindir}/libtiffxx-6.dll
%{mingw32_includedir}/*
%{mingw32_libdir}/libtiff.dll.a
%{mingw32_libdir}/libtiffxx.dll.a
%{mingw32_libdir}/pkgconfig/libtiff-4.pc

%files -n mingw32-libtiff-static
%{mingw32_libdir}/libtiff.a
%{mingw32_libdir}/libtiffxx.a

# Win64
%files -n mingw64-libtiff
%doc README.md RELEASE-DATE VERSION TODO ChangeLog
%license LICENSE.md
%{mingw64_bindir}/libtiff-6.dll
%{mingw64_bindir}/libtiffxx-6.dll
%{mingw64_includedir}/*
%{mingw64_libdir}/libtiff.dll.a
%{mingw64_libdir}/libtiffxx.dll.a
%{mingw64_libdir}/pkgconfig/libtiff-4.pc

%files -n mingw64-libtiff-static
%{mingw64_libdir}/libtiff.a
%{mingw64_libdir}/libtiffxx.a


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.7.1-2
- Prepare for Oreon 11 (RP1)
