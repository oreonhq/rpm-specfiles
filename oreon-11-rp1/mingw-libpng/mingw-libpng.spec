%global source0_hash 28eb403f51f0f7405249132cecfe82ea5c0ef97f1b32c5a65828814ae0d34775
%{?mingw_package_header}
Name:           mingw-libpng
Version:        1.6.58
Release:        1%{?dist}
Summary:        MinGW Windows Libpng library
License:        Zlib
URL:            http://www.libpng.org/pub/png/
Source0:        https://downloads.sourceforge.net/libpng/libpng-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-zlib
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-zlib
# /oreon:deps
%description
MinGW Windows Libpng library.

# Win32
%package -n mingw32-libpng
Summary:        MinGW Windows Libpng library
Requires:       pkgconfig
%description -n mingw32-libpng
MinGW Windows Libpng library.

%package -n mingw32-libpng-static
Summary:        Static version of MinGW Windows Libpng library
Requires:       mingw32-libpng = %{version}-%{release}
%description -n mingw32-libpng-static
MinGW Windows Libpng library.

This package contains static cross-compiled libraries.

# Win64
%package -n mingw64-libpng
Summary:        MinGW Windows Libpng library
Requires:       pkgconfig
%description -n mingw64-libpng
MinGW Windows Libpng library.

%package -n mingw64-libpng-static
Summary:        Static version of MinGW Windows Libpng library
Requires:       mingw64-libpng = %{version}-%{release}
%description -n mingw64-libpng-static
MinGW Windows Libpng library.

This package contains static cross-compiled libraries.

%{?mingw_debug_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir libpng-%{version}
%oreon_prep
%build

%mingw_configure
%mingw_make_build
%install
%mingw_make_install
find %{buildroot} -name "*.la" -delete
rm -rf %{buildroot}%{mingw32_mandir}
rm -rf %{buildroot}%{mingw64_mandir}
%oreon_autofiles mingw32-libpng usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libpng-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libpng usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libpng-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libpng -f %{oreon_filedir}/mingw32-libpng.list
%files -n mingw32-libpng-static -f %{oreon_filedir}/mingw32-libpng-static.list
%files -n mingw64-libpng -f %{oreon_filedir}/mingw64-libpng.list
%files -n mingw64-libpng-static -f %{oreon_filedir}/mingw64-libpng-static.list

%changelog

%autochangelog
