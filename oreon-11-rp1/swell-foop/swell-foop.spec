%global source0_hash 96b243023e0d4a66f986bc2968b0f0b86618e15a55f97e83fe6ab009e7e782eb

%global tarball_version %%(echo %{version} | tr '~' '.')

Name:           swell-foop
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME colored tiles puzzle game

License:        GPL-2.0-or-later AND CC-BY-SA-4.0
URL:            https://wiki.gnome.org/Apps/Swell%20Foop
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{tarball_version}.tar.xz

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)

BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  yelp-tools

%description
Clear the screen by removing groups of colored and shaped tiles

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --all-name --with-gnome

%check
desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SwellFoop.desktop

%files -f %{name}.lang
%license COPYING
%doc NEWS
%{_bindir}/swell-foop
%{_datadir}/applications/org.gnome.SwellFoop.desktop
%{_datadir}/dbus-1/services/org.gnome.SwellFoop.service
%{_datadir}/glib-2.0/schemas/org.gnome.SwellFoop.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.gnome.SwellFoop*
%{_datadir}/metainfo/org.gnome.SwellFoop.metainfo.xml

%changelog
%autochangelog
