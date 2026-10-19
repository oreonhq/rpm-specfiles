%global source0_hash 5f4a7a8bb884f793c278ac3f3713be41980c5eedccecff0260411347714facb4
Name:		SDL_net
Version:	1.2.8
Release:        32%{?dist}
Summary:        SDL portable network library
License:	LGPL-2.0-or-later
URL:		http://www.libsdl.org/projects/SDL_net/
Source0:        http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This is a portable network library for use with SDL.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.4-1
Requires:	pkgconfig
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles SDL_net-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL_net-devel -f %{oreon_filedir}/SDL_net-devel.list

%changelog

%autochangelog
