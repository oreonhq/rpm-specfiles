%global source0_hash dbfcc3ce8f2e52710a44438d690d6fc4f180b0ec0896066c639c2acd9c155340
%global tarball_version %%(echo %{version} | tr '~' '.')
%define major_version %(c=%{version}; echo $c | cut -d. -f1 | cut -d~ -f1)
Name:           quadrapassel
Version:        51.0
Release:        1%{?dist}
Summary:        GNOME Quadrapassel game
License:        GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:            https://wiki.gnome.org/Apps/Quadrapassel
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  clutter-gtk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gsound-devel
BuildRequires:  gtk4-devel
BuildRequires:  itstool
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  libcanberra-devel
BuildRequires:  libgee-devel
BuildRequires:  libmanette-devel
BuildRequires:  librsvg2-devel
BuildRequires:  meson
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  vala
# /oreon:deps
%description
The Russian game of falling geometric shapes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name} --with-gnome
%find_lang %{name}_libgnome-games-support --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Quadrapassel.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/org.gnome.Quadrapassel.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
