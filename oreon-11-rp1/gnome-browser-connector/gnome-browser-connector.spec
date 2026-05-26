%global debug_package %{nil}

Name:           gnome-browser-connector
Version:        42.1
Release:        %autorelease
Summary:        GNOME Shell browser connector

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/gnome-browser-connector
Source0:        https://download.gnome.org/sources/gnome-browser-connector/42/gnome-browser-connector-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 bd9702ce1c163606ca32b8c13d1f3ba6e82b247cf87aac60610b411df1556212
%global source0_file gnome-browser-connector-42.1.tar.xz
# oreon url source checksums end

BuildRequires:  desktop-file-utils
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base

Requires:       dbus
Requires:       gnome-shell
Requires:       hicolor-icon-theme
Requires:       mozilla-filesystem
Requires:       python3-gobject-base

# Obsoleted in F37
Obsoletes:      chrome-gnome-shell < 10.1-18

%description
Native host messaging connector that provides integration with GNOME Shell and
the corresponding extensions repository https://extensions.gnome.org.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/gnome-browser-connector-42.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bd9702ce1c163606ca32b8c13d1f3ba6e82b247cf87aac60610b411df1556212" || { echo "oreon: Source0 SHA256 mismatch for gnome-browser-connector-42.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1


%build
%meson
%meson_build


%install
%meson_install


%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.BrowserConnector.desktop


%files
%license LICENSE
%doc NEWS README.md
%{_sysconfdir}/chromium/
%{_sysconfdir}/opt/chrome/
%{_bindir}/gnome-browser-connector
%{_bindir}/gnome-browser-connector-host
%{python3_sitelib}/gnome_browser_connector/
%{_libdir}/mozilla/native-messaging-hosts/
%{_datadir}/applications/org.gnome.BrowserConnector.desktop
%{_datadir}/dbus-1/services/org.gnome.BrowserConnector.service
%{_datadir}/icons/hicolor/*/apps/org.gnome.BrowserConnector.png


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 42.1-1
- Prepare for Oreon 11 (RP1)
