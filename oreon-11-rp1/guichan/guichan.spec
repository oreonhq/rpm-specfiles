%global source0_hash 39b78c7ee4f2c1411b856dcde90ee734c91feed9bf88cd40db41720af9809ccd
%define microversion 0.8.1
Name:           guichan
Version:        0.8.3
Release:        1%{?dist}
Summary:        Portable C++ GUI library for games using Allegro, SDL and OpenGL
License:        BSD-3-Clause
URL:            https://github.com/darkbitsorg/guichan
Source0:        https://github.com/darkbitsorg/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         guichan-0.8.1-extended-utf8-support.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  allegro-devel
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libGL-devel
BuildRequires:  libtool
BuildRequires:  make
# /oreon:deps
%description
Guichan is a small, efficient C++ GUI library designed for games. It comes
with a standard set of widgets and can use several different objects for 
displaying graphics and grabbing user input.

%package devel
Summary:        Header and libraries for guichan development
Requires:       %{name} = %{version}-%{release}
Requires:       pkgconfig
%description devel
This package includes header and libraries files for development using
guichan, a small and efficient C++ GUI library designed for games. This
package is needed to build programs written using guichan.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

autoreconf -if
%configure
make %{?_smp_mflags}
%install
make install DESTDIR=$RPM_BUILD_ROOT
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n guichan-devel -f %{oreon_filedir}/guichan-devel.list

%changelog

%autochangelog
