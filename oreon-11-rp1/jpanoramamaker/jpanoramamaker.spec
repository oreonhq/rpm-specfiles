%global source0_hash a9ce56717e11b9acabdde15235c267c2f33593e803a9175a3b99682b29616e9e

%global majorv 5
%global minorv 6

Name:           jpanoramamaker
Version:        %{majorv}.%{minorv}
Release:        39%{?dist}
Summary:        Tool for stitching photos to panorama in linear curved space
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

#Group:          Applications/Graphics
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://jpanoramamaker.wz.cz
Source0:        http://jpanoramamaker.wz.cz/fedora/%{name}-%{version}.src.tar.gz
Source1:        %{name}.appdata.xml
Patch1:         bumpJdkVersion.patch

BuildRequires:  jpackage-utils
BuildRequires:  java-25-devel
BuildRequires:  ant-openjdk25 
BuildRequires:  swing-layout
BuildRequires:  desktop-file-utils

Requires:       jpackage-utils
Requires:       java-25
Requires:       swing-layout

%description
Tool for stitching photos to panorama in linear curved space

%package javadoc
Summary:        Javadocs for %{name}
Requires:       %{name} = %{version}-%{release}
Requires:       jpackage-utils

%description javadoc
This package contains the API documentation for %{name}.
This tool is unique in number of manual touches you can do to affect final result.
Sometimes simple changing of order of image or lying a bit on position where they meet can do miracles.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{majorv}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
%patch -P1 -p1

#add swing-layout to classpath
sed -i 's-javac.classpath=\\-javac.classpath=/usr/share/java/swing\-layout/swing\-layout.jar\:\\-g'  nbproject/project.properties
#remove copylibraries
sed -i 's/<taskdef/<!--<taskdef/g' nbproject/build-impl.xml
sed -i 's:</copylibs>:</copylibs>-->:g' nbproject/build-impl.xml

%build
ant

#pack manually
pushd  build/classes
jar -cvf ../../dist/%{name}.jar *
popd

%install
rm -rf $RPM_BUILD_ROOT

#desktop
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --dir=${RPM_BUILD_ROOT}%{_datadir}/applications  jpanoramamaker.desktop
cp -p ./jpanoramamaker.png  $RPM_BUILD_ROOT%{_datadir}/pixmaps/jpanoramamaker.png
#end desktop

#launcher
mkdir -p $RPM_BUILD_ROOT%{_bindir}/
cp -p ./jpanoramamaker $RPM_BUILD_ROOT%{_bindir}/jpanoramamaker
#end launcher

# we are in /BUILD/jpanoramamaker-5/
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p ./dist/%{name}.jar  $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -rp ./dist/javadoc/  $RPM_BUILD_ROOT%{_javadocdir}/%{name}
ln -s %{_javadocdir}/%{name} $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

#appdata
install -Dpm0644 %{SOURCE1} %{buildroot}%{_datadir}/appdata/%{name}.appdata.xml

#####################################

%files
%{_datadir}/pixmaps/jpanoramamaker.png
%{_datadir}/applications/jpanoramamaker.desktop
%attr(755,root,root) %{_bindir}/jpanoramamaker
%{_datadir}/appdata/%{name}.appdata.xml

%defattr(-,root,root,-)
%{_javadir}/*
%doc license.txt

%files javadoc
%{_javadocdir}/%{name}
%{_javadocdir}/%{name}-%{version}

%changelog
%autochangelog
