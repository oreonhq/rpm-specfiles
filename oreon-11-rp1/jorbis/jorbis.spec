%global source0_hash eb019a6469085212144be8d19a92ad579349511989ef8bb1d3e1b0ef8d2158d8

Name:           jorbis
Version:        0.0.17
Release:        40%{?dist}
Summary:        Pure Java Ogg Vorbis Decoder
URL:            http://www.jcraft.com/jorbis/
License:        LGPL-2.0-or-later
Source0:        http://www.jcraft.com/jorbis/%{name}-%{version}.zip
# Some fixes from the jorbis copy embedded in cortada. I've mailed upstream
# asking them to integrate these, for more info also see:
# https://trac.xiph.org/ticket/1565
# Note that although the original git headers were left in place for reference
# the actual patches have been rebased to 0.0.17 !
Patch0:         jorbis-0.0.17-cortado-fixes.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  java-25-devel
Requires:       java-25-headless
# We used to also package the comment editor example, but that is not so
# useful to end users (esp. the passing of cmdline args as java defines)
Obsoletes:      %{name}-comment <= 0.0.17-3

%description
JOrbis is a pure Java Ogg Vorbis decoder.

%package javadoc
Summary:        Java docs for jorbis

%description javadoc
This package contains the API documentation for jorbis.

%package player
Summary:        Java applet for playing ogg-vorbis files from a browser
# Automatically converted from old format: GPLv2+ - review is highly recommended.
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

%files
%doc ChangeLog COPYING.LIB README
%{_javadir}/jogg.jar
%{_javadir}/jorbis.jar

%files javadoc
%doc COPYING.LIB
%{_javadocdir}/%{name}

%files player
%doc player/JOrbisPlayer.html
%{_javadir}/JOrbisPlayer.jar

%changelog
%autochangelog
