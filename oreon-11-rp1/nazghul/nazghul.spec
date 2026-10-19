%global source0_hash 23ec0d988bd06475bb2f95f9ab9c04469e0c02347866daa28769b0245836d103
Name:           nazghul
Version:        0.7.1
Release:        1%{?dist}
Summary:        A computer role-playing game (CRPG) engine
License:        GPL-2.0-or-later
URL:            http://sourceforge.net/projects/nazghul/
%global         version_us %(echo %{version} | sed -e 's/\\./_/g')
Source0:        nazghul-20120228gitb0a402a.txz
Source1:        haxima-music-license
Source2:        haxima.png
Patch0:         nazghul-desktop.patch
Patch1:         nazghul-format-security.patch
Patch2:         nazghul-armbuild.patch
# oreon:deps
BuildRequires:  SDL_image-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc-c++
BuildRequires:  libpng-devel
BuildRequires:  make
# /oreon:deps
%description
Nazghul is an old-school RPG engine modeled after those made in the
heyday of top-down, 2d tile-based graphics. It is specifically modeled
after Ultima V.

%package -n haxima
Summary:        A full-featured role-playing game for the Nazghul engine
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
%oreon_autofiles haxima usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n haxima -f %{oreon_filedir}/haxima.list

%changelog

%autochangelog
