%global source0_hash 7e2fa4e8c7c98e8d8140671f5772542afaaa6acccfbd746506886b6d85f7f8d6
Name:           harfbuzz
Version:        14.5.1
Release:        1%{?dist}
Summary:        Text shaping library
License:        MIT-Modern-Variant
URL:            https://github.com/harfbuzz/harfbuzz/
Source0:        https://github.com/harfbuzz/harfbuzz/releases/download/%{version}/harfbuzz-%{version}.tar.xz
Requires:       graphite2%{?_isa}
%global _distro_extra_cflags -fno-exceptions
%global _distro_extra_cxxflags -fno-exceptions -fno-rtti
# oreon:deps
BuildRequires:  cairo-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection-devel
BuildRequires:  graphite2-devel
BuildRequires:  gtk-doc
BuildRequires:  libicu-devel
BuildRequires:  make
BuildRequires:  meson
BuildRequires:  pkgconfig(glew)
BuildRequires:  pkgconfig(glfw3)
# /oreon:deps
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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson -Dgraphite2=enabled -Dchafa=disabled
%meson_build
%install
%meson_install
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%ldconfig_scriptlets
%ldconfig_scriptlets icu
%ldconfig_scriptlets cairo
%ldconfig_scriptlets raster
%ldconfig_scriptlets vector
%files -f %{oreon_filedir}/main.list
%files -n harfbuzz-devel -f %{oreon_filedir}/harfbuzz-devel.list
%files -n harfbuzz-icu -f %{oreon_filedir}/harfbuzz-icu.list
%files -n harfbuzz-cairo -f %{oreon_filedir}/harfbuzz-cairo.list
%files -n harfbuzz-raster -f %{oreon_filedir}/harfbuzz-raster.list
%files -n harfbuzz-vector -f %{oreon_filedir}/harfbuzz-vector.list

%changelog

%autochangelog
