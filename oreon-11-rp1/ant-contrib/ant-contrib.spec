%global source2_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash 5c180feaca2704d914054a1e6b453673cc9b65cfb3da307aff17439a9aa09d6b
%global beta_number b3
Summary:        Collection of tasks for Ant
Name:           ant-contrib
Version:        1.0b3
Release:        1%{?dist}
License:        Apache-2.0 AND Apache-1.1
URL:            http://ant-contrib.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/ant-contrib/ant-contrib/1.0b3/ant-contrib-1.0b3-src.tar.bz2
Source2:        https://www.apache.org/licenses/LICENSE-2.0.txt
Patch2:         ant-contrib-antservertest.patch
Patch3:         ant-contrib-java-8.patch
Requires:       java-25-headless
Requires:       junit
Requires:       ant-openjdk25 
Requires:       xerces-j2
BuildArch:      noarch
ExclusiveArch: %{java_arches} noarch
# oreon:deps
BuildRequires:  ant-junit
BuildRequires:  ant-openjdk25
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-parent
BuildRequires:  apache-ivy
BuildRequires:  bcel
BuildRequires:  ivy-local
BuildRequires:  java-25-devel
BuildRequires:  junit
BuildRequires:  xerces-j2
# /oreon:deps
%description
The Ant-Contrib project is a collection of tasks
(and at one point maybe types and other tools)
for Apache Ant.

%package        javadoc
Summary:        Javadoc for %{name}
%description    javadoc
Api documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q  -n %{name}
%autopatch -p1

cp -p %{SOURCE2} LICENSE-2.0.txt

find -name '*.class' -delete
find -name '*.jar' -delete

sed -i "s|xercesImpl|xerces-j2|g" ivy.xml
# needs porting to latest ivy
rm -fr src/java/net/sf/antcontrib/net/URLImportTask.java
# remove httpclient stuff
rm -fr src/java/net/sf/antcontrib/net/httpclient

sed -i '/<ivy:configure /d' build.xml
rm -f ivy-conf.xml

sed -i 's/antlib:fr.jayasoft.ivy.ant/antlib:org.apache.ivy.ant/g' build.xml
sed -i 's/org="jayasoft"/org="org.apache.ivy"/g' ivy.xml
sed -i '/<dependency org="apache"/{N;N;N;/commons-httpclient/d}' ivy.xml

sed -i '/<info /s//&revision="1.0b3" /' ivy.xml
%mvn_alias : ant-contrib:

%build

%ant -Divy.mode=local dist
%install
%mvn_artifact ivy.xml target/%{name}.jar
%mvn_install -J target/docs/api
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
echo "ant-contrib/ant-contrib" > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-contrib
%oreon_autofiles ant-contrib-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n ant-contrib-javadoc -f %{oreon_filedir}/ant-contrib-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.51.
- Prepare for Oreon 11 (RP1)
