%global source0_hash 7f75d3b97acf707c696ea126424906204ebfa07660162de925173cdd0257eba4

Summary: Rendering of internationalized text for SDL (Simple DirectMedia Layer)
Name: SDL_Pango
Version: 0.1.2
Release: 48%{?dist}
License: LGPL-2.0-or-later
URL: http://sdlpango.sourceforge.net/

Source0: http://downloads.sf.net/sdlpango/SDL_Pango-%{version}.tar.gz
Source1: doxygen.png
Patch0: SDL_Pango-0.1.2-suppress-warning.patch
Patch1: SDL_Pango-0.1.2-API-adds.patch
Patch2: SDL_Pango-0.1.2-matrix_declarations.patch
Patch99: SDL_Pango-0.1.2-fedora-c99.patch

BuildRequires: make
BuildRequires: pango-devel, SDL-devel, dos2unix
BuildRequires: autoconf, automake, libtool

%description
Pango is the text rendering engine of GNOME 2. SDL_Pango connects that engine
to SDL, the Simple DirectMedia Layer.

%package devel
Summary: Development files for SDL_pango
Requires: %{name} = %{version}-%{release}
Requires: pango-devel, SDL-devel, pkgconfig

%description devel
Development files for SDL_pango.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .suppress-warning
%patch -P1 -p1 -b .API-adds
%patch -P2 -p1 -b .matrix_declarations
%patch -P99 -p1 -b .c99
# Clean up, we include the entire "docs/html" content for the devel package
rm -rf docs/html/CVS/
# Replace the corrupt doxygen.png file with a proper one
install -m 0644 -p %{SOURCE1} docs/html/doxygen.png
# Fix the (many) DOS encoded files, not *.png since they get corrupt
find . -not -name \*.png -type f -exec dos2unix -k {} \;
# For FC-5 x86_64 this is required, or the shared library doesn't get built
autoreconf -if

%build
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%ldconfig_scriptlets

%files
%doc AUTHORS ChangeLog COPYING NEWS README
%{_libdir}/*.so.*

%files devel
%doc docs/html/*
%{_includedir}/SDL_Pango.h
%{_libdir}/pkgconfig/SDL_Pango.pc
%exclude %{_libdir}/*.la
%{_libdir}/*.so

%changelog
%autochangelog
