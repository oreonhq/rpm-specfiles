%global source0_hash eb019a6469085212144be8d19a92ad579349511989ef8bb1d3e1b0ef8d2158d8
Name:           jorbis
Version:        0.0.17
Release:        1%{?dist}
Summary:        Pure Java Ogg Vorbis Decoder
URL:            http://www.jcraft.com/jorbis/
License:        LGPL-2.0-or-later
Source0:        http://www.jcraft.com/jorbis/%{name}-%{version}.zip
Patch0:         jorbis-0.0.17-cortado-fixes.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25-headless
Obsoletes:      %{name}-comment <= 0.0.17-3
# oreon:deps
BuildRequires:  java-25-devel
# /oreon:deps
%description
JOrbis is a pure Java Ogg Vorbis decoder.

%package javadoc
Summary:        Java docs for jorbis
%description javadoc
This package contains the API documentation for jorbis.

%package player
Summary:        Java applet for playing ogg-vorbis files from a browser
License:        GPL-2.0-or-later
Requires:       java-25
Requires:       %{name} = %{version}-%{release}
%description player
This package contains JOrbisPlayer a simple java applet for playing
ogg-vorbis files from a browser.
See %{_docdir}/%{name}-player/JOrbisPlayer.html for
an example how to embed and use the applet.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1

%build

javac com/jcraft/jogg/*.java com/jcraft/jorbis/*.java player/*.java
jar cf jogg.jar com/jcraft/jogg/*.class
jar cf jorbis.jar com/jcraft/jorbis/*.class
jar cf JOrbisPlayer.jar player/*.class
javadoc -d doc -public com/jcraft/*/*.java
%install
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -a *.jar $RPM_BUILD_ROOT%{_javadir}
cp -a doc $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jorbis-javadoc -f %{oreon_filedir}/jorbis-javadoc.list
%files -n jorbis-player -f %{oreon_filedir}/jorbis-player.list

%changelog

%autochangelog
