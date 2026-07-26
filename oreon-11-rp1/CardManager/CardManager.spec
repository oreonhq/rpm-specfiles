%global source0_hash 8cf09a04a1107ef8fb2bf8249fa88618cb842cb1ff4a82e0f943b059f1effcc2

Name:           CardManager
Version:        3
Release:        37%{?dist}
Summary:        Java application to allows you to play any, especially collectible, card game

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://cardmanager.wz.cz/
Source0:        http://cardmanager.wz.cz/CardManager_sources%{version}.zip
Source1:        %{name}.appdata.xml
Patch0:         removeManifestEntries.patch
Patch1:         jdk8-javadoc.patch
Patch2:         bumpJdk.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  jpackage-utils
BuildRequires:  java-25-devel
BuildRequires:  ant-openjdk25 
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Requires:       java-25

%description
This is free, open source multiplatform (java) application which allows you to
 play ANY card game. 
The game is designed especially to play collectible card games like Magic the
 Gathering or Doomtrooper over network.
To play those games you need to own (scanned) images of card, which are not part
 of this package.
Some can be easily downloadable from internet, but be aware of copyrights.
The default deck and background is free of copyright
Also please feel free to add your own backgrounds to 
~/CardManager/data/backgrounds and of course enhance
collection under ~/CardManager/collection

%package javadoc
Summary:        Javadocs for %{name}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c CardManager
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch -P0
%patch -P1
%patch -P2

%build

ant

%install

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  CardManager.desktop
cp -p ./CardManager.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./FedoraLauncher.sh $RPM_BUILD_ROOT%{_bindir}/CardManager
#end launcher

#appdata
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p dist/%{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r data $RPM_BUILD_ROOT/%{_datadir}/%{name}/
cp -r collection $RPM_BUILD_ROOT/%{_datadir}/%{name}/

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -r dist/javadoc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%{_datadir}/pixmaps/CardManager.png
%{_datadir}/applications/CardManager.desktop
%{_datadir}/%{name}
%attr(755,root,root) %{_bindir}/CardManager
%{_javadir}/*
%doc license.txt
%{_datadir}/appdata/%{name}.appdata.xml

%files javadoc
%{_javadocdir}/%{name}
%doc license.txt

%changelog
%autochangelog
