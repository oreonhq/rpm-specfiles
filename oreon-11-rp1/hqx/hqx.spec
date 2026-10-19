%global source0_hash 5a44f1745b7fb0321c1d244822d79505df7cf85cfe383ee70b16f5bcd6803396
%global summ() High quality upscaling %1 for pixel-art
Name: hqx
Summary:        High quality upscaling program for pixel-art
License: LGPL-2.1-or-later
Version: 1.2
Release:        1%{?dist}
URL: https://github.com/grom358/hqx
Source0:        https://github.com/grom358/%{name}/archive/v%{version}/%{name}-v%{version}.tar.gz
Patch0: %{name}--add-man-page.patch
Patch1: %{name}--undefined-variables.patch
Requires: lib%{name}%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  DevIL-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Command-line program providing an implementation of hqx,
one of the pixel art scaling algorithms developed by Maxim Stepin.

%package -n lib%{name}
Summary: %{summ library}
%description -n lib%{name}
Library providing an implementation of hqx, one of the pixel art
scaling algorithms developed by Maxim Stepin.

%package -n lib%{name}-devel
Summary: Development files for lib%{name}
Requires: lib%{name}%{?_isa} = %{version}-%{release}
%description -n lib%{name}-devel
This package provides development files required to build applications
using lib%{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

autoreconf -vi
%configure --disable-static
sed -e '/^CFLAGS = -O3$/d' -i Makefile
%make_build
%install
%make_install
rm %{buildroot}%{_libdir}/lib%{name}.la
%oreon_autofiles main usr/*/lib*.so.* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libhqx -f %{oreon_filedir}/libhqx.list
%files -n libhqx-devel -f %{oreon_filedir}/libhqx-devel.list

%changelog

%autochangelog
