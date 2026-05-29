%global source0_hash 063bf66e163f43b7d7897ac14efe1e80ed094d4016afe1181fe2285e3797bed3

Name:           jsch
Version:        0.1.55
Release:        %autorelease
Summary:        Pure Java implementation of SSH2
License:        BSD-3-Clause
URL:            http://www.jcraft.com/jsch/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://download.sourceforge.net/sourceforge/jsch/jsch-0.1.55.zip
# stripped manifest based on 
# https://download.eclipse.org/tools/orbit/downloads/drops2/R20201130205003/repository/plugins/com.jcraft.jsch_0.1.55.v20190404-1902.jar
Source1:        MANIFEST.MF
Source2:        plugin.properties

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.jcraft:jzlib)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  zip
Requires:       jzlib >= 0:1.0.5
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 0.1.55-29

%description
JSch allows you to connect to an sshd server and use port forwarding, 
X11 forwarding, file transfer, etc., and you can integrate its 
functionality into your own Java programs.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
%mvn_file : jsch

%pom_remove_parent

%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-compiler-plugin

%pom_xpath_remove pom:project/pom:build/pom:extensions
%pom_xpath_set pom:project/pom:version %{version}

%build
%mvn_build -j -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

# inject the OSGi Manifest
mkdir META-INF
cp %{SOURCE1} META-INF
cp %{SOURCE2} plugin.properties
touch META-INF/MANIFEST.MF
touch plugin.properties
zip target/%{name}-%{version}.jar META-INF/MANIFEST.MF
zip target/%{name}-%{version}.jar plugin.properties

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.1.55-1
- Import
