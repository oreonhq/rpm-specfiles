%global source0_hash 47776f97fc5e37bd00196cfd2b4f7410d7f4926cbbc74d04b1986f9d60d9d7bd
Name:		fbg2
Version:	0.4
Release:        1%{?dist}
Summary:        A falling block stacking game
License:	GPL-2.0-or-later AND LicenseRef-Callaway-CC-BY-SA
URL:		http://sourceforge.net/projects/fbg/
Source0:        %{name}-%{version}-clean.tar.gz
Source1:	RudySeb_-_russian.ogg
Source2:	README.music
Source3:	fbg2.png
Patch0:		fbg2-0.4-desktop-fix.patch
# oreon:deps
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  radius-engine-devel
BuildRequires:  zip
# /oreon:deps
%description
Falling Block Game is a free, open source block stacking game. The object of 
the game is to move and rotate pieces in order to fill in complete rows. The 
more rows you clear at once, the more points you score! 

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .fix
cp %{SOURCE1} Data/Music/FallingBlockGameSndTrk.ogg
cp %{SOURCE2} .
mv fbg2.png fbg2-small.png
cp %{SOURCE3} .

chmod -x License.txt ChangeLog *.c

%build

%configure
make %{?_smp_mflags}
%install
make install DESTDIR=%{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ryan Lerch <rlerch@redhat.com> -->
<!--
BugReportURL: https://sourceforge.net/p/fbg/feature-requests/12/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">fbg2.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>move the falling blocks to create lines</summary>
  <description>
    <p>
      The Falling Block Game is a game where groups of blocks of certain
      predefined shapes fall from the top of the screen, and the player
      has to rotate and move them to create lines of blocks that then
      disappear when a line is complete.
    </p>
  </description>
  <url type="homepage">http://sourceforge.net/projects/fbg/</url>
  <screenshots>
    <screenshot type="default">http://fbg.sourceforge.net/releases/images/fbg2-v0.4-released/fbgscore2.jpg</screenshot>
  </screenshots>
</application>
EOF
desktop-file-validate %{buildroot}%{_datadir}/applications/fbg2.desktop
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
