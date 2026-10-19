%global source0_hash 397297bbd140a2b2c90024392dbc5f8a77bc6a10472308c7741c7913e82eb050
%global rdnn        dev.geopjr.Tuba
Name:           tuba
Version:        0.10.3
Release:        1%{?dist}
Summary:        Browse the Fediverse
License:        GPL-3.0-only
URL:            https://tuba.geopjr.dev/
Source0:        https://github.com/GeopJr/Tuba/archive/v%{version}/Tuba-%{version}.tar.gz
Patch:          0001-Revert-feat-meson-use-appstream-for-appdata-validation-1379.patch
Requires:       hicolor-icon-theme
Recommends:     webp-pixbuf-loader
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(clapper-0.0)
BuildRequires:  pkgconfig(clapper-gtk-0.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gexiv2)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gtksourceview-5)
BuildRequires:  pkgconfig(icu-uc)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libsecret-1)
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libspelling-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(webkitgtk-6.0)
BuildRequires:  vala
# /oreon:deps
%description
Explore the federated social web with Tuba for GNOME. Stay connected to your
favorite communities, family and friends with support for popular Fediverse
platforms like Mastodon, GoToSocial, Akkoma & more!

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Tuba-%{version}
%oreon_prep
%build

%meson \
    -Dclapper=enabled \
    -Dspelling=enabled \
    -Dgstreamer=enabled \
    -Din-app-browser=enabled \
    -Dgexiv2=enabled
%meson_build
%install
%meson_install
%find_lang %{rdnn}
%oreon_autofiles main

%check

%meson_test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
