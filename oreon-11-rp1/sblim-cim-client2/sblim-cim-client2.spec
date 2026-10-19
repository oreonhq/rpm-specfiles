%global source0_hash 9aadcb0e2001577c2be26c3cac9c3f4fd909af72eece788c5e110b6fae00c12b
%global project_folder %{name}-%{version}-src
%global archive_folder build
Name:           sblim-cim-client2
Version:        2.2.5
Release:        34%{?dist}
Summary:        Java CIM Client library
License:        EPL-1.0
URL:            http://sourceforge.net/projects/sblim/
Source0:        http://downloads.sourceforge.net/project/sblim/%{name}/%{version}/%{name}-%{version}-src.zip
Patch0:         sblim-cim-client2-2.2.5-fix-for-java-11-openjdk.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25-headless >= 1.4
Requires:       jpackage-utils >= 0:1.5.32
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
# /oreon:deps
%description
The purpose of this package is to provide a CIM Client Class Library for Java
applications. It complies to the DMTF standard CIM Operations over HTTP and
intends to be compatible with JCP JSR48 once it becomes available. To learn
more about DMTF visit http://www.dmtf.org.
More infos about the Java Community Process and JSR48 can be found at
http://www.jcp.org and http://www.jcp.org/en/jsr/detail?id=48.

%package javadoc
Summary:        Javadoc for %{name}
Requires:       sblim-cim-client2 = %{version}-%{release}
Requires:       jpackage-utils
%description javadoc
Javadoc for %{name}.

%package manual
Summary:        Manual and sample code for %{name}
Requires:       sblim-cim-client2 = %{version}-%{release}
%description manual
Manual and sample code for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{project_folder}
%autopatch -p1

dos2unixConversion() {
        fileName=$1
        %{__sed} -i 's/\r//g' "$fileName"
}

dosFiles2unix() {
        fileList=$1
        for fileName in $fileList; do
                dos2unixConversion $fileName
        done
}

dosFiles2unix 'ChangeLog NEWS README COPYING sblim-cim-client2.properties sblim-slp-client2.properties'
dosFiles2unix 'smpl/org/sblim/slp/example/*'
dosFiles2unix 'smpl/org/sblim/cimclient/samples/*'

%build

export ANT_OPTS="-Xmx256m"
ant \
        -Dbuild.compiler=modern \
        -DManifest.version=%{version}\
        package java-doc
%install
dstDocDir=$RPM_BUILD_ROOT%{_pkgdocdir}
install -d $dstDocDir
install --mode=644 ChangeLog COPYING README NEWS $dstDocDir
cp -pr  smpl/org $dstDocDir
confDir=$RPM_BUILD_ROOT%{_sysconfdir}/java
install -d $confDir
install --mode=664 sblim-cim-client2.properties sblim-slp-client2.properties $confDir
install -d $RPM_BUILD_ROOT%{_javadir}
install %{archive_folder}/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{archive_folder}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sblim-cim-client2-javadoc -f %{oreon_filedir}/sblim-cim-client2-javadoc.list
%files -n sblim-cim-client2-manual -f %{oreon_filedir}/sblim-cim-client2-manual.list

%changelog

%autochangelog
