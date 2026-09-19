%global source0_hash d6071390a0980fb8eb8418750766c744cf0bca56f24ab4dbe3f23cb1ffd1973d

Name:           gcolor3
Version:        2.4.0
Release:        16%{?dist}
Summary:        A simple color chooser written in GTK3 (like gcolor2)

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            https://www.hjdskes.nl/projects/gcolor3/

Source0:        https://gitlab.gnome.org/World/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
# Extracted from upstream merge request:
#   https://gitlab.gnome.org/World/gcolor3/-/merge_requests/151
Patch0:         gcolor3-2.4.0-libportal-0.5.patch

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  gnome-common
BuildRequires:  gtk3-devel >= 3.12.0
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  libappstream-glib
BuildRequires:  make
BuildRequires:  pkgconfig(libportal-gtk3)
Requires:       hicolor-icon-theme

%description
Gcolor3 is a color selection dialog written in GTK+ 3. It is much alike Gcolor2,
but uses the newer GTK+ version to better integrate into your modern desktop.
It has the same feature set as Gcolor2, except that recent versions of Gcolor3
use an .ini style file to save colors (older versions use the same file as
Gcolor2).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang gcolor3
desktop-file-validate %{buildroot}%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/nl.hjdskes.gcolor3.appdata.xml

%files -f gcolor3.lang
%doc README.md
%license LICENSE
%{_bindir}/gcolor3
%{_datadir}/applications/nl.hjdskes.gcolor3.desktop
%{_datadir}/icons/hicolor/scalable/apps/nl.hjdskes.gcolor3.svg
%{_datadir}/icons/hicolor/symbolic/apps/nl.hjdskes.gcolor3-symbolic.svg
%{_metainfodir}/nl.hjdskes.gcolor3.appdata.xml
%{_mandir}/man1/gcolor3.1*

%changelog
%autochangelog
