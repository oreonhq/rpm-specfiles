# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 5c180feaca2704d914054a1e6b453673cc9b65cfb3da307aff17439a9aa09d6b
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%global beta_number b3

Summary:        Collection of tasks for Ant
Name:           ant-contrib
Version:        1.0
Release:        0.51.%{beta_number}%{?dist}
# Project site on sf lists both Apache Software License, Apache License V2.0
# see: https://sourceforge.net/projects/ant-contrib/
License:        Apache-2.0 AND Apache-1.1

URL:            http://ant-contrib.sourceforge.net/
Source0:        https://downloads.sourceforge.net/project/ant-contrib/ant-contrib/1.0b3/ant-contrib-1.0b3-src.tar.bz2
# ASL 2.0 Licence text
# Upstream bug at https://sourceforge.net/tracker/?func=detail&aid=3590371&group_id=36177&atid=416920
Source2:        http://www.apache.org/licenses/LICENSE-2.0.txt

Patch2:         ant-contrib-antservertest.patch
Patch3:         ant-contrib-java-8.patch

BuildRequires:  ivy-local, ant-openjdk25 , ant-openjdk25 
BuildRequires:  junit
BuildRequires:  ant-junit
BuildRequires:  xerces-j2
BuildRequires:  bcel
BuildRequires:  java-25-devel
BuildRequires:  apache-ivy
BuildRequires:  apache-commons-logging
BuildRequires:  apache-commons-parent

Requires:       java-25-headless
Requires:       junit
Requires:       ant-openjdk25 
Requires:       xerces-j2

BuildArch:      noarch
ExclusiveArch: %{java_arches} noarch

%description
The Ant-Contrib project is a collection of tasks
(and at one point maybe types and other tools)
for Apache Ant.

%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
Api documentation for %{name}.

%prep
%oreon_verify_sources
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

%files -f .mfiles
%{_sysconfdir}/ant.d/ant-contrib
%license target/docs/LICENSE.txt LICENSE-2.0.txt
%doc target/docs/manual/tasks/*

%files javadoc -f .mfiles-javadoc
%license target/docs/LICENSE.txt LICENSE-2.0.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.51.
- Prepare for Oreon 11 (RP1)
