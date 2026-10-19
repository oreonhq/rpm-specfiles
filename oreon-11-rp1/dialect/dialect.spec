%global source0_hash 9efd2695b1339d7b98a4207ced8e49202a2cf3ba233900da141eccad555805be
%global         uuid app.drey.Dialect
%global         forgeurl0 https://github.com/dialect-app/dialect
%global         forgeurl1 https://github.com/dialect-app/po
%global         adw_version 1.6.0
Name:           dialect
Version:        2.6.1
Release:        1%{?dist}
Summary:        A translation app for GNOME based on Google Translate
%global         tag0 %{version}
%global         tag1 %{version}
%forgemeta -a
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl0}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        %{forgesource1}
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       gstreamer1-plugins-base
Requires:       gtk4
Requires:       libadwaita >= %{adw_version}
Requires:       libsecret
Requires:       libsoup3
Requires:       python3-gobject >= 3.51.0
Requires:       python3-dbus
Requires:       python3-gtts
Requires:       python3-beautifulsoup4
Requires:       libspelling
Requires:       gtksourceview5
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  gstreamer1-devel
BuildRequires:  gtk4-devel
BuildRequires:  libadwaita-devel
BuildRequires:  libappstream-glib
BuildRequires:  libsecret-devel
BuildRequires:  libsoup3-devel
BuildRequires:  meson
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-devel
# /oreon:deps
%description
A translation app for GNOME based on Google Translate.

Features:
* Text translation up to 5000 chars
* Text to speech
* History
* Automatic language detection
* Clipboard buttons

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup -z 0
gzip -dc %{SOURCE1} | tar -xof -
rmdir po
mv po-%{tag1} po

%build

%meson
%meson_build
%install
%meson_install
%py_byte_compile %{python3} %{buildroot}%{_datadir}/%{name}/
%find_lang %{name}
%find_lang %{name}-cldr-langs
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}/%{_datadir}/applications/%{uuid}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{uuid}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
