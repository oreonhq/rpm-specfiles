%global source0_hash 9015d109ec00bb9ae1a384b172bf2fc1dff41e2c66e5a9eeddf933af9db37f5a

%{?mingw_package_header}

Name:           mingw-libarchive
Version:        3.5.1
Release:        14%{?dist}
Summary:        MinGW package for handling streaming archive formats

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.libarchive.org/
Source0:        http://www.libarchive.org/downloads/libarchive-%{version}.tar.gz
# Fix detection of OpenSSL
Patch0:         libarchive-mingw-openssl.patch

BuildArch:      noarch

BuildRequires: make
BuildRequires:  mingw32-filesystem >= 95
BuildRequires:  mingw64-filesystem >= 95
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-gcc
BuildRequires:  mingw32-binutils
BuildRequires:  mingw64-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw64-nettle
BuildRequires:  mingw32-openssl
BuildRequires:  mingw64-openssl
BuildRequires:  mingw32-xz-libs
BuildRequires:  mingw64-xz-libs
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-zlib
BuildRequires:  automake autoconf libtool

%description
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

# Mingw32
%package -n mingw32-libarchive
Summary:        MinGW package for handling streaming archive formats

%description -n mingw32-libarchive
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package -n mingw32-libarchive-static
Summary:        Static version of the MinGW libarchive library
Requires:       mingw32-libarchive = %{version}-%{release}

%description -n mingw32-libarchive-static
Static version of the MinGW libarchive library.

%package -n     mingw32-bsdtar
Summary:        MinGW package for bsdtar utility

%description -n mingw32-bsdtar
The bsdtar package contains standalone bsdtar utility split off regular
libarchive packages.

%package -n     mingw32-bsdcat
Summary:        MinGW package for bsdcat utility

%description -n mingw32-bsdcat
The bsdcat package contains standalone bsdcat utility split off regular
libarchive packages.

%package -n     mingw32-bsdcpio
Summary:        MinGW package for bsdcpio utility

%description -n mingw32-bsdcpio
The bsdcpio package contains standalone bsdcpio utility split off regular
libarchive packages.

# Mingw64
%package -n mingw64-libarchive
Summary:        MinGW package for handling streaming archive formats

%description -n mingw64-libarchive
Libarchive is a programming library that can create and read several different
streaming archive formats, including most popular tar variants, several cpio
formats, and both BSD and GNU ar variants. It can also write shar archives and
read ISO9660 CDROM images and ZIP archives.

%package -n mingw64-libarchive-static
Summary:        Static version of the MinGW libarchive library
Requires:       mingw64-libarchive = %{version}-%{release}

%description -n mingw64-libarchive-static
Static version of the MinGW libarchive library.

%package -n     mingw64-bsdtar
Summary:        MinGW package for bsdtar utility

%description -n mingw64-bsdtar
The bsdtar package contains standalone bsdtar utility split off regular
libarchive packages.

%package -n     mingw64-bsdcat
Summary:        MinGW package for bsdcat utility

%description -n mingw64-bsdcat
The bsdcat package contains standalone bsdcat utility split off regular
libarchive packages.

%package -n     mingw64-bsdcpio
Summary:        MinGW package for bsdcpio utility

%description -n mingw64-bsdcpio
The bsdcpio package contains standalone bsdcpio utility split off regular
libarchive packages.

%?mingw_debug_package

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libarchive-%{version}
%patch -P0 -p1 -b.openssl

%build
build/autogen.sh
# Disable CNG to support wider range of Windows versions
%mingw_configure --without-cng --with-nettle
%mingw_make %{?_smp_mflags} V=1

%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name cpio.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name mtree.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name tar.5 -exec rm -f {} ';'

# Remove documentation which duplicates that found in the native package.
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share

# Win32
%files -n mingw32-libarchive
%license COPYING
%doc NEWS
%{mingw32_bindir}/libarchive-13.dll
%{mingw32_includedir}/archive.h
%{mingw32_includedir}/archive_entry.h
%{mingw32_libdir}/libarchive.dll.a
%{mingw32_libdir}/pkgconfig/libarchive.pc

%files -n mingw32-libarchive-static
%{mingw32_libdir}/libarchive.a

%files -n mingw32-bsdtar
%{mingw32_bindir}/bsdtar.exe

%files -n mingw32-bsdcat
%{mingw32_bindir}/bsdcat.exe

%files -n mingw32-bsdcpio
%{mingw32_bindir}/bsdcpio.exe

# Win64
%files -n mingw64-libarchive
%license COPYING
%doc NEWS
%{mingw64_bindir}/libarchive-13.dll
%{mingw64_includedir}/archive.h
%{mingw64_includedir}/archive_entry.h
%{mingw64_libdir}/libarchive.dll.a
%{mingw64_libdir}/pkgconfig/libarchive.pc

%files -n mingw64-libarchive-static
%{mingw64_libdir}/libarchive.a

%files -n mingw64-bsdtar
%{mingw64_bindir}/bsdtar.exe

%files -n mingw64-bsdcat
%{mingw64_bindir}/bsdcat.exe

%files -n mingw64-bsdcpio
%{mingw64_bindir}/bsdcpio.exe

%changelog
%autochangelog
