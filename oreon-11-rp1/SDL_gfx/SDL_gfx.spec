%global source0_hash dfb15ac5f8ce7a4952dc12d2aed9747518c5e6b335c0e31636d23f93c630f419

Summary: SDL graphics drawing primitives and other support functions
Name: SDL_gfx
Version: 2.0.27
Release: 8%{?dist}
License: Zlib
URL: http://www.ferzkopp.net/Software/SDL_gfx-2.0/
Source: http://www.ferzkopp.net/Software/SDL_gfx-2.0/SDL_gfx-%{version}.tar.gz
Patch0: SDL_gfx-2.0.13-ppc.patch
BuildRequires: make
BuildRequires:  gcc
BuildRequires: SDL-devel
BuildRequires: libXt-devel

%description
Library providing SDL graphics drawing primitives and other support functions
wrapped up in an addon library for the Simple Direct Media (SDL) cross-platform
API layer.

%package devel
Summary: Development files for SDL_gfx
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Requires: SDL-devel

%description devel
This package contains the files required to develop programs which use SDL_gfx.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P 0 -p1 -b .ppc

%build
%configure \
%ifnarch %{ix86} x86_64
    --disable-mmx \
%endif
    --disable-static
make %{?_smp_mflags}

%install
%make_install

%ldconfig_scriptlets

%files
%doc LICENSE README AUTHORS COPYING
%{_libdir}/*.so.*

%files devel
%{_includedir}/SDL/*.h
%exclude %{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc
%{_libdir}/*.so

%changelog
%autochangelog
