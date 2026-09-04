%global source0_hash 6eb7d1a1e6eb294ab3d2ef38d3c4e0c321b4f9e4a92c209eec86af3c6cbe2668

# New versions 0.8+ are built with gradle build system, which is not present in Fedora

%global         gituser         syvaidya
%global         gitname         openstego
# Release 0.7.4 - 2020-06-06
%global         commit          2f4d84f0e38421809fa8213f0fe1028bfc3fa9ed
%global         shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           OpenStego
Version:        0.8.6
Release:        1%{?dist}
Summary:        Free Steganography solution
Summary(fr):    Solution libre pour la steganographie

# Automatically converted from old format: GPLv2 - review is highly recommended.
License:        GPL-2.0-only
#               https://github.com/syvaidya/openstego/releases
URL:            http://openstego.sourceforge.net/index.html
# Source0:      http://downloads.sourceforge.net/project/openstego/openstego/openstego-%%{version}/openstego-src-%%{version}.zip
Source0:        https://github.com/%{gituser}/%{gitname}/archive/%{gitname}-%{version}.tar.gz
Source1:        openstego.desktop
# Patch the ant build script to build only the binary package out of java sources
Patch0:         %{name}-antbuild.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
BuildRequires:  ant-openjdk25 
BuildRequires:  desktop-file-utils
Requires:       java-25-headless
Requires:       jpackage-utils

%description
OpenStego is a tool implemented in Java for generic steganography,
with support for password-based encryption of the data. It supports
plugins for various steganographic algorithms.

%description -l fr
OpenStego est un outil implanté en Java pour la steganographie générique,
avec le support de l'encryption des données basé sur mot de passe. Il
supporte les plugins pour des algorithmes steganographiques variés.

%package javadoc
BuildArch: noarch
Requires:  jpackage-utils
Summary:   Javadoc generated documentation for Openstego
Summary(fr):    Documentation javadoc générée pour Openstego

%description javadoc
Javadoc generated documentation for Openstego.

%description javadoc -l fr
Documentation javadoc générée pour Openstego

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gitname}-%{gitname}-%{version}
%patch -P0 -p 1 -b .antbuild
find . -name *.class -delete
find . -name *.jar -delete
# Delete file for Windows :
rm -f openstego.bat

%build
ant package doc

%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_javadocdir}/openstego
cp -p ./lib/openstego.jar %{buildroot}%{_javadir}/openstego.jar
cp -p ./src/image/ImagesVectorSource.svg %{buildroot}%{_datadir}/pixmaps/openstego.svg
cp -pr ./doc/api/* %{buildroot}%{_javadocdir}/openstego
%jpackage_script com.openstego.desktop.OpenStego "" "" openstego.jar openstego true

# Install openstego.desktop
desktop-file-install                       \
--dir=%{buildroot}%{_datadir}/applications \
%{SOURCE1}

%files
%doc README LICENSE
%{_bindir}/openstego
%{_javadir}/openstego.jar
%{_datadir}/pixmaps/openstego.svg
%{_datadir}/applications/openstego.desktop

%files javadoc
%doc LICENSE
%{_javadocdir}/openstego/

%changelog
%autochangelog
