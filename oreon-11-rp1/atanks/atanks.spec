%global source0_hash bc6b1efc9fc7e7624fad1d8352d72e927be0fba2160bb25bb6b8bd6c6370bf43

Name:           atanks
Version:        6.6
Release:        10%{?dist}
Summary:        Remake of a classic DOS game "Scorched Earth"

License:        GPL-2.0-or-later
URL:            http://atanks.sourceforge.net/
Source0:        http://download.sourceforge.net/atanks/atanks-%{version}.tar.gz

# atanks upstream adds "-march=native -O2" to CXXFLAGS which may affect Fedora
# optimization flags. Also not every platform has -march=native option.
Patch0:         atanks-remove-cxxflags-mangling.patch

BuildRequires:  allegro-devel, desktop-file-utils, gcc-c++
BuildRequires: make
Requires:	hicolor-icon-theme

%description
Atomic Tanks is a game in which you control an overly-powerful
tank and attempt to blow up other highly powerful tanks. Players
get to select a number of weapons and defensive items and then
attack each other in a turn-based manner. The last tank standing
is the winner.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build
PREFIX=%{_prefix} CXXFLAGS="%{optflags}" LDFLAGS="$RPM_LD_FLAGS" make %{?_smp_mflags} DEBUG=NO

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 0755 \
    $RPM_BUILD_ROOT%{_datadir}/games/atanks \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_datadir}/pixmaps \
    $RPM_BUILD_ROOT%{_datadir}/applications
install -p -m 0644 *.txt $RPM_BUILD_ROOT%{_datadir}/games/atanks/
install -p -m 0644 unicode.dat $RPM_BUILD_ROOT%{_datadir}/games/atanks/
install -p -m 0755 atanks $RPM_BUILD_ROOT%{_bindir}/atanks
install -p -m 0644 atanks.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/48x48/apps
install -p -m 644 atanks.png \
  %{buildroot}%{_datadir}/icons/hicolor/48x48/apps

cp -pr button exporter misc missile sound stock tank tankgun text title $RPM_BUILD_ROOT%{_datadir}/games/atanks/ 
desktop-file-install \
    --mode 0644 \
    --dir $RPM_BUILD_ROOT%{_datadir}/applications/ \
    --add-category StrategyGame \
    atanks.desktop

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!-- HOUSEKEEPING FOR RICHARD, REMOVE THIS COMMENT WHEN THIS GOES UPSTREAM
BugReportURL: jessefrgsmith@yahoo.ca
SentUpstream: 2014-09-17
-->
<application>
  <id type="desktop">atanks.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Turn-based artillery strategy game</summary>
  <description>
    <p>
      Atomic Tanks is a turn based artillery strategy game where opponents
      take turns to bombard each other with a wide array of different weapons.
      To make things more interesting, Atomic Tanks also features desctructable
      landscapes, teleporting, parachutes and different weather conditions.
    </p>
  </description>
  <url type="homepage">http://atanks.sourceforge.net/index.html</url>
  <screenshots>
    <screenshot type="default">http://atanks.sourceforge.net/Screenshots/scrnshot29.png</screenshot>
  </screenshots>
  <!-- FIXME: change this to an upstream email address for spec updates
  <updatecontact>someone_who_cares@upstream_project.org</updatecontact>
   -->
</application>
EOF

%files
%license COPYING
%doc Changelog README TODO
%dir %{_datadir}/games/atanks
%{_datadir}/games/atanks/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/hicolor/48x48/apps/*
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*
%{_bindir}/atanks

%changelog
%autochangelog
