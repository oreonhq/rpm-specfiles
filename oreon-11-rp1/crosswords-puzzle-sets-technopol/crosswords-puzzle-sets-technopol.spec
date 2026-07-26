%global source0_hash e5701b164bf4f8fdf31c901bcbe5840c0628d1c009e664041411f7ea270558e9

%global puzzleset technopol
%global srcname puzzle-sets-%{puzzleset}

Name:           crosswords-%{srcname}
Version:        0.1.0
Release:        %autorelease
Summary:        Polish crosswords downloader from TECHNOPOL for GNOME Crosswords

License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/miku/%{srcname}
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
Requires:       python3dist(beautifulsoup4)
Requires:       python3dist(requests)

%description
This repo contains Polish puzzle set downloaders for GNOME Crosswords. The
puzzles are pulled from TECHNOPOL and converted to ipuz format supported
by Crosswords.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build
%meson
%meson_build

%install
%meson_install

install -Dpm0755 technopol.py %{buildroot}%{_bindir}/technopol-downloader

%check
appstream-util validate-relax --nonet \
  %{buildroot}%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%files
%license COPYING
%doc README.md
%{_bindir}/technopol-downloader
%{_datadir}/crosswords/puzzle-sets/%{puzzleset}/
%{_metainfodir}/org.gnome.Crosswords.PuzzleSets.%{puzzleset}.metainfo.xml

%changelog
%autochangelog
