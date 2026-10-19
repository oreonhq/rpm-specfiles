%global source0_hash 1c31aec4da15ecc6ba01c01af0b1f82537fb250b970c86e8066d5e9c311f6481
%global __provides_exclude_from ^%{_libdir}/gthumb/.*\\.so$
%global __requires_exclude ^(%%(find %{buildroot}%{_libdir}/gthumb/ -name '*.so' | xargs -n1 basename | sort -u | paste -s -d '|' -))
Name:           gthumb
Epoch:          1
Version:        3.12.11
Release:        1%{?dist}
Summary:        Image viewer, editor, organizer
License:        GPL-2.0-or-later
URL:            https://wiki.gnome.org/Apps/gthumb
Source0:        https://download.gnome.org/sources/%{name}/3.12/%{name}-%{version}.tar.xz
%if %{defined el8}
ExcludeArch:    s390x
%endif
Requires: hicolor-icon-theme
Provides: bundled(libjpeg)
# oreon:deps
BuildRequires:  bison
BuildRequires:  desktop-file-utils
BuildRequires:  flex
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(appstream)
BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libbrasero-burn3)
BuildRequires:  pkgconfig(libheif)
BuildRequires:  pkgconfig(libjxl)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libraw)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(zlib)
# /oreon:deps
%description
gthumb is an application for viewing, editing, and organizing
collections of images.

%package devel
Summary: Header files needed for developing gthumb extensions
Requires: %{name}%{_isa} = %{epoch}:%{version}-%{release}
%description devel
The gthumb-devel package includes header files for the gthumb
package.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n gthumb-devel -f %{oreon_filedir}/gthumb-devel.list

%changelog

%autochangelog
