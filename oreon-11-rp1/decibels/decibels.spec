%global source0_hash 29b79ba2e2967e69141e39f0ad2c677e38fe3ffb9fba0fa5c7531f94d3f673ca

%global rdnn_name org.gnome.Decibels
%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           decibels
Version:        49.0
Release:        %autorelease
Summary:        Audio player for the GNOME desktop

# one source file is GPLv2+ the rest are GPLv3
License:        GPL-2.0-or-later and GPL-3.0-only
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  (npm(typescript) >= 5.7.3 with npm(typescript) < 5.8)
Requires:       hicolor-icon-theme
# Lacking typelib dependency generator, so use package names instead
Requires:       gtk4
Requires:       libadwaita
Requires:       gstreamer1-plugins-bad-free-libs
# Bundled gi-typescript-defs
Provides:       bundled(gi-typescript-definitions)

# Codecs to make it work
Recommends:     gstreamer1-plugins-good
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-ugly-free

BuildArch:      noarch

%description
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{tarball_version}

%conf
%meson

%build
%meson_build

%install
%meson_install

%find_lang %{rdnn_name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn_name}.metainfo.xml

%files -f %{rdnn_name}.lang
%license LICENSE
%doc README*
%{_bindir}/%{rdnn_name}
%{_datadir}/%{rdnn_name}/
%{_datadir}/applications/%{rdnn_name}.desktop
%{_datadir}/icons/hicolor/*/*/%{rdnn_name}*
%{_datadir}/dbus-1/services/%{rdnn_name}.service
%{_metainfodir}/%{rdnn_name}.metainfo.xml

%changelog
%autochangelog
