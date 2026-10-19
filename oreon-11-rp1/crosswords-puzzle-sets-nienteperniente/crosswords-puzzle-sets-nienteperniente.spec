%global source0_hash a991fbadbe0612ffde3b39740d66e98d25c5d7e54ac5c463ba631324fed95cc9
%global puzzleset nienteperniente
%global srcname puzzle-sets-%{puzzleset}
Name:           crosswords-%{srcname}
Version:        0.1.0
Release:        1%{?dist}
Summary:        Italian puzzle sets from Niente per niente for GNOME Crosswords
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/davide125/%{srcname}
Source0:        https://gitlab.gnome.org/davide125/%{srcname}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       crosswords
Supplements:    crosswords
Requires:       python3
Requires:       python3dist(puzpy)
Requires:       python3dist(requests)
# oreon:deps
BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
# /oreon:deps
%description
This repo contains Italian puzzle set downloaders for GNOME Crosswords. The
puzzles are pulled from BOOM!!! niente per niente and converted to the ipuz
format supported by Crosswords.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
install -Dpm0755 puzdownloader-%{puzzleset}.py \
  %{buildroot}%{_libexecdir}/puzdownloader-%{puzzleset}
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
