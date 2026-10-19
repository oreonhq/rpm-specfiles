%global source0_hash b3909bdcb4905b68427d6ab581e01f436dff8e5c0a389b1e0b14500f18806ebb
%global tarball_version %(echo %{version} | tr '~' '.')
%global major_version %(echo %{tarball_version} | cut -d. -f1)
Name:           gnome-tweaks
Version:        49.0
Release:        2%{?dist}
Summary:        Customize advanced GNOME 3 options
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Tweaks
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{version}.tar.xz
Requires:       gnome-desktop4
Requires:       gobject-introspection
Requires:       gsettings-desktop-schemas
Requires:       gtk4
Requires:       libadwaita
Requires:       libgudev
Requires:       libnotify
Requires:       pango
Requires:       %{py3_dist pygobject}
Recommends:     gnome-settings-daemon
Recommends:     gnome-shell
Recommends:     mutter
Recommends:     sound-theme-freedesktop
Suggests:       gnome-shell-extension-user-theme
Provides:       gnome-tweak-tool = %{version}-%{release}
BuildArch:      noarch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  python3-devel
# /oreon:deps
%description
GNOME Tweaks allows adjusting advanced configuration settings in GNOME 3. This
includes things like the fonts used in user interface elements, alternative user
interface themes, changes in window management behavior, GNOME Shell appearance
and extension, etc.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n %{name}-%{tarball_version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml
%files -f %{oreon_filedir}/main.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-2
- Import
