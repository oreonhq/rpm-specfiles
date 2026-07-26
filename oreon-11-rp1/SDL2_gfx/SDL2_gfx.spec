%global source0_hash 63e0e01addedc9df2f85b93a248f06e8a04affa014a835c2ea34bfe34e576262

Summary: SDL2 graphics drawing primitives and other support functions
Name: SDL2_gfx
Version: 1.0.4
Release: 18%{?dist}
License: Zlib
URL: http://www.ferzkopp.net/Software/SDL2_gfx-2.0/
Source: http://www.ferzkopp.net/Software/SDL2_gfx/%{name}-%{version}.tar.gz
# Requires --batch support not currently in SDL2_test
#Patch0: 0001-test-Add-batch-switch.patch
Patch1: 0002-test-format-security.patch

BuildRequires: make
BuildRequires: gcc libtool
BuildRequires: SDL2-devel
# for -lSDL2_test
BuildRequires: SDL2-static
BuildRequires: doxygen

%description
Library providing graphics drawing primitives and other support functions
wrapped up in an addon library for the Simple Direct Media version 2 (SDL2)
cross-platform API layer.

%package devel
Summary: Development files for SDL2_gfx
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: SDL2-devel%{?_isa}

%description devel
This package contains the files required to develop programs which use SDL2_gfx.

%package docs
Summary: API Documentation for SDL2_gfx
BuildArch: noarch
Requires: %{name} = %{version}-%{release}

%description docs
This package contains the API documentation for SDL2_gfx library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find -name '*.[ch]' |xargs chmod -x
chmod -x NEWS README AUTHORS COPYING
mv test/TestGfx.c test/testgfx.c
sed -i 's/\r//' README
autoreconf -ivf

%build
%configure \
%ifnarch %{ix86} x86_64
    --disable-mmx \
%endif
    --disable-static
%make_build

# API documentation
cd Docs
rm -rf html
doxygen html.doxyfile
cd ..

%install
%make_install

# Missing from Makefile.am
install -pm644 SDL2_gfxPrimitives_font.h %{buildroot}%{_includedir}/SDL2/

# API documentation
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a Docs/html %{buildroot}%{_pkgdocdir}/

# This might be useful for live tests; ship it in the devel package
install -d %{buildroot}%{_libdir}/%{name}
install -Dpm0644 %{name}.pc %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

find %{buildroot} -type f -name '*.la' -delete

%ldconfig_scriptlets

%files
%license COPYING
%doc NEWS README AUTHORS
%{_libdir}/*.so.*

%files devel
%{_includedir}/SDL2/*.h
%{_libdir}/*.so
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%files docs
%{_pkgdocdir}/html

%changelog
%autochangelog
