%global source0_hash 7e8441755d0de717428c800e45ae06c85ec964af46ac53b9dc65b41bc3a32c74
%global appname org.gnome.Manuals
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           gnome-manuals
Version:        50.1
Release:        1%{?dist}
Summary:        Install, Browse, and Search developer documentation
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/manuals
Source0:        https://download.gnome.org/sources/manuals/50/manuals-%{version}.tar.xz
ExcludeArch:    %{ix86}
Requires:       dbus-common
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(flatpak)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gom-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(libdex-1)
BuildRequires:  pkgconfig(libfoundry-1)
BuildRequires:  pkgconfig(libpanel-1)
BuildRequires:  pkgconfig(webkitgtk-6.0)
# /oreon:deps
%description
Manuals is an extraction of the Documentation component of GNOME Builder
into a standalone application.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n manuals-%{tarball_version} -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang manuals
%oreon_autofiles main

%check

desktop-file-validate \
    $RPM_BUILD_ROOT/%{_datadir}/applications/%{appname}.desktop
appstream-util validate-relax --nonet \
    $RPM_BUILD_ROOT/%{_datadir}/metainfo/%{appname}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
