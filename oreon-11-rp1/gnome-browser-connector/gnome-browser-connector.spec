%global source0_hash bd9702ce1c163606ca32b8c13d1f3ba6e82b247cf87aac60610b411df1556212
%global debug_package %{nil}
Name:           gnome-browser-connector
Version:        42.1
Release:        1%{?dist}
Summary:        GNOME Shell browser connector
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-browser-connector
Source0:        https://download.gnome.org/sources/gnome-browser-connector/42/gnome-browser-connector-%{version}.tar.xz
Requires:       dbus
Requires:       gnome-shell
Requires:       hicolor-icon-theme
Requires:       mozilla-filesystem
Requires:       python3-gobject-base
Obsoletes:      chrome-gnome-shell < 10.1-18
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
# /oreon:deps
%description
Native host messaging connector that provides integration with GNOME Shell and
the corresponding extensions repository https://extensions.gnome.org.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.BrowserConnector.desktop
%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 42.1-1
- Prepare for Oreon 11 (RP1)
