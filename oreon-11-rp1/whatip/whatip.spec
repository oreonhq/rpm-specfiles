%global source0_hash 5bfb8eb4edc583578128c7d7d9bb86d5c8974fb43e4bf5e21e70d33e297500a3

%global app_id  org.gabmus.whatip

Name:           whatip
Version:        1.2
Release:        %autorelease
Summary:        Info on your IP address
License:        GPL-3.0-or-newer
URL:            https://gitlab.gnome.org/GabMus/whatip
Source0:        %{url}/-/archive/%{version}/whatip-%{version}.tar.bz2

BuildRequires:  meson
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
Requires:       gtk4
Requires:       libadwaita
Requires:       iproute
Requires:       iputils
Requires:       python3-gobject
Requires:       python3-netaddr
Requires:       python3-requests
Requires:       hicolor-icon-theme

BuildArch:      noarch

%description
What IP displays information on your local network, IP addresses and open ports.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

%build
%meson
%meson_build

%install
%meson_install

desktop-file-validate %{buildroot}%{_datadir}/applications/%{app_id}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%find_lang %{name}

%files -f %{name}.lang
%license LICENSE
%doc README.md
%{_bindir}/whatip
%{python3_sitelib}/%{name}/
%{_datadir}/applications/%{app_id}.desktop
%{_datadir}/dbus-1/services/%{app_id}.service
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/*/%{app_id}*
%{_metainfodir}/%{app_id}.appdata.xml
%{_datadir}/%{name}/

%changelog
%autochangelog
