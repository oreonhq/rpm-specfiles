%global source0_hash 23ec0d988bd06475bb2f95f9ab9c04469e0c02347866daa28769b0245836d103

Name:           nazghul
Version:        0.7.1
Release:        41.20120228gitb0a402a%{?dist}
Summary:        A computer role-playing game (CRPG) engine

# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/nazghul/

# Occasionally upstream names things with an underscore.
%global         version_us %(echo %{version} | sed -e 's/\\./_/g')

# Construct cvs checkout tarball with:
#  ./nazghul-make-snapshot %%{cvsdate}
Source0:        nazghul-20120228gitb0a402a.txz
Source1:        haxima-music-license
# Since xcftools is orphaned, this was converted manually from haxima.xcf.  If
# there is ever an update, upstream will hopefully include this icon in the
# tarball.
Source2:        haxima.png
Patch0:         nazghul-desktop.patch
Patch1:         nazghul-format-security.patch
Patch2:         nazghul-armbuild.patch

# For building from a CVS snapshot
BuildRequires: make
BuildRequires:  automake, autoconf, gcc-c++
BuildRequires:  SDL_image-devel, SDL_mixer-devel, desktop-file-utils
BuildRequires:  libpng-devel

%description
Nazghul is an old-school RPG engine modeled after those made in the
heyday of top-down, 2d tile-based graphics. It is specifically modeled
after Ultima V.

%package -n haxima
Summary:        A full-featured role-playing game for the Nazghul engine
# The music files installed in /usr/share/nazghul/haxima/music have been
# relicensed as CC-BY-SA-2.0.   See the
# haxima-music-license file for details. The rest of the package is GPL-2.0-or-later.
License:        GPL-2.0-or-later AND CC-BY-SA-2.0
Requires:       nazghul = %{version}
Provides:       nazghul-haxima = %{version}-%{release}
Obsoletes:      nazghul-haxima < 0.6.0-8

%description -n haxima
A complete, playable and full-featured role playing game which runs
under the Nazghul CRPG engine.

You must install Nazghul in order to play Haxima.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}

# clean up CVS directories left in the source tarball
find . -depth -type d -name CVS -exec rm -rf {} \;

# Fix line endings
sed -i -e 's/\r//' doc/engine_extension_and_design/my_TODO.2004.05.05.txt

mv doc/* .

cp %SOURCE1 .

%build
export CFLAGS="-std=c++14 $RPM_OPT_FLAGS"
./autogen.sh
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

mv %{buildroot}/%{_bindir}/haxima.sh %{buildroot}/%{_bindir}/haxima

desktop-file-install \
    --dir %{buildroot}/%{_datadir}/applications \
    --add-category X-Fedora                     \
    haxima.desktop

install -D -m 644 %SOURCE2 %{buildroot}/%{_datadir}/pixmaps/haxima.png

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/haxima.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/nazghul/support-requests/5/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">haxima.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Top view 2D role playing game</summary>
  <description>
    <p>
      Haxima is a 2D role playing game (RPG) that runs on the Nazghul engine.
      You start out as a defenseless wanderer, you have to equip yourself,
      learn spells, and travel the land completing quests.
    </p>
  </description>
  <url type="homepage">http://myweb.cableone.net/gmcnutt/nazghul.html</url>
  <screenshots>
    <screenshot type="default">https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/haxima/a.png</screenshot>
    <screenshot>https://raw.githubusercontent.com/hughsie/fedora-appstream/master/screenshots-extra/haxima/b.png</screenshot>
  </screenshots>
</application>
EOF

%files
%{_bindir}/nazghul
%dir %{_datadir}/nazghul
%doc AUTHORS ChangeLog COPYING NEWS GAME_RULES GHULSCRIPT
%doc MAP_HACKERS_GUIDE engine_extension_and_design world_building

%files -n haxima
%{_bindir}/haxima
%{_datadir}/nazghul/haxima
%{_datadir}/appdata/*.appdata.xml
%{_datadir}/applications/*haxima.desktop
%{_datadir}/pixmaps/haxima.png
%doc USERS_GUIDE haxima-music-license

%changelog
%autochangelog
