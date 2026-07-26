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

BuildRequires:  java-25-devel >= 1.4
BuildRequires:  jpackage-utils >= 0:1.5.32
BuildRequires:  ant-openjdk25  >= 0:1.6

Requires:       java-25-headless >= 1.4
Requires:       jpackage-utils >= 0:1.5.32

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
# --- documentation ---
dstDocDir=$RPM_BUILD_ROOT%{_pkgdocdir}
install -d $dstDocDir
install --mode=644 ChangeLog COPYING README NEWS $dstDocDir
# --- samples (also into _docdir) ---
cp -pr  smpl/org $dstDocDir
# --- config files ---
confDir=$RPM_BUILD_ROOT%{_sysconfdir}/java
install -d $confDir
install --mode=664 sblim-cim-client2.properties sblim-slp-client2.properties $confDir
# --- jar ---
install -d $RPM_BUILD_ROOT%{_javadir}
install %{archive_folder}/lib/%{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar
# --- javadoc ---
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}
cp -pr %{archive_folder}/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}

%files
%dir %{_pkgdocdir}
%config(noreplace) %{_sysconfdir}/java/sblim-cim-client2.properties
%config(noreplace) %{_sysconfdir}/java/sblim-slp-client2.properties
%doc %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/README
%doc %{_pkgdocdir}/ChangeLog
%doc %{_pkgdocdir}/NEWS
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}

%files manual
%doc %{_pkgdocdir}/COPYING
%doc %{_pkgdocdir}/org

%changelog
%autochangelog
