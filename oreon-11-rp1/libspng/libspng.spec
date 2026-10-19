%global source0_hash 47ec02be6c0a6323044600a9221b049f63e1953faf816903e7383d4dc4234487
Name:           libspng
Version:        0.7.4
Release:        1%{?dist}
Summary:        Simple, modern libpng alternative
License:        BSD-2-Clause
URL:            https://libspng.org/
Source0:        https://github.com/randy408/libspng/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
Libspng is a C library for reading and writing Portable Network Graphics (PNG)
format files with a focus on security and ease of use.

Libspng is an alternative to libpng, the projects are separate and the APIs are
not compatible.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
# spng incompatible with libpng 1.6.47 (PNGv3)
# https://github.com/randy408/libspng/issues/276
sed -i -e '/\(ch1n3p04\|ch2n3p08\)/s/)$/, should_fail : true)/' tests/images/meson.build

%build

%meson -Ddev_build=true
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n libspng-devel -f %{oreon_filedir}/libspng-devel.list

%changelog

%autochangelog
