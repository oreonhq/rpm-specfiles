%global source0_hash 3f070dd58ab05998dec18aead923c2f8a02b28a312831ca2628459da0d6c6c10

%global puzzleset keesing
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        4.4
Release:        %autorelease
Summary:        Dutch puzzle sets from web.keesing.com for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/philip.goto/%{srcname}
Source:         %{url}/-/archive/%{version}/%{srcname}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  gcc
BuildRequires:  libappstream-glib
BuildRequires:  meson

BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel

Requires:       crosswords
Supplements:    crosswords

# For the downloader script
Requires:       python3
Requires:       python3dist(python-dateutil)
Requires:       python3dist(requests)
Requires:       python3dist(xmltodict)

%description
This repo contains Dutch puzzle set downloaders for GNOME Crosswords. The
puzzles are pulled from web.keesing.com and converted to ipuz format supported
by Crosswords.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dpm0755 ikeesing.py %{buildroot}%{_libexecdir}/ikeesing

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}
%{_libexecdir}/ikeesing
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
