%global source0_hash 617e574c15f90618b82493c9939d717596ad2ce1ff1de0aad5c9c3976633d379
%global tarball_version %%(echo %%{version} | tr '~' '.')
%global major_version %%(echo %%{tarball_version} | cut -d "." -f 1)
Name:           gnome-robots
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME Robots game
License:        %{shrink:
    GPL-3.0-or-later AND GFDL-1.1-or-later AND
    ((MIT OR Apache-2.0) AND Unicode-DFS-2016) AND
    (Apache-2.0 OR MIT) AND
    (Apache-2.0 WITH LLVM-exception) AND
    MIT AND
    (MIT OR Apache-2.0) AND
    (Unlicense OR MIT)
}
URL:            https://wiki.gnome.org/Apps/Robots
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
Requires:       hicolor-icon-theme
# oreon:deps
BuildRequires:  cargo-rpm-macros
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  itstool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)
# /oreon:deps
%description
The classic game where you have to avoid a hoard of robots who are trying to
kill you. Each step you take brings them closer toward you. Fortunately they
aren't very smart and you also have a helpful teleportation gadget.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{tarball_version}

%build

%meson
%meson_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%install
%meson_install
%find_lang %{name} --with-gnome
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.Robots.desktop
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_datadir}/metainfo/org.gnome.Robots.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
