%global source0_hash fc39443f87bcf98b72f90ea9f8d9bd8a9cafe49ac767f20a2f2531823a3cb711

%global core   org.abego.treelayout
%global giturl https://github.com/abego/treelayout

Name:          treelayout
Version:       1.0.3
Release:       28%{?dist}
Summary:       Efficient and customizable Tree Layout Algorithm in Java
License:       BSD-3-Clause
URL:           http://treelayout.sourceforge.net/
VCS:           git:%{giturl}.git
Source0:       %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
# Dummy POM to ease building with RPM
Source1:       pom.xml

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: maven-local-openjdk25
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)

%description
Efficiently create compact, highly customizable tree layouts.  The software
builds tree layouts in linear time; i.e., even trees with many nodes are built
quickly.

%package       demo
Summary:       TreeLayout Core Demo

%description   demo
Demo for "org.abego.treelayout.core".

%package       javadoc
Summary:       Javadoc for %{name}

%description   javadoc
This package contains javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup
cp -p %{SOURCE1} .

%conf
# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent %{core} %{core}.demo %{core}.netbeans %{core}.netbeans.demo

# update the source and target JDK
sed -i 's/1\.5/1.8/g' $(find . -name pom.xml)

# fix non ASCII chars for JDK 8 and earlier
if [ -x %{_bindir}/native2ascii ]; then
  native2ascii -encoding UTF8 \
    %{core}/src/main/java/org/abego/treelayout/package-info.java \
    %{core}/src/main/java/org/abego/treelayout/package-info.java
fi

%mvn_package :%{core}.project __noinstall

%build
%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{core}.core
%doc %{core}/CHANGES.txt README.md
%license %{core}/src/LICENSE.TXT

%files demo -f .mfiles-%{core}.demo
%doc %{core}.demo/CHANGES.txt
%license %{core}.demo/src/LICENSE.TXT

%files javadoc -f .mfiles-javadoc
%license %{core}/src/LICENSE.TXT

%changelog
%autochangelog
