%global source0_hash 79de6b5cdb6b2f3c2bcb5efe370f7f59dccaf0f671b8032844779acc2f7cf0b6

%global uuid    com.github.maoschanz.DynamicWallpaperEditor

Name:           dynamic-wallpaper-editor
Version:        2.7
Release:        12%{?dist}
Summary:        Utility for creation or edition GNOME desktop's XML wallpapers

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://github.com/maoschanz/dynamic-wallpaper-editor
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  desktop-file-utils
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  python3-devel

BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       hicolor-icon-theme

%description
The GNOME desktop allows the wallpaper to change with time.

These dynamic wallpapers are XML files, and you don't want to write these files
yourself: Dynamic Wallpaper Editor is a little utility for the creation or the
edition of these XML wallpapers.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} --with-gnome

%check
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml

%changelog
%autochangelog
