%global source0_hash 767ec234ae7aa684695b3a735548224888132e063f92db585759b422570621d4
%{?mingw_package_header}
Name:           mingw-libcroco
Version:        0.6.13
Release:        1%{?dist}
Summary:        A CSS2 parsing library for MinGW
License:        LicenseRef-Callaway-LGPLv2
URL:            http://ftp.gnome.org/pub/GNOME/sources/libcroco/
Source0:        http://download.gnome.org/sources/libcroco/0.6/libcroco-%{version}.tar.xz
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-glib2
BuildRequires:  mingw32-libxml2
BuildRequires:  mingw32-pkg-config
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-glib2
BuildRequires:  mingw64-libxml2
BuildRequires:  mingw64-pkg-config
# /oreon:deps
%description
CSS2 parsing and manipulation library for GNOME

This is the MinGW version of this library.

%package -n mingw32-libcroco
Summary:        MinGW A CSS2 parsing library
Requires:       pkgconfig
%description -n mingw32-libcroco
This package contains the header files and libraries needed to develop MinGW
applications that use libcroco.

%package -n mingw32-libcroco-static
Summary:        MinGW static A CSS2 parsing library
Requires:       mingw32-libcroco = %{version}-%{release}
%description -n mingw32-libcroco-static
This package contains the static libraries needed to develop MinGW
applications that use libcroco-0.6.

%package -n mingw64-libcroco
Summary:        MinGW A CSS2 parsing library
Requires:       pkgconfig
%description -n mingw64-libcroco
This package contains the header files and libraries needed to develop MinGW
applications that use libcroco-0.6.

%package -n mingw64-libcroco-static
Summary:        MinGW static A CSS2 parsing library
Requires:       mingw64-libcroco = %{version}-%{release}
%description -n mingw64-libcroco-static
This package contains the static libraries needed to develop MinGW
applications that use libcroco-0.6.

%{?mingw_debug_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libcroco-%{version}

%build

%mingw_configure --without-pic
%mingw_make %{?_smp_mflags} V=1
%install
%mingw_make_install "DESTDIR=$RPM_BUILD_ROOT"
find $RPM_BUILD_ROOT -name "*.la" -delete
%oreon_autofiles mingw32-libcroco usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw32-libcroco-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libcroco usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libcroco-static usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libcroco -f %{oreon_filedir}/mingw32-libcroco.list
%files -n mingw32-libcroco-static -f %{oreon_filedir}/mingw32-libcroco-static.list
%files -n mingw64-libcroco -f %{oreon_filedir}/mingw64-libcroco.list
%files -n mingw64-libcroco-static -f %{oreon_filedir}/mingw64-libcroco-static.list

%changelog

%autochangelog
