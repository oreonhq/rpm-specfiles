%global source0_hash d29ab617b7c0faa56ec4f8f13663c690a1b85e9212dd01717cc214c720d3ff76
Name:           openttd
Version:        15.2
Release:        1%{?dist}
Summary:        Transport system simulation game
License:        GPL-2.0-only AND BSD-3-Clause AND LGPL-2.1-or-later AND MIT AND Zlib
URL:            https://www.openttd.org
Source0:        https://cdn.%{name}.org/%{name}-releases/%{version}/%{name}-%{version}-source.tar.xz
Requires:       hicolor-icon-theme
Provides:       bundled(squirrel) = 2.2.5~openttd
Provides:       bundled(fmt) = 7.1.3
Recommends:     openttd-opengfx => 0.5.0
Recommends:     fluid-soundfont-gm
# oreon:deps
BuildRequires:  SDL2-devel
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  doxygen
BuildRequires:  fluidsynth-devel
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  grfcodec
BuildRequires:  libcurl-devel
BuildRequires:  libicu-devel
BuildRequires:  libpng-devel
BuildRequires:  lzo-devel
BuildRequires:  xz-devel
BuildRequires:  zlib-devel
# /oreon:deps
%description
OpenTTD is modeled after a popular transportation business simulation game
by Chris Sawyer and enhances the game experience dramatically. Many features
were inspired by TTDPatch while others are original.

%package docs
Summary:        Documentation for OpenTTD
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
%description docs
Development documentation for OpenTTD. Includes information on how to program
the AI.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}%{?prever:-%{prever}}

sed -i "s|/usr/share|%{_datadir}|g" src/music/fluidsynth.cpp

%build

%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_BINDIR=bin \
    -DCMAKE_INSTALL_DATADIR=%{_datadir} \
    -DGLOBAL_DIR:PATH=%{_datadir}/%{name}
%cmake_build
%install
%cmake_install
rm -rf $RPM_BUILD_ROOT%{_docdir}
install -dpm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/
cp -a docs/* $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/docs/%{name}.6
desktop-file-install --dir=$RPM_BUILD_ROOT%{_datadir}/applications \
        --add-category=StrategyGame \
        $RPM_BUILD_ROOT%{_datadir}/applications/openttd.desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ankur Sinha <ankursinha@fedoraproject.org> -->
<!--
EmailAddress: alberth@openttd.org
SentUpstream: 2014-09-25
-->
<application>
  <id type="desktop">openttd.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A highly detailed transport simulation game</summary>
  <description>
  <p>
      OpenTTD is a transport tycoon simulation game that enhances the
      original Transport Tycoon game developed by Chris Sawyer.
      The game includes road, air, train and naval transport with a large
      selection of industries and passenger services that need to be provided.
    </p>
  <p>
      The game can be played in both single and multiplayer modes where
      you compete with other transport companies to dominate the markets.
  </p>
  </description>
  <url type="homepage">https://www.openttd.org</url>
  <screenshots>
    <screenshot type="default">https://www.openttd.org/screenshots/1.4-02-opengfx-1920x1200.png</screenshot>
    <screenshot>https://www.openttd.org/screenshots/1.9-darkuk-3.png</screenshot>
  </screenshots>
  <updatecontact>info@openttd.org</updatecontact>
</application>
EOF
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n openttd-docs -f %{oreon_filedir}/openttd-docs.list

%changelog

%autochangelog
