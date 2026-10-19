%global source0_hash 724cd895ecf4da319a3ef164892b72078bd92632a5d812111261cde248ebcdb7
Name:		SDL_ttf
Version:	2.0.11
Release:        34%{?dist}
Summary:        Simple DirectMedia Layer TrueType Font library
License:	Zlib
URL:		http://www.libsdl.org/projects/SDL_ttf/
Source0:        http://www.libsdl.org/projects/%{name}/release/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
This library allows you to use TrueType fonts to render text in SDL
applications.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.4
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%build

%configure --disable-dependency-tracking --disable-static
make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
%ldconfig_scriptlets
%oreon_autofiles SDL_ttf-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n SDL_ttf-devel -f %{oreon_filedir}/SDL_ttf-devel.list

%changelog

%autochangelog
