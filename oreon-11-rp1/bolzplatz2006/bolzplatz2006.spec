%global source0_hash d993f118fdf2343c5bc4e891b6b5f39c70b201c39419e0a6b0e2260b5875ec5b
Name:           bolzplatz2006
Version:        1.0.3
Release:        66%{?dist}
Summary:        Slam Soccer 2006 is a funny football game in 3D-comic-style
Summary(fr):    Coup de Foot 2006 est un jeu comique en 3D
Summary(de):    Bolzplatz 2006 ist ein spaßiges Fußballspiel im 3D-Comic-Stil
License:        GPL-2.0-or-later
URL:            http://www.bolzplatz2006.de
Source0:        http://downloads.sourceforge.net/bp2k6/%{name}-%{version}-src.zip
Source1:        %{name}.png
Source2:        %{name}.sh
Source3:        %{name}-settings.sh
Source4:        %{name}.desktop
Source5:        %{name}.appdata.xml
Source6:        %{name}-jirr-no-crash.patch
Source7:        %{name}-functions.sh
Source8:        %{name}.autodlrc
Source9:        input.xml
Patch0:         %{name}-irrlicht.i.patch
Patch1:         %{name}-irrlicht-extra-qualification-error.patch
Patch2:         %{name}-irrlicht-use-systemlibs.patch
Patch3:         %{name}-irrlicht-png-64bit.patch
Patch4:         %{name}-lwjgl-nofmod.patch
Patch5:         %{name}-lwjgl-openal11.patch
Patch6:         %{name}-lwjgl-Makefile.patch
Patch7:         %{name}-no-xrandr.patch
Patch8:         %{name}-versioned-openal.patch
Patch9:         %{name}-1.0.3-libpng15.patch
Patch10:        %{name}-use-system-extgl.patch
Patch11:        %{name}-gcc6.patch
Patch12:        %{name}-openjdk11.patch
Patch13:        %{name}-gcc15.patch
Requires:       sdljava dom4j vecmath1.2 java-25 jpackage-utils
Requires:       hicolor-icon-theme autodownloader
Requires:       openal-soft
ExclusiveArch:  %{java_arches}
# oreon:deps
BuildRequires:  DevIL-devel
BuildRequires:  ant-openjdk25
BuildRequires:  desktop-file-utils
BuildRequires:  dom4j
BuildRequires:  gcc-c++
BuildRequires:  java-25-devel
BuildRequires:  libGLU-devel
BuildRequires:  libXcursor-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXt-devel
BuildRequires:  libXxf86vm-devel
BuildRequires:  libappstream-glib
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libvorbis-devel
BuildRequires:  make
BuildRequires:  sdljava
BuildRequires:  swig
BuildRequires:  vecmath1.2
BuildRequires:  xml-commons-apis
# /oreon:deps
%description
Slam Soccer 2006 is a funny football game in
3D-comic-style - and it's for free!

* Freeware and open source
* Funny 3d-comic-style
* Enthralling stadium atmosphere
* Keyboard and gamepad control
* 2-player mode
* Career and world cup
* Register in the online hall of fame
* Build your own stadium

* 80 teams
* 20 stadiums
* 10 weather conditions
* 50 adboards
* 10 referees
* 9 commentators (5 German, 2 English, 2 French)

* 3 languages: German, English, French

%description -l de
Bolzplatz 2006 ist ein spaßiges Fußballspiel
im 3D-Comic-Stil für lau.

* Kostenlos und Open-Source
* Witzige 3D-Comic-Grafik
* Packende Stadionatmosphäre
* Steuerung mit Tastatur oder Gamepad
* 2-Spieler-Modus
* Karriere und Weltmeisterschaft
* Eintrag in die Hall of Fame
* Baue Dein eigenes Stadion

* 80 Teams
* 20 Stadien
* 10 Wetterverhältnisse
* 50 Werbebanden
* 10 Schiedsrichter
* 9 Kommentatoren (5xDeutsch, 2xEnglisch, 2xFranzösisch)

* 3 Sprachen: Deutsch, Englisch und Französisch

%description -l fr
Coup de Foot 2006 est un jeu comique en 3D.
Gratuit et open-source.

* Graphiques 3D en style cartoon
* Ambiance de stade presqu'originale
* A commander par clavier ou gamepad
* Mode 2 joueurs
* Mode Carrière et Coupe du Monde
* Inscription au Hall of Fame
* Construis tes propres stades

* 80 équipes
* 20 stades
* 10 conditions atmosphériques différentes
* 50 panneaux publicitaires
* 10 arbitres
* 9 commentateurs

* 3 langues: allemand, anglais et français

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -c -p1
cp %{SOURCE6} libsrc/jirr-dev/diff.txt
cp %{SOURCE7} .
sed -i 's/\r//' license.txt
# we use the system versions of these
rm -r libsrc/irrlicht-0.14-patched/libpng libsrc/irrlicht-0.14-patched/zlib \
  libsrc/irrlicht-0.14-patched/jpeglib libsrc/irrlicht-0.14-patched/glext.h

%build

export RPM_OPT_FLAGS="$RPM_OPT_FLAGS -D_GNU_SOURCE"
export JAVA_HOME=/usr/lib/jvm/java-openjdk
%ifarch %{ix86}
export JAVA_ARCH=i386
%endif
%ifarch x86_64
export JAVA_ARCH=amd64
%endif
if [ -z "$JAVA_ARCH" ]; then
  export JAVA_ARCH=%{_arch}
fi
echo "export LD_LIBRARY_PATH=/usr/lib/jvm/jre-openjdk/lib/$JAVA_ARCH" >> \
  %{name}-functions.sh
pushd libsrc/irrlicht-0.14-patched
make %{?_smp_mflags} CPP="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing" \
  CC="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
popd
pushd libsrc/jirr-dev
make CXX="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing -fpermissive" \
  CC="g++ $RPM_OPT_FLAGS -fPIC -fno-strict-aliasing"
popd
pushd libsrc/lwjgl
ant jars
ant compile_native
popd
mkdir classes
javac -d classes -encoding iso-8859-1 \
  -cp `build-classpath dom4j sdljava vecmath1.2`:./libsrc/jirr-dev/lib/irrlicht.jar:./libsrc/lwjgl/libs/lwjgl.jar \
  `find ./src -name '*.java'`
jar cf %{name}.jar -C classes .
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/appdata
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
install -m 644 %{name}.jar libsrc/jirr-dev/lib/irrlicht.jar \
  libsrc/lwjgl/libs/lwjgl.jar $RPM_BUILD_ROOT%{_javadir}/%{name}
install -m 755 libsrc/jirr-dev/libirrlicht_wrap.so \
  libsrc/lwjgl/libs/linux/liblwjgl.so $RPM_BUILD_ROOT%{_libdir}/%{name}
install -m 755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT%{_bindir}/%{name}-settings
install -p -m 644 %{SOURCE1} \
  $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/128x128/apps
desktop-file-install --dir $RPM_BUILD_ROOT%{_datadir}/applications %{SOURCE4}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{_datadir}/appdata
appstream-util validate-relax --nonet \
  $RPM_BUILD_ROOT%{_datadir}/appdata/%{name}.appdata.xml
install -p -m 644 %{name}-functions.sh %{SOURCE8} %{SOURCE9} \
  $RPM_BUILD_ROOT%{_datadir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
