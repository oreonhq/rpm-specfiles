%global source0_hash 32427e8c471ac095853212a37aef816c60b42052d4d9e48230bab3bdf2936ccc
%{?mingw_package_header}
Name:           mingw-freetype
Version:        2.14.1
Release:        1%{?dist}
Summary:        Free and portable font rendering engine
License:        FTL OR GPL-2.0-or-later
URL:            http://www.freetype.org
Source0:        http://download.savannah.gnu.org/releases/freetype/freetype-%{version}.tar.xz
Patch0:         freetype-2.3.0-enable-spr.patch
Patch1:         freetype-2.2.1-enable-valid.patch
Patch2:         freetype-2.10.0-internal-outline.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-bzip2
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-libpng
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-bzip2
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-libpng
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows Freetype library.

# Win32
%package -n mingw32-freetype
Summary:        Free and portable font rendering engine
%description -n mingw32-freetype
MinGW Windows Freetype library.

%package -n mingw32-freetype-static
Summary:        Static version of the MinGW Windows Freetype library
Requires:       mingw32-freetype = %{version}-%{release}
%description -n mingw32-freetype-static
Static version of the MinGW Windows Freetype library.

# Win64
%package -n mingw64-freetype
Summary:        Free and portable font rendering engine
%description -n mingw64-freetype
MinGW Windows Freetype library.

%package -n mingw64-freetype-static
Summary:        Static version of the MinGW Windows Freetype library
Requires:       mingw64-freetype = %{version}-%{release}
%description -n mingw64-freetype-static
Static version of the MinGW Windows Freetype library.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir freetype-%{version}
%oreon_prep
%build

%mingw_configure \
           --enable-static \
           --enable-shared \
           --with-zlib=yes \
           --with-bzip2=yes \
           --with-png=yes \
           --enable-freetype-config \
           --with-harfbuzz=no
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
rm -rf %{buildroot}%{mingw32_mandir} %{buildroot}%{mingw64_mandir}
%oreon_autofiles mingw32-freetype usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-freetype-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-freetype usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-freetype-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-freetype -f %{oreon_filedir}/mingw32-freetype.list
%files -n mingw32-freetype-static -f %{oreon_filedir}/mingw32-freetype-static.list
%files -n mingw64-freetype -f %{oreon_filedir}/mingw64-freetype.list
%files -n mingw64-freetype-static -f %{oreon_filedir}/mingw64-freetype-static.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.14.1-2
- Prepare for Oreon 11 (RP1)
