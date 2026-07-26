%global source0_hash 42c155816dae2c5dad560faa50edaa1ca84536530283d37859c4b91e82675110

Name: t4k_common
Version: 0.1.1
Release: 40%{?dist}
URL: https://github.com/tux4kids/t4kcommon/
Summary: Library for Tux4Kids applications
License: GPL-3.0-or-later
Source0: https://github.com/tux4kids/t4kcommon/archive/debian/0.1.1-1.1/t4k_common-0.1.1.tar.gz
Patch0: t4k_common-0.1.1.patch
Patch1: t4k_common-c99.patch
Patch2: pointer-types.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: SDL-devel SDL_mixer-devel SDL_image-devel
BuildRequires: SDL_Pango-devel SDL_net-devel librsvg2-devel cairo-devel
BuildRequires: libpng-devel libxml2-devel doxygen
Provides: bundled(liblinebreak)

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

%files
%license COPYING
%doc README
%{_libdir}/lib%{name}.so.*
%{_datadir}/%{name}/

%files devel
%doc doxygen/html/
%{_libdir}/lib%{name}.so
%{_includedir}/t4k*.h
%{_libdir}/pkgconfig/t4k_common.pc

%changelog
%autochangelog
