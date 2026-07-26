%global source0_hash 7acad286ac9d8ed1d7328411ec38d225dd8a90acb848f63bb8bb7edee8de42ed

Name:		radius-engine
Version:	1.1
Release:	29%{?dist}
Summary:	A Lua based real-time 2D graphics game engine
License:	MIT
URL:		http://radius-engine.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/%{name}/%{name}-%{version}.tar.gz
Patch0:		radius-engine-0.6-configure-lua.patch
Patch1:		radius-engine-1.1-shared-libs.patch
# Latest autoconf enables "extra-portability" along with "Wall", which causes
# warnings (treated as errors because of Wall) to be thrown. We just need to 
# pass "-Wno-extra-portability" to fix this.
Patch2:		radius-engine-1.1-disable-extra-portability.patch
# Use compat-lua
Patch3:		radius-engine-1.1-compat-lua.patch
BuildRequires: make
BuildRequires:	compat-lua-devel, SDL-devel, mesa-libGL-devel, mesa-libGLU-devel
BuildRequires:	physfs-devel, libpng-devel, zlib-devel, SDL_sound-devel
# I could not figure out a way to generate a patch to enable shared libraries 
# that worked right. All my attempts resulted in an environment where make, 
# when invoked, would re-run aclocal and automake. :P
# So, I'm just running autoreconf in the spec file. :P :P
BuildRequires:	autoconf, libtool

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

%files
%doc ChangeLog
%{_libdir}/libradius-engine.so.*

%files devel
%{_includedir}/radius.h
%{_libdir}/libradius-engine.so
%{_libdir}/pkgconfig/radius-engine.pc

%changelog
%autochangelog
