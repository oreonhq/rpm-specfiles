%global source0_hash f4930b1ebb4ecc8f7a021a3b185a668e9ec26a0dcdb9b361a00edbad557e9f62

%global app_id  org.gweled.gweled

Name:           gweled
Version:        1.0~beta1
Release:        5%{?dist}

Summary:        Swapping gem game

License:        GPL-2.0-or-later
URL:            http://launchpad.net/gweled
Source0:        http://launchpad.net/gweled/1.0/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires:	desktop-file-utils
BuildRequires:	gcc
BuildRequires:	libappstream-glib
BuildRequires:	meson >= 0.59.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.36
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.20
BuildRequires:	pkgconfig(clutter-1.0) >= 1.20
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.8
BuildRequires:	pkgconfig(gsound) >= 1.0.3
BuildRequires:	pkgconfig(libgnome-games-support-1) >= 1.0.3
Requires:	hicolor-icon-theme

%description
Gweled is a Gnome version of a popular PalmOS/Windows/Java game called
"Bejeweled" or "Diamond Mine". The aim of the game is to make alignment of 3 or
more gems, both vertically or horizontally by swapping adjacent gems. The game
ends when there are no possible moves left.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/org.gweled.gweled.desktop
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/%{app_id}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/%{name}
%{_datadir}/applications/org.gweled.gweled.desktop
%{_datadir}/glib-2.0/schemas/%{app_id}.gschema.xml
%{_datadir}/icons/hicolor/*/apps/org.%{name}.*
%{_datadir}/pixmaps/%{name}/
%{_datadir}/sounds/%{name}/
%{_metainfodir}/%{app_id}.appdata.xml

%changelog
%autochangelog
