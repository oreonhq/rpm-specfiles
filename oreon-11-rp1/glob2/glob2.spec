%global source0_hash 0f4d898ec6b05ce27b4a12ef242cc26571304b90d2509932a4743c71311314b8

Name:           glob2
Version:        0.9.4.4
Release:        73%{?dist}
Summary:        An innovative RTS game

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            http://globulation2.org/
Source0:        http://dl.sv.nongnu.org/releases/%{name}/0.9.4/%{name}-%{version}.tar.gz
#Source3:        glob2.desktop
#patch0 fixes polish diacritics
#Patch0:         glob2-texts.pl.patch
#Patch2:         glob2-gcc43.patch
Patch3:         glob2-0.9.4.1-gcc44.patch
# https://savannah.nongnu.org/bugs/index.php?39593
Patch4:         glob2_SConstruct.patch
Patch5:		glob2-private.patch
Patch6:		glob2-fix_missing_return_in_nonvoid_functions.patch
Patch7:		glob2-iostream.patch
# https://bitbucket.org/giszmo/glob2/pull-requests/7
Patch8:		glob2-gcc7.patch
Patch9:		glob2-python3.patch
Patch10:	glob2-scons3.patch
Patch11:	glob2-fix-tabs.patch
Patch12:	glob2-bool.patch

BuildRequires:  boost-devel
BuildRequires:  desktop-file-utils
BuildRequires:  libvorbis-devel
BuildRequires:  portaudio-devel
BuildRequires:  python3
BuildRequires:  python3-scons
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_net-devel
BuildRequires:  SDL_ttf-devel
BuildRequires:  SDL-devel
BuildRequires:  speex-devel
BuildRequires:  zlib-devel
BuildRequires:  gcc-c++

# Handle font moves more automatically
%global fonts font(dejavusans)
BuildRequires: fontconfig %{fonts}
Requires: %{fonts}

Requires:       hicolor-icon-theme

%description
Globulation 2 brings a new type of gameplay to RTS games. The player chooses
the number of units to assign to various tasks, and the units do their best to
satisfy the requests. This allows players to manage more units and focus on
strategy rather than individual unit's jobs. Globulation 2 also features AI
allowing single-player games or any possible combination of human-computer
teams. Also included is a scripting language for versatile gameplay or
tutorials and an integrated map editor. Globulation2 can be played in single
player mode, through your local network, or over the Internet with Ysagoon
Online Gaming (or YOG for short).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
#%patch 0 -p0
#%patch 2 -p0
%patch 3 -p0
%patch 4 -p1
%patch 5 -p1
%patch 6 -p0
%patch 7 -p1
%patch 8 -p1
%patch 9 -p1 -b.python3
%patch 10 -p1 -b.scons3
%patch 11 -p1 -b.fixtabs
%patch 12 -p1 -b.bool

sed -i -e '3d' -e '12d' data/glob2.desktop
sed -i s#"Icon=glob2-icon-48x48"#"Icon=glob2"# data/glob2.desktop

chmod -x campaigns/Tutorial_Campaign.txt
sed -i 's/\r//' campaigns/Tutorial_Campaign.txt

%build
scons %{?_smp_mflags} INSTALLDIR=$RPM_BUILD_ROOT%{_datadir} BINDIR=$RPM_BUILD_ROOT%{_bindir} DATADIR=%{_datadir} CXXFLAGS="%{optflags}" --portaudio=true

%install
scons install --portaudio=true

# Use the dejavu-sans-fonts package to supply the neeeded fonts
ln -f -s $(fc-match -f "%{file}" "sans") $RPM_BUILD_ROOT%{_datadir}/%{name}/data/fonts/sans.ttf

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/
cp -p data/icons/glob2-icon-64x64.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/glob2.png

for f in 128x128 16x16 24x24 32x32 48x48; do
mv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$f/apps/glob2-icon-$f.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/$f/apps/glob2.png
done
rm -rf $RPM_BUILD_ROOT%{_datadir}/glob2/data/icons
find $RPM_BUILD_ROOT%{_datadir} -name *~* -exec rm -rf {} \;

desktop-file-install                                    \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications   \
        --remove-category=Application                   \
        --delete-original                               \
        $RPM_BUILD_ROOT%{_datadir}/applications/glob2.desktop

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
<!--
BugReportURL: https://savannah.nongnu.org/bugs/?43293
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">glob2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>real time strategy game with globs</summary>
  <description>
    <p>
      Globulation 2 is a real time strategy (RTS) game where you use three
      types of globs: workers, scouts, and warriors to wage war on computer
      controlled communites of other
      globs.
      Globulation is unique from other RTS games in that it removes a lot of the
      micromanagement from the gameplay.
      You cannot control the globs directly, only place buildings and let the
      globs do what they do best.
    </p>
  </description>
  <url type="homepage">http://globulation2.org/</url>
  <screenshots>
    <screenshot type="default">http://globulation2.org/images/9/93/Beta3-Battle.jpg</screenshot>
    <screenshot>http://globulation2.org/images/5/5a/Beta2_MoreAttackingEnemy.jpg</screenshot>
    <screenshot>http://globulation2.org/images/6/6a/Beta2_ParticleEffects.jpg</screenshot>
  </screenshots>
</application>
EOF

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}

%changelog
%autochangelog
