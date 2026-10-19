%global source0_hash none
Name:           freecol
Version:        1.2.0
Release:        1%{?dist}
Summary:        Turn-based multi-player strategy game
License:        GPL-1.0-or-later
URL:            http://www.freecol.org/
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.sh
Source2:        %{name}.desktop
Source3:        freecol.appdata.xml
Source4:        %{name}-imperator.metainfo.xml
Source5:        Imperator.ttf
Source6:        %{name}.6
Patch0:         freecol-1.1.0-no-classpath-in-MF.patch
Patch1:         freecol-fix-makeindex-invocation.patch
Patch2:         freecol-source-encoding.patch
Patch3:         freecol-1.2.0-commons-cli-1.5.0.patch
Patch4:         freecol-1.1.0-java-17.patch
Patch5:         freecol-1.2.0-findbugs-annotations.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25 >= 1:17.0.0 jpackage-utils hicolor-icon-theme
Requires:       apache-commons-cli >= 1.5.0 cortado jorbis miglayout >= 5.3
Requires:       %{name}-shadowedblack-fonts
# oreon:deps
BuildRequires:  ImageMagick
BuildRequires:  ant-openjdk25
BuildRequires:  apache-commons-cli
BuildRequires:  cortado
BuildRequires:  desktop-file-utils
BuildRequires:  fontpackages-devel
BuildRequires:  java-25-devel
BuildRequires:  jorbis
BuildRequires:  miglayout
BuildRequires:  tex(latex)
BuildRequires:  tex(tex4ht.sty)
BuildRequires:  xml-commons-apis
BuildRequires:  xml-commons-resolver
# /oreon:deps
%description
FreeCol is a turn-based, multi-player, X based strategy game. FreeCol
has compatible rules with the Colonization game.

%package manual
Summary:        User Documentation for freecol
Requires:       %{name} = %{version}-%{release}
%description manual
User Documentation for freecol.

%package shadowedblack-fonts
Summary:        Gothic font with drop shadows
License:        GPL-2.0-or-later
Requires:       fontpackages-filesystem
%description shadowedblack-fonts
A gothic font with drop shadows originally created by Paul Lloyd in 2002,
extended by the freecol project to include most accented latin characters.

%package imperator-fonts
Summary:        Gothic font
License:        GPL-2.0-or-later
Requires:       fontpackages-filesystem
%description imperator-fonts
A gothic font originally created by Paul Lloyd in 2002, extended by the freecol
project to include most accented latin characters.

%prep

%setup -q
%patch -P 0 -p1
%patch -P 1 -p1
%patch -P 2 -p1
%patch -P 3 -p1
%patch -P 4 -p1
%patch -P 5 -p1
# freecol normally builds against copies shipped with the source. Remove these
# and symlink to the system versions of these.
rm jars/*
ln -s %{_javadir}/commons-cli.jar jars/commons-cli-1.5.jar
ln -s %{_javadir}/cortado.jar jars/cortado-0.6.0.jar
ln -s %{_javadir}/jogg.jar jars/jogg-0.0.17.jar
ln -s %{_javadir}/jorbis.jar jars/jorbis-0.0.17.jar
ln -s %{_javadir}/miglayout-core.jar jars/miglayout-core-5.3.jar
ln -s %{_javadir}/miglayout-swing.jar jars/miglayout-swing-5.3.jar

%build

ant clean package manual
convert packaging/common/freecol.{xpm,png}
convert packaging/common/freecol_64x64.{xpm,png}
convert -resize 96x96 packaging/common/freecol_{90x90.xpm,96x96.png}
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_javadir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man6
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/96x96/apps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
mkdir -p $RPM_BUILD_ROOT%{_fontdir}
install -p -m 644 FreeCol.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -p -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/%{name}
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE2}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/appdata
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_fontdir}
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{_mandir}/man6
cp -a data $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/data/base/resources/fonts/ShadowedBlack.ttf \
  $RPM_BUILD_ROOT%{_fontdir}
ln -s ../../../../../fonts/freecol/ShadowedBlack.ttf \
  $RPM_BUILD_ROOT%{_datadir}/%{name}/data/base/resources/fonts/ShadowedBlack.ttf
install -p -m 644 packaging/common/freecol.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/freecol.png
install -p -m 644 packaging/common/freecol_64x64.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/freecol.png
install -p -m 644 packaging/common/freecol_96x96.png \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/96x96/apps/freecol.png
install -p -m 644 packaging/common/freecol.svg \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n freecol-manual -f %{oreon_filedir}/freecol-manual.list
%files -n freecol-shadowedblack-fonts -f %{oreon_filedir}/freecol-shadowedblack-fonts.list
%files -n freecol-imperator-fonts -f %{oreon_filedir}/freecol-imperator-fonts.list

%changelog

%autochangelog
