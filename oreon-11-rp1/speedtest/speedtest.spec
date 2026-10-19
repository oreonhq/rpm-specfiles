%global source0_hash d98d60743903cda0520d794126ec0962d4fc7e94d96ae7ef4d63a9b58c94fcc9
%global forgeurl https://github.com/Ketok4321/%{name}
%global rdnsappid xyz.ketok.Speedtest
Name:           speedtest
Version:        1.4.0
Release:        1%{?dist}
Summary:        A graphical librespeed client written using gtk4 + libadwaita
%forgemeta
License:        GPL-3.0-or-later
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
Requires:       hicolor-icon-theme
Requires:       libadwaita
Requires:       python3-gobject
Requires:       python3dist(aiohttp)
# oreon:deps
BuildRequires:  blueprint-compiler
BuildRequires:  desktop-file-utils
BuildRequires:  git-core
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  meson
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  python3-devel
BuildRequires:  python3dist(aiohttp)
BuildRequires:  python3dist(setuptools)
# /oreon:deps
%description
%{summary}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgeautosetup -p1

%build

%meson
%meson_build
%install
%meson_install
%find_lang %{name}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/*.desktop
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
