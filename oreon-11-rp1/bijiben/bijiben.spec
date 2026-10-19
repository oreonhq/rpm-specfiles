%global source0_hash b22111bc06956bef359aacf1d6ede1e52a35b000c88113936632f8ac6cedce67
Name:           bijiben
Version:        40.2
Release:        1%{?dist}
Summary:        Simple Note Viewer
License:        GPL-3.0-or-later AND LGPL-3.0-only AND LGPL-2.0-or-later
Url:            http://www.gnome.org
Source0:        http://download.gnome.org/sources/%{name}/40/%{name}-%{version}.tar.xz
Patch02:        webkitdep.patch
Recommends:     gvfs-goa
Provides: bundled(libgd)
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(goa-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libecal-2.0)
BuildRequires:  pkgconfig(libedataserver-1.2)
BuildRequires:  pkgconfig(libhandy-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(tracker-sparql-3.0)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(webkit2gtk-4.1)
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
%description
Simple note editor which emphasis on visuals : quickly write
notes, quickly find it back.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson \
%if 0%{?flatpak}
  -Dprivate_store=true
%else
  -Dprivate_store=false
%endif
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/org.gnome.Notes.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gnome.Notes.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
