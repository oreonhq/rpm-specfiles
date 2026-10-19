%global source0_hash ce09138971617f46edc9be82909738023ea04b0cc2e194e202ca859444cda3fb
%global puzzleset xword-dl
%global srcname puzzle-sets-%{puzzleset}
Name:           crosswords-%{srcname}
Version:        0.5.1
Release:        1%{?dist}
Summary:        Puzzle Sets from assorted newspapers for GNOME Crosswords
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/jrb/%{srcname}
Source0:        https://gitlab.gnome.org/jrb/%{srcname}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch
Requires:       crosswords
Supplements:    crosswords
Requires:       python3-xword-dl
Provides:       crosswords-puzzle-sets-puzzlepull = %{version}-%{release}
Obsoletes:      crosswords-puzzle-sets-puzzlepull < 0.3.0-2
# oreon:deps
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libappstream-glib
BuildRequires:  meson
# /oreon:deps
%description
Download crossword puzzles for GNOME Crosswords from assorted newspapers using
xword-dl.

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
