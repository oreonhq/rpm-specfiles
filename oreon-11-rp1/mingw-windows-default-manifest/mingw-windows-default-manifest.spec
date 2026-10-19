%global source0_hash 3c6c32b9e29d0c7531b07cab126e2ed069095f1afb7e5648a4936ba7584fd734
%?mingw_package_header
Name:           mingw-windows-default-manifest
Version:        6.4
Release:        1%{?dist}
Summary:        MinGW Default Windows application manifest
License:        FSFAP and MIT
URL:            https://cygwin.com/
Source0:        windows-default-manifest-%{version}.tar.bz2
BuildArch:      noarch
# oreon:deps
BuildRequires:  make
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
# /oreon:deps
%description
The Default Windows application manifest is linked to applications by
default to claim compatibility with the latest Windows versions.
The package version number reflects the latest Windows kernel version
supported by this manifest.

This package contains the MinGW Windows cross compiled default Windows
application manifest.

# Win32
%package -n mingw32-windows-default-manifest
Summary:        MinGW Default Windows application manifest
%description -n mingw32-windows-default-manifest
The Default Windows application manifest is linked to applications by
default to claim compatibility with the latest Windows versions.
The package version number reflects the latest Windows kernel version
supported by this manifest.

This package contains the MinGW Windows cross compiled default Windows
application manifest.

# Win64
%package -n mingw64-windows-default-manifest
Summary:        MinGW Default Windows application manifest
%description -n mingw64-windows-default-manifest
The Default Windows application manifest is linked to applications by
default to claim compatibility with the latest Windows versions.
The package version number reflects the latest Windows kernel version
supported by this manifest.

This package contains the MinGW Windows cross compiled default Windows
application manifest.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n windows-default-manifest

%build

%mingw_configure
%mingw_make %{?_smp_mflags}
%install
%mingw_make install DESTDIR=$RPM_BUILD_ROOT
%oreon_autofiles mingw32-windows-default-manifest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-windows-default-manifest usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-windows-default-manifest -f %{oreon_filedir}/mingw32-windows-default-manifest.list
%files -n mingw64-windows-default-manifest -f %{oreon_filedir}/mingw64-windows-default-manifest.list

%changelog

%autochangelog
