%global source0_hash none
%global forgeurl https://github.com/openjdk/jfx25u
%global openjfxdir %{_jvmdir}/%{name}
%global rtdir jfx25u-25.0.2-3
Name:           openjfx
Epoch:          3
Version:        25.0.5+3
Release:        1%{?dist}
Summary:        Rich client application platform for Java
%forgemeta
License:        GPL-2.0-only WITH Classpath-exception-2.0 AND BSD-2-Clause AND BSD-3-Clause
URL:            %{forgeurl}
Source0:        %{forgeurl}/archive/v%{version}/jfx25u-%{version}.tar.gz
Source1:        pom-base.xml
Source2:        pom-controls.xml
Source3:        pom-fxml.xml
Source4:        pom-graphics.xml
Source5:        pom-graphics_antlr.xml
Source6:        pom-graphics_decora.xml
Source7:        pom-graphics_compileJava.xml
Source8:        pom-graphics_compileJava-decora.xml
Source9:        pom-graphics_compileJava-java.xml
Source10:       pom-graphics_compileJava-prism.xml
Source11:       pom-graphics_graphics.xml
Source12:       pom-graphics_libdecora.xml
Source13:       pom-graphics_libglass.xml
Source14:       pom-graphics_libglassgtk3.xml
Source15:       pom-graphics_libjavafx_font.xml
Source16:       pom-graphics_libjavafx_font_freetype.xml
Source17:       pom-graphics_libjavafx_font_pango.xml
Source18:       pom-graphics_libjavafx_iio.xml
Source19:       pom-graphics_libprism_common.xml
Source20:       pom-graphics_libprism_es2.xml
Source21:       pom-graphics_libprism_sw.xml
Source22:       pom-graphics_prism.xml
Source23:       pom-media.xml
Source24:       pom-openjfx.xml
Source25:       pom-swing.xml
Source26:       pom-swt.xml
Source27:       pom-web.xml
Source28:       build.xml
Source29:       pom-jdk.jsobject.xml
Source30:       pom-jfx.incubator.input.xml
Source31:       pom-jfx.incubator.richtext.xml	
Patch0:         openjfx-disable-mtl.patch
ExclusiveArch:  %{java_arches}
Requires:       java-25-headless
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gperf
BuildRequires:  java-25-devel
BuildRequires:  javapackages-tools
BuildRequires:  libstdc++-static
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr4-maven-plugin)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:native-maven-plugin)
BuildRequires:  mvn(org.eclipse.swt:swt)
BuildRequires:  perl
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xxf86vm)
BuildRequires:  python3
# /oreon:deps
%description
JavaFX/OpenJFX is a set of graphics and media APIs that enables Java
developers to design, create, test, debug, and deploy rich client
applications that operate consistently across diverse platforms.

The media module have been removed due to missing dependencies.

%global debug_package %{nil}

%prep

%autosetup -p1 -n %{rtdir}

#Drop *src/test folders
rm -rf modules/javafx.{base,controls,fxml,graphics,media,swing,swt,web}/src/test/
rm -rf modules/jfx.incubator.{input,richtext}/src/test/

#prep for javafx.graphics
cp -a modules/javafx.graphics/src/jslc/antlr modules/javafx.graphics/src/main/antlr3
cp -a modules/javafx.graphics/src/main/resources/com/sun/javafx/tk/quantum/*.properties modules/javafx.graphics/src/main/java/com/sun/javafx/tk/quantum

find -name '*.class' -delete
find -name '*.jar' -delete

#copy maven files
cp -a %{_sourcedir}/pom-*.xml .
mv pom-openjfx.xml pom.xml

for MODULE in base controls fxml graphics media swing swt web
do
    mv pom-$MODULE.xml ./modules/javafx.$MODULE/pom.xml
done

for MODULE in jdk.jsobject jfx.incubator.input jfx.incubator.richtext
do
    mv pom-$MODULE.xml ./modules/$MODULE/pom.xml
done

mkdir ./modules/javafx.graphics/mvn-{antlr,decora,compileJava,graphics,libdecora,libglass,libglassgtk3,libjavafx_font,libjavafx_font_freetype,libjavafx_font_pango,libjavafx_iio,libprism_common,libprism_es2,libprism_sw,prism}
for GRAPHMOD in antlr decora compileJava graphics libdecora libglass libglassgtk3 libjavafx_font libjavafx_font_freetype libjavafx_font_pango libjavafx_iio libprism_common libprism_es2 libprism_sw prism
do
    mv pom-graphics_$GRAPHMOD.xml ./modules/javafx.graphics/mvn-$GRAPHMOD/pom.xml
done

mkdir ./modules/javafx.graphics/mvn-compileJava/mvn-{decora,java,prism}
for SUBMOD in decora java prism
do
    mv pom-graphics_compileJava-$SUBMOD.xml ./modules/javafx.graphics/mvn-compileJava/mvn-$SUBMOD/pom.xml
done

#set VersionInfo
cp -a %{_sourcedir}/build.xml .
ant -f build.xml

mkdir -p ./modules/javafx.graphics/mvn-antlr/src/main
mv ./modules/javafx.graphics/src/main/antlr3 ./modules/javafx.graphics/mvn-antlr/src/main/antlr4

rm -rf ./modules/javafx.web/src/main/native/Source/WTF/icu
rm -rf ./modules/javafx.web/src/main/native/Source/ThirdParty/icu

%build

export CFLAGS="${RPM_OPT_FLAGS}"
export CXXFLAGS="${RPM_OPT_FLAGS}" 
%mvn_build --skip-javadoc
%install
install -d -m 755 %{buildroot}%{openjfxdir}
cp -a modules/javafx.{base,controls,fxml,media,swing,swt,web}/target/*.jar %{buildroot}%{openjfxdir}
cp -a modules/jdk.jsobject/target/*.jar %{buildroot}%{openjfxdir}
cp -a modules/jfx.incubator.{input,richtext}/target/*.jar %{buildroot}%{openjfxdir}
cp -a modules/javafx.graphics/mvn-compileJava/mvn-java/target/*.jar %{buildroot}%{openjfxdir}
cp -a modules/javafx.graphics/mvn-lib{decora,javafx_font,javafx_font_freetype,javafx_font_pango,glass,glassgtk3,javafx_iio,prism_common,prism_es2,prism_sw}/target/*.so %{buildroot}%{openjfxdir}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
