Name:           harfbuzz
Version:        13.1.1
Release:        2%{?dist}
Summary:        Text shaping library

License:        MIT-Modern-Variant
URL:            https://github.com/harfbuzz/harfbuzz/
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 e7f3b8bac3fdcc529985be8e84fbd65c675ac47ee58512b15a5dd620c79ffe2a
%global source0_file harfbuzz-13.1.1.tar.xz
# oreon url source checksums end

BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  libicu-devel
BuildRequires:  graphite2-devel
BuildRequires:  gtk-doc
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  meson

# Graphite shaping links libgraphite2; explicit Requires for minimal ISO roots
# where auto-deps are not always pulled into the transaction.
Requires:       graphite2%{?_isa}

# https://github.com/harfbuzz/harfbuzz/issues/3163
%global _distro_extra_cflags -fno-exceptions
%global _distro_extra_cxxflags -fno-exceptions -fno-rtti

%description
HarfBuzz is an implementation of the OpenType Layout engine.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       %{name}-icu%{?_isa} = %{version}-%{release}
Requires:       %{name}-cairo%{?_isa} = %{version}-%{release}
Requires:       %{name}-raster%{?_isa} = %{version}-%{release}
Requires:       %{name}-vector%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        icu
Summary:        Harfbuzz ICU support library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    icu
This package contains Harfbuzz ICU support library.

%package        cairo
Summary:        Harfbuzz Cairo support library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    cairo
This package contains Harfbuzz Cairo support library.

%package        raster
Summary:        Harfbuzz Raster support library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    raster
This package contains Harfbuzz Raster support library.

%package        vector
Summary:        Harfbuzz Vector support library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    vector
This package contains Harfbuzz Vector support library.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/harfbuzz-13.1.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "e7f3b8bac3fdcc529985be8e84fbd65c675ac47ee58512b15a5dd620c79ffe2a" || { echo "oreon: Source0 SHA256 mismatch for harfbuzz-13.1.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
%meson -Dgraphite2=enabled -Dchafa=disabled
%meson_build


%install
%meson_install


%check
%meson_test


%ldconfig_scriptlets

%ldconfig_scriptlets icu

%ldconfig_scriptlets cairo

%ldconfig_scriptlets raster

%ldconfig_scriptlets vector

%files
%license COPYING
%doc NEWS AUTHORS README.md
%{_libdir}/libharfbuzz.so.0*
%{_libdir}/libharfbuzz-gobject.so.0*
%{_libdir}/libharfbuzz-subset.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/HarfBuzz-0.0.typelib

%files devel
%doc %{_datadir}/gtk-doc
%{_bindir}/hb-info
%{_bindir}/hb-view
%{_bindir}/hb-raster
%{_bindir}/hb-shape
%{_bindir}/hb-subset
%{_bindir}/hb-vector
%{_includedir}/harfbuzz/
%{_libdir}/libharfbuzz.so
%{_libdir}/libharfbuzz-gobject.so
%{_libdir}/libharfbuzz-cairo.so
%{_libdir}/libharfbuzz-icu.so
%{_libdir}/libharfbuzz-raster.so
%{_libdir}/libharfbuzz-subset.so
%{_libdir}/libharfbuzz-vector.so
%{_libdir}/pkgconfig/harfbuzz.pc
%{_libdir}/pkgconfig/harfbuzz-cairo.pc
%{_libdir}/pkgconfig/harfbuzz-gobject.pc
%{_libdir}/pkgconfig/harfbuzz-icu.pc
%{_libdir}/pkgconfig/harfbuzz-raster.pc
%{_libdir}/pkgconfig/harfbuzz-subset.pc
%{_libdir}/pkgconfig/harfbuzz-vector.pc
%{_libdir}/cmake/harfbuzz/
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/HarfBuzz-0.0.gir

%files icu
%{_libdir}/libharfbuzz-icu.so.*

%files cairo
%{_libdir}/libharfbuzz-cairo.so.*

%files raster
%{_libdir}/libharfbuzz-raster.so.*

%files vector
%{_libdir}/libharfbuzz-vector.so.*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 13.1.1-2
- Prepare for Oreon 11 (RP1)
