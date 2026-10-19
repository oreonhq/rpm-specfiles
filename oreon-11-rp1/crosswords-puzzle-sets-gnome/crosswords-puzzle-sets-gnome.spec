%global source0_hash 96c67a660b2df5782e6c2c2145c51066ab46791b53ad048758ba1f74de18fc6b
%global puzzleset gnome
%global srcname puzzle-sets-%{puzzleset}
Name:           crosswords-%{srcname}
Version:        0.4.5
Release:        1%{?dist}
Summary:        Extra puzzles to go with GNOME Crosswords
License:        GPL-3.0-or-later and CC-BY-SA-4.0
URL:            https://gitlab.gnome.org/jrb/%{srcname}
Source0:        https://gitlab.%{puzzleset}.org/jrb/%{srcname}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       crosswords
Supplements:    crosswords
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
# /oreon:deps
%description
This package is for collecting the great puzzles put out by crossword
authors to go with GNOME Crosswords.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%meson
%meson_build
%install
%meson_install
%oreon_autofiles main

%check

appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
