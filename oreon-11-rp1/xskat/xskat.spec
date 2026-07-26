%global source0_hash 8ba52797ccbd131dce69b96288f525b0d55dee5de4008733f7a5a51deb831c10

%global           upstream_version 4.0

Summary:          The card game Skat
Name:             xskat
# Upstream License requires to alter the version number
# for re-distribution
Version:          %{upstream_version}.0
Release:          39%{?dist}
# https://fedoraproject.org/wiki/Licensing/XSkat_License
License:          XSkat
Source0:          http://www.xskat.de/xskat-%{upstream_version}.tar.gz
Source1:          xskat.desktop
Patch0:           xskat-c99.patch
URL:              http://www.xskat.de/xskat.html
# xskat requires an 10x20 font
Requires:         xorg-x11-fonts-misc
BuildRequires:    make
BuildRequires:    gcc
BuildRequires:    imake
BuildRequires:    libX11-devel
BuildRequires:    desktop-file-utils
BuildRequires:    ImageMagick
BuildRequires:    libappstream-glib

%description
XSkat lets you play the card game Skat as defined by the official Skat Order.

Features:
    * Single- and multiplayer mode
    * Playing over LAN or IRC
    * Game lists and logs
    * Three types of scoring
    * English or German text
    * German or French suited cards
    * Selectable computer playing strength
    * Pre-definable card distributions
    * Variations: Ramsch, Bock, Kontra & Re, ... 

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{upstream_version}

# fix encoding
iconv -f iso8859-1 -t utf-8 CHANGES-de > CHANGES-de.conv && \
touch -r CHANGES-de CHANGES-de.conv && \
mv -f CHANGES-de.conv CHANGES-de

iconv -f iso8859-1 -t utf-8 README-de > README-de.conv && \
touch -r README-de README-de.conv && \
mv -f README-de.conv README-de

iconv -f iso8859-1 -t utf-8 README.IRC-de > README.IRC-de.conv && \
touch -r README.IRC-de README.IRC-de.conv && \
mv -f README.IRC-de.conv README.IRC-de

%build
%configure
make CDEBUGFLAGS="-std=c99 %{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT MANDIR=%{_mandir}/man6 MANSUFFIX=6 install install.man
install -d $RPM_BUILD_ROOT%{_mandir}/de/man6
mv $RPM_BUILD_ROOT%{_mandir}/man6/xskat-de.6 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6
chmod 644 $RPM_BUILD_ROOT%{_mandir}/man6/xskat.6*
chmod 644 $RPM_BUILD_ROOT%{_mandir}/de/man6/xskat.6*

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
desktop-file-install \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications \
  %{SOURCE1}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
convert icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm
touch -r icon.xbm $RPM_BUILD_ROOT%{_datadir}/pixmaps/xskat.xpm

# Register as an application to be visible in the software center
#
# NOTE: It would be *awesome* if this file was maintained by the upstream
# project, translated and installed into the right place during `make install`.
#
# See http://www.freedesktop.org/software/appstream/docs/ for more details.
#

mkdir -p $RPM_BUILD_ROOT%{_metainfodir}
cat > $RPM_BUILD_ROOT%{_metainfodir}/xskat.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
EmailAddress: m@il.xskat.de
SentUpstream: 2014-09-25
-->
<component type="desktop">
  <id>xskat.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A trick taking card game popular in Germany</summary>
  <name>XSkat</name>
  <description>
    <p>
      XSkat is a trick taking card game that is popular in Germany.
      It has single and multiplayer (IRC, LAN) options.
    </p>
  </description>
  <url type="homepage">http://www.xskat.de/xskat.html</url>
</component>
EOF

%check
# Check the AppData add-on to comply with guidelines.
appstream-util validate-relax --nonet $RPM_BUILD_ROOT%{_metainfodir}/*.xml

%files
%doc README* CHANGES*
%{_bindir}/xskat
%{_mandir}/man6/xskat.6.gz
%lang(de) %{_mandir}/de/man6/xskat.6.gz
%{_metainfodir}/%{name}.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/%{name}.xpm

%changelog
%autochangelog
