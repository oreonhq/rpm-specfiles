%global source0_hash 9a67ba14df23517c849fcfdea764c73a241e59055299b125e98aeab2a7801ad5
%global rdnn_name org.gnome.Decibels
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           decibels
Version:        49.6.1
Release:        1%{?dist}
Summary:        Audio player for the GNOME desktop
License:        GPL-2.0-or-later and GPL-3.0-only
URL:            https://www.gnome.org
Source0:        https://download.gnome.org/sources/%{name}/49/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
Requires:       gtk4
Requires:       libadwaita
Requires:       gstreamer1-plugins-bad-free-libs
Provides:       bundled(gi-typescript-definitions)
Recommends:     gstreamer1-plugins-good
Recommends:     gstreamer1-plugins-bad-free
Recommends:     gstreamer1-plugins-ugly-free
BuildArch:      noarch
# oreon:deps
BuildRequires:  (npm(typescript) >= 5.7.3 with npm(typescript) < 5.8)
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(blueprint-compiler)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate %{buildroot}%{_datadir}/applications/%{rdnn_name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{rdnn_name}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
