%global source0_hash f5a6539059cf5e597dbeda37bfa4874b1e8dea063c8d93bf85a2b44af90a5bd4
%{?mingw_package_header}
Name:           mingw-libarchive
Version:        3.8.9
Release:        1%{?dist}
Summary:        MinGW package for handling streaming archive formats
License:        LicenseRef-Callaway-BSD
URL:            http://www.libarchive.org/
Source0:        http://www.libarchive.org/downloads/libarchive-%{version}.tar.gz
Patch0:         libarchive-mingw-openssl.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-nettle
BuildRequires:  mingw32-openssl
BuildRequires:  mingw32-xz-libs
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-nettle
BuildRequires:  mingw64-openssl
BuildRequires:  mingw64-xz-libs
BuildRequires:  mingw64-zlib
# /oreon:deps
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
%mingw_configure --without-cng --with-nettle
%mingw_make %{?_smp_mflags} V=1
%install
%mingw_make_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name cpio.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name mtree.5 -exec rm -f {} ';'
find $RPM_BUILD_ROOT -name tar.5 -exec rm -f {} ';'
rm -r $RPM_BUILD_ROOT/%{mingw32_prefix}/share
rm -r $RPM_BUILD_ROOT/%{mingw64_prefix}/share
%oreon_autofiles mingw32-libarchive usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libarchive-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-bsdtar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-bsdcat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-bsdcpio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libarchive usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libarchive-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-bsdtar usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-bsdcat usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-bsdcpio usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libarchive -f %{oreon_filedir}/mingw32-libarchive.list
%files -n mingw32-libarchive-static -f %{oreon_filedir}/mingw32-libarchive-static.list
%files -n mingw32-bsdtar -f %{oreon_filedir}/mingw32-bsdtar.list
%files -n mingw32-bsdcat -f %{oreon_filedir}/mingw32-bsdcat.list
%files -n mingw32-bsdcpio -f %{oreon_filedir}/mingw32-bsdcpio.list
%files -n mingw64-libarchive -f %{oreon_filedir}/mingw64-libarchive.list
%files -n mingw64-libarchive-static -f %{oreon_filedir}/mingw64-libarchive-static.list
%files -n mingw64-bsdtar -f %{oreon_filedir}/mingw64-bsdtar.list
%files -n mingw64-bsdcat -f %{oreon_filedir}/mingw64-bsdcat.list
%files -n mingw64-bsdcpio -f %{oreon_filedir}/mingw64-bsdcpio.list

%changelog

%autochangelog
