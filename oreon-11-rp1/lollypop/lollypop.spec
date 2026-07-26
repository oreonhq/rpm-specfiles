%global source0_hash cb5fda9d34c7519edf0d74393269ec3d98670e7a247c4fb08d19e089ed5d5873

# bytecompile with Python 3
%global __python %{__python3}
%global provider org.gnome.Lollypop

Name:           lollypop
Version:        1.4.45
Release:        2%{?dist}
Summary:        Music player for GNOME
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/World/lollypop
Source0:        https://adishatz.org/lollypop/%{name}-%{version}.tar.xz

BuildRequires:  gobject-introspection-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  python3-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk3-devel
BuildRequires:  intltool
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(pygobject-3.0) >= 3.29.1
BuildRequires:  pkgconfig(libsoup-3.0)
BuildRequires:  pkgconfig(libhandy-1) >= 1.5
Requires:       gdk-pixbuf2
Requires:       gstreamer1-plugins-base
Requires:       gobject-introspection
Requires:       gtk3
Recommends:     kid3-common
Requires:       libnotify >= 0.7.6
Requires:       python3-gobject
Requires:       python3-cairo
Requires:       python3-dbus
Requires:       python3-pillow
Requires:       python3-beautifulsoup4
Requires:       python3-gstreamer1
Requires:       pango
Requires:       totem-pl-parser
Requires:       gstreamer1-plugins-good
Requires:       libhandy1 >= 1.5
%if %{undefined flatpak}
# managed by an extension for flatpaks
Requires:       yt-dlp
%endif
# last.fm support
BuildArch:      noarch
Obsoletes:      lollypop-cli < 1.0.6

%description
Lollypop is a new GNOME music playing application.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}
sed -i -e 's|libsoup-2.4|libsoup-3.0|' meson.build

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome
chmod +x %{buildroot}%{_bindir}/*%{name}*

%check
#meson_test failed on koji build server with
#url-not-found : <screenshot> failed to connect: Cannot resolve hostname
desktop-file-validate %{buildroot}%{_datadir}/applications/%{provider}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%files -f %{name}.lang
%doc AUTHORS README.md
%license LICENSE 
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.gresource
%{_libexecdir}/%{name}-sp
%{_datadir}/metainfo/%{provider}.*.xml
%{_datadir}/applications/%{provider}.desktop
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/icons/hicolor/*/apps/%{provider}.png
%{_datadir}/icons/hicolor/*/apps/%{provider}*.svg
%{_datadir}/icons/hicolor/*/actions/%{provider}-*.svg
%{_datadir}/dbus-1/services/%{provider}.SearchProvider.service
%{_datadir}/gnome-shell/search-providers/%{provider}.SearchProvider.ini
%{python3_sitelib}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
