%global source0_hash 2654ddd64ab243e1424d44b8f293daec1eab442809dd85b763ce70a58aa641e4
%?mingw_package_header
Summary:        MinGW Windows port of Gamerzilla Integration Library
Name: mingw-libgamerzilla
Version: 0.1.3
Release:        1%{?dist}
License: zlib
URL: https://github.com/dulsi/libgamerzilla
Source0:        http://www.identicalsoftware.com/gamerzilla/libgamerzilla-%{version}.tgz
Patch0: libgamerzilla-win.patch
BuildArch:      noarch
# oreon:deps
BuildRequires:  cmake
BuildRequires:  mingw32-binutils
BuildRequires:  mingw32-curl
BuildRequires:  mingw32-filesystem
BuildRequires:  mingw32-gcc
BuildRequires:  mingw32-gcc-c++
BuildRequires:  mingw32-jansson
BuildRequires:  mingw64-binutils
BuildRequires:  mingw64-curl
BuildRequires:  mingw64-filesystem
BuildRequires:  mingw64-gcc
BuildRequires:  mingw64-gcc-c++
BuildRequires:  mingw64-jansson
# /oreon:deps
%description
Gamerzilla is trophy/achievement system for games. It integrates with a
hubzilla plugin to display your results online. Games can either connect
directly to hubzilla or connect to a game launcher with using this
library.

# Win32
%package -n mingw32-libgamerzilla
Summary:        MinGW Windows port of Gamerzilla Integration Library
%description -n mingw32-libgamerzilla
Gamerzilla is trophy/achievement system for games. It integrates with a
hubzilla plugin to display your results online. Games can either connect
directly to hubzilla or connect to a game launcher with using this
library.

# Win64
%package -n mingw64-libgamerzilla
Summary:        MinGW Windows port of Gamerzilla Integration Library
%description -n mingw64-libgamerzilla
Gamerzilla is trophy/achievement system for games. It integrates with a
hubzilla plugin to display your results online. Games can either connect
directly to hubzilla or connect to a game launcher with using this
library.

%?mingw_debug_package

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n libgamerzilla-%{version}
%patch -P0 -p1

%build

%mingw_cmake
%mingw_make %{?smp_mflags}
%install
%mingw_make DESTDIR=%{buildroot} install
mkdir %{buildroot}/%{mingw32_bindir}
mkdir %{buildroot}/%{mingw64_bindir}
mv %{buildroot}/%{mingw32_libdir}/libgamerzilla.dll %{buildroot}/%{mingw32_bindir}/libgamerzilla.dll
mv %{buildroot}/%{mingw64_libdir}/libgamerzilla.dll %{buildroot}/%{mingw64_bindir}/libgamerzilla.dll
%oreon_autofiles mingw32-libgamerzilla usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles mingw64-libgamerzilla usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n mingw32-libgamerzilla -f %{oreon_filedir}/mingw32-libgamerzilla.list
%files -n mingw64-libgamerzilla -f %{oreon_filedir}/mingw64-libgamerzilla.list

%changelog

%autochangelog
