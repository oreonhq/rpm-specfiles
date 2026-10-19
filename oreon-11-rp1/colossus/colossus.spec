%global source0_hash d6797387e6931abd57eff98adffd3d3f4b2e27800ffe1f7ff76d0f8b0d5c197e
Name:           colossus
%global         rev        5331
%global         revdate    20130917
Version:        0.14.0
%global         branch    %{nil}
Release:        1%{?dist}
Summary:        Allows people to play Titan against each other or AIs
License:        GPL-2.0-only
URL:            http://colossus.sourceforge.net/
Source0:        %{name}--%{revdate}-%{rev}.tar.gz
Source1:        colossus-gen-tarball.sh
Source2:        colossus-rev.xsl
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25
Requires:       jpackage-utils
Requires:       jdom
Requires(post):  coreutils
Requires(postun):  coreutils
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  desktop-file-utils
BuildRequires:  java-25-devel
BuildRequires:  jdom
BuildRequires:  jpackage-utils
BuildRequires:  zip
# /oreon:deps
%description
Colossus allows people to play Titan
(http://www.boardgamegeek.com/boardgame/103) and several Titan variants, hot
seat or via a network. Several different AIs are provided that can play instead
of humans.

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{branch}-%{revdate}-%{rev}

%build

cp /dev/null local_build.properties
echo "libs.dir=%{_javadir}" >> local_build.properties
echo "source.level=1.8" >> local_build.properties
echo "target.level=1.8" >> local_build.properties
mkdir -p build/ant/classes/META-INF
cat <<EOF > build/ant/classes/META-INF/build.properties
release.version=%{version}
svn.revision.max-with-flags=%{rev}
build.timestamp=%{revdate}
username=rpmbuild
EOF
ant jar
zip -d Colossus.jar META-INF/MANIFEST.MF
cat <<EOF > fixup.xml
<?xml version="1.0"?>
<!-- Replace manifest with one without a classpath -->
<project name="Colossus" default="fixup" basedir=".">
  <target name="fixup"
  description="Remove classpath from manifest">
    <jar jarfile="Colossus.jar" update="true">
      <manifest>
        <attribute name="Main-Class"
        value="net.sf.colossus.appmain.Start" /> 
      </manifest>
    </jar>
  </target>
</project>
EOF
ant -f fixup.xml
ant -lib %{_javadir}/jdom.jar javadoc
echo -e "#!/bin/sh\njava -cp %{_javadir}/jdom.jar:%{_javadir}/colossus.jar net.sf.colossus.appmain.Start" > %{name}
cat <<EOF > %{name}.desktop
[Desktop Entry]
Name=Colossus
GenericName=Strategy Game
Comment=Multiplayer turned based fantasy game with AIs available
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF
%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 Colossus.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -D -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -m 644 core/src/main/resource/icons/ColossusIcon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications %{name}.desktop
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}
cp -rpv build/ant/javadoc $RPM_BUILD_ROOT%{_javadocdir}/%{name}
chmod -R og=u-w $RPM_BUILD_ROOT%{_javadocdir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
cat > $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml <<EOF
<?xml version="1.0" encoding="UTF-8"?>
<!-- Copyright 2014 Ravi Srinivasan <ravishankar.srinivasan@gmail.com> -->
<!--
BugReportURL: https://sourceforge.net/p/colossus/feature-requests/225/
SentUpstream: 2014-09-24
-->
<application>
  <id type="desktop">colossus.desktop</id>
  <metadata_license>CC0-1.0</metadata_license>
  <summary>A fantasy board game with strategic and tactical battle elements</summary>
  <description>
    <p>
      Colossus is a clone of Avalon Hill's "Titan" Board game.
    </p>
    <p>
      It is a fantasy board game where you lead an army of mythological creatures
      against other players.
    </p>
  </description>
  <url type="homepage">http://colossus.sourceforge.net/</url>
  <screenshots>
    <screenshot type="default">http://colossus.sourceforge.net/pics/screenshots/Colossi.jpg</screenshot>
  </screenshots>
</application>
EOF
%oreon_autofiles colossus-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n colossus-javadoc -f %{oreon_filedir}/colossus-javadoc.list

%changelog

%autochangelog
