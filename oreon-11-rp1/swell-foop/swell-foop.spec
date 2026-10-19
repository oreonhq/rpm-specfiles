%global source0_hash 96b243023e0d4a66f986bc2968b0f0b86618e15a55f97e83fe6ab009e7e782eb
%global tarball_version %%(echo %{version} | tr '~' '.')
Name:           swell-foop
Version:        50.0
Release:        1%{?dist}
Summary:        GNOME colored tiles puzzle game
License:        GPL-2.0-or-later AND CC-BY-SA-4.0
URL:            https://wiki.gnome.org/Apps/Swell%20Foop
Source0:        https://download.gnome.org/sources/%{name}/50/%{name}-%{version}.tar.xz
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gettext-devel
BuildRequires:  itstool
BuildRequires:  meson
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(librsvg-2.0)
BuildRequires:  vala
BuildRequires:  yelp-tools
# /oreon:deps
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
%oreon_autofiles main

%check

desktop-file-validate $RPM_BUILD_ROOT%{_datadir}/applications/org.gnome.SwellFoop.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
