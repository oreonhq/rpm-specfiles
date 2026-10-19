%global source0_hash ac1de7009e638c784b4d413b56a4387be94a31bd5fe3050db7b51e39ccfdd248
Name:           methane
Version:        1.5.1
Release:        1%{?dist}
Summary:        Super Methane Brothers
License:        GPL-2.0-or-later
URL:            http://methane.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch1:         methane-highscore.patch
Patch2:         methane-fullscreen.patch
Patch3:         methane-1.5.1-clanlib-23.patch
Patch4:         methane-1.5.1-gcc5.patch
Requires:       hicolor-icon-theme opengl-games-utils
# oreon:deps
BuildRequires:  ClanLib-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  make
# /oreon:deps
%description
Super Methane Brothers is a platform game converted from the Amiga by
its original author.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

make CXXFLAGS="$RPM_OPT_FLAGS"
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_var}/games
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}
cp -a resources $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s opengl-game-wrapper.sh $RPM_BUILD_ROOT%{_bindir}/%{name}-wrapper
touch $RPM_BUILD_ROOT%{_var}/games/%{name}.scores
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 William Moreno Reyes <williamjmorenor@gmail.com> -->
<!--
UpstreamURL:  Upstream is dead, private email
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">methane.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>Platform Arcade Game similar to Bubble Bubble</summary>
  <description>
    <p>
      Super Methane Brothers is a platform arcade game Puff and Blow each have a
      Methane Gas Gun which fires a cloud of immobilising gas.
      If this comes into contact with a bad guy, he will be absorbed into the gas
      and then float around the screen for a limited time.
      Bad guys are harmless in this state.
      Puff and Blow must suck the floating gas clouds into their guns and blast
      them out against a vertical surface.
      bThe Bad guys then turn into bonuses which can be collected.
    </p>
  </description>
  <url type="homepage">http://methane.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://methane.sourceforge.net/gamepic.gif</screenshot>
  </screenshots>
</application>
EOF
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
