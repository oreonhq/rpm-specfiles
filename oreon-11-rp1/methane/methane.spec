%global source0_hash ac1de7009e638c784b4d413b56a4387be94a31bd5fe3050db7b51e39ccfdd248

Name:           methane
Version:        1.5.1
Release:        39%{?dist}
Summary:        Super Methane Brothers
# Automatically converted from old format: GPLv2+ - review is highly recommended.
License:        GPL-2.0-or-later
URL:            http://methane.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tgz
Source1:        %{name}.desktop
Source2:        %{name}.png
Patch1:         methane-highscore.patch
Patch2:         methane-fullscreen.patch
Patch3:         methane-1.5.1-clanlib-23.patch
Patch4:         methane-1.5.1-gcc5.patch
BuildRequires: make
BuildRequires:  gcc gcc-c++
BuildRequires:  ClanLib-devel >= 2.3 desktop-file-utils
Requires:       hicolor-icon-theme opengl-games-utils

%description
Super Methane Brothers is a platform game converted from the Amiga by
its original author.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

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

# below is the desktop file and icon stuff.
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE1}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -p -m 644 %{SOURCE2} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps

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

%files
%doc authors.txt docs history.txt readme.txt
%license copying.txt
%attr(2755,root,games) %{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_datadir}/%{name}
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
%verify(not md5 size mtime) %config(noreplace) %attr(664,root,games) %{_var}/games/%{name}.scores

%changelog
%autochangelog
