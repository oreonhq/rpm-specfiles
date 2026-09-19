%global source0_hash daf8732c229a4cc04f460514bff1ba05171faada9e19575c72a50a914f2352e3

Name:           garden
Version:        1.0.9
Release:        25%{?dist}
Summary:        An innovative old-school 2D vertical shoot-em-up

License:        GPL-3.0-or-later
URL:            http://garden.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
#Patch0:         garden-dso.patch
#Patch1:         garden-printf-format.patch
Patch2:         garden-1.0.8-inline.patch

BuildRequires:  allegro-devel
BuildRequires:  desktop-file-utils
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  libtool
BuildRequires: make
Requires:       allegro

%description
Garden of colored lights is an old school 2D vertical shoot-em-up with some
innovative elements. Innovative graphics, soundtrack and game concept. The
game itself is very challenging and as you progress, you will understand that
you are dealing with a true piece of art...

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

# patch for DSO-linking
# https://sourceforge.net/tracker/?func=detail&aid=2982590&group_id=242667&atid=1121672
#%%patch0 -p1 -b .dso
#%%patch1 -p0 -b .format
%patch -P2 -p1

%build
autoreconf -if
export CPPFLAGS="$CPPFLAGS -fcommon"
%configure 
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

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
<!-- Copyright 2014 Tim Waugh <twaugh@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/garden/feature-requests/4/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">garden.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Choose your equipment and fly your ship past the enemies</summary>
  <description>
    <p>
      In garden of coloured lights you must fly as far as you can while enemies
      attack.
      You choose how to equip the ship, depending on your strategy.
    </p>
    <p>
      The futuristic landscape scrolls upwards while strange plant-like enemies
      engage your ship in various ways.
      There are boss enemies to kill in each stage.
    </p>
  </description>
  <url type="homepage">http://garden.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://garden.sourceforge.net/drupal/sites/default/files/images/stage1_1.png</screenshot>
    <screenshot>http://garden.sourceforge.net/drupal/sites/default/files/images/stage1_2.png</screenshot>
    <screenshot>http://garden.sourceforge.net/drupal/sites/default/files/images/stage0_0.png</screenshot>
  </screenshots>
</application>
EOF

desktop-file-validate \
%{buildroot}%{_datadir}/applications/%{name}.desktop

%files
%license COPYING
%doc README NEWS AUTHORS ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop

%changelog
%autochangelog
