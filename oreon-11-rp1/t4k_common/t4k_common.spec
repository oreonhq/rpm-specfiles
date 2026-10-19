%global source0_hash 61ce0384e3db723b3a956a8b1dfd915c88b633606c7a594f5375979eec40f0b3
Name: t4k_common
Version: 0.1.1
Release:        40%{?dist}
URL: https://github.com/tux4kids/t4kcommon/
Summary:        Library for Tux4Kids applications
License: GPL-3.0-or-later
Source0:        https://github.com/tux4kids/t4kcommon/archive/debian/0.1.1-1.1/t4k_common-0.1.1.tar.gz
Patch0: t4k_common-0.1.1.patch
Patch1: t4k_common-c99.patch
Patch2: pointer-types.patch
Provides: bundled(liblinebreak)
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_Pango-devel
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  SDL_net-devel
BuildRequires:  cairo-devel
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  libpng-devel
BuildRequires:  librsvg2-devel
BuildRequires:  libxml2-devel
BuildRequires:  make
# /oreon:deps
%package devel
Summary: Development files for the Tux4Kids library
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
%description
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

%description devel
library of code shared by TuxMath, TuxType, and
possibly other Tux4Kids apps in the future.

These are the development files.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p0

%build

export CPPFLAGS="$CPPFLAGS -fcommon -std=gnu17"
%configure
make %{?_smp_mflags}
doxygen
rm -f doxygen/html/installdox
%install
INSTALL='install -p' make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
rm -f $RPM_BUILD_ROOT%{_includedir}/t4k_scandir.h
chmod 755 $RPM_BUILD_ROOT%{_libdir}/lib%{name}.so
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n t4k_common-devel -f %{oreon_filedir}/t4k_common-devel.list

%changelog

%autochangelog
