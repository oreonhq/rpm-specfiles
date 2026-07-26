%global source0_hash 70662b1bb03815f879d4ac91f94a5e5aeec0e347aac48f20e0b79f048b35f248

Name:           barrage
Version:        1.0.7
Release:        9%{?dist}
Summary:        Kill and destroy as many targets as possible within 3 minutes

License:        GPL-2.0-or-later
URL:            http://lgames.sourceforge.net/index.php?project=Barrage
Source0:        http://downloads.sourceforge.net/lgames/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:	%{name}.desktop
Patch0:         barrage-1.0.2-spelling.patch
Patch1:         barrage-1.0.5-hiscore.patch

Requires:       hicolor-icon-theme
BuildRequires:  gcc
BuildRequires:  SDL-devel SDL_mixer-devel desktop-file-utils
BuildRequires: make

%description
Barrage is a rather violent action game with the objective to kill
and destroy as many targets as possible within 3 minutes. The player
controls a gun that may either fire small or large grenades at
soldiers, jeeps and tanks. It is a very simple gameplay though it is
not that easy to get high scores.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p0
%patch -P1 -p0
# add Icon to desktop file
echo Icon=barrage >> barrage.desktop

%build
export CFLAGS="$CFLAGS -std=gnu17"
%configure
find . -type f -name 'Makefile' | xargs sed -i s/-Werror=format-security//g
%make_build %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# below the desktop file and icon stuff
desktop-file-install %{SOURCE2} \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        $RPM_BUILD_ROOT/%{_datadir}/applications/%{name}.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps

install -p -m 0644 %{SOURCE1} \
           $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/%{name}.png

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
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/lgames/support-requests/2/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">barrage.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fast paced action game where you shoot down as many targets as possible</summary>
  <description>
    <p>
      Barrage is a fast paced shooter game where the objective is to destroy
      targets like soldiers, tanks and jeeps within 3 minutes.
    </p>
    <p>
      The player controls a gun that shoots small and large grenades at fast
      moving targets and you need to manage your aim, ammo and re-load times carefully.
    </p>
  </description>
  <url type="homepage">http://lgames.sourceforge.net/index.php?project=Barrage</url>
  <screenshots>
    <screenshot type="default">http://lgames.sourceforge.net/Barrage/ss1.jpg</screenshot>
    <screenshot>http://lgames.sourceforge.net/Barrage/ss0.jpg</screenshot>
    <screenshot>http://lgames.sourceforge.net/Barrage/ss2.jpg</screenshot>
  </screenshots>
</application>
EOF

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/barrage48.gif
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/barrage48.png

%files
%license COPYING
%doc AUTHORS BUGS ChangeLog README
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_var}/games/barrage.hscr

%changelog
%autochangelog
