%global source0_hash 7acad286ac9d8ed1d7328411ec38d225dd8a90acb848f63bb8bb7edee8de42ed
Name:		radius-engine
Version:	1.1
Release:        1%{?dist}
Summary:        A Lua based real-time 2D graphics game engine
License:	MIT
URL:		http://radius-engine.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:		radius-engine-0.6-configure-lua.patch
Patch1:		radius-engine-1.1-shared-libs.patch
Patch2:		radius-engine-1.1-disable-extra-portability.patch
Patch3:		radius-engine-1.1-compat-lua.patch
# oreon:deps
BuildRequires:  SDL-devel
BuildRequires:  SDL_sound-devel
BuildRequires:  autoconf
BuildRequires:  compat-lua-devel
BuildRequires:  libpng-devel
BuildRequires:  libtool
BuildRequires:  make
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  physfs-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
Radius Engine is a Lua script-based real-time 2D graphics engine designed for 
rapidly prototyping games. Built on top of SDL and OpenGL, games made with 
Radius Engine are portable to both Windows and Linux.

%package devel
Summary:	Development libraries and headers for Radius Engine
Requires:	compat-lua-devel, SDL-devel, mesa-libGL-devel, mesa-libGLU-devel
Requires:	physfs-devel, libpng-devel, zlib-devel, SDL_sound-devel
Requires:	%{name} = %{version}-%{release}
%description devel
Development libraries and headers for Radius Engine.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .lua
%patch -P1 -p1 -b .shared
%patch -P2 -p1 -b .disable-extra-portability
%patch -P3 -p1 -b .compat-lua
# autoconf is being anal now.
mv configure.in configure.ac
autoreconf -if
chmod -x *.c *.h ChangeLog

%build

%configure --disable-static
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
rm -rf %{buildroot}%{_libdir}/*.la
%ldconfig_scriptlets
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n radius-engine-devel -f %{oreon_filedir}/radius-engine-devel.list

%changelog

%autochangelog
