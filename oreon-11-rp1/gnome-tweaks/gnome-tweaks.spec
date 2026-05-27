%global source0_hash none

%global tarball_version %%(tr '~' '.' <<<%{version})
%global major_version %%(cut -d '.' -f 1 <<<%{tarball_version})

Name:           gnome-tweaks
Version:        49.0
Release:        2%{?dist}
Summary:        Customize advanced GNOME 3 options

# Software is GPL-3.0+, Appdata file is CC0-1.0
License:        GPL-3.0-or-later AND CC0-1.0
URL:            https://wiki.gnome.org/Apps/Tweaks
Source0:        https://download.gnome.org/sources/%{name}/%{major_version}/%{name}-%{tarball_version}.tar.xz

BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gsettings-desktop-schemas) >= 46.0
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(gudev-1.0)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(pygobject-3.0)
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

%description
GNOME Tweaks allows adjusting advanced configuration settings in GNOME 3. This
includes things like the fonts used in user interface elements, alternative user
interface themes, changes in window management behavior, GNOME Shell appearance
and extension, etc.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -n %{name}-%{tarball_version} -p1


%build
%meson
%meson_build


%install
%meson_install

%find_lang %{name}


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.appdata.xml


%files -f %{name}.lang
%doc AUTHORS NEWS README.md
%license LICENSES/*
%{_bindir}/%{name}
%{python3_sitelib}/gtweak/
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/dbus-1/services/*.service
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.tweaks.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.tweaks-symbolic.svg
%{_metainfodir}/*.appdata.xml


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 49.0-2
- Import
