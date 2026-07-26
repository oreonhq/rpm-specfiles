%global source0_hash d7da3332e105f835d3899f516859e0cdc4be7403883f3a5fb7c56f09d6e009e4

Summary:        Web Services Description Language Toolkit for Java
Name:           wsdl4j
Epoch:          0
Version:        1.6.3
Release:        36%{?dist}
# Automatically converted from old format: CPL - review is highly recommended.
License:        CPL-1.0
URL:            http://sourceforge.net/projects/wsdl4j
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://downloads.sourceforge.net/project/wsdl4j/WSDL4J/%{version}/wsdl4j-src-%{version}.zip
Source1:        %{name}-MANIFEST.MF
Source2:        http://repo1.maven.org/maven2/wsdl4j/wsdl4j/%{version}/wsdl4j-%{version}.pom

BuildRequires:  ant-openjdk25 
BuildRequires:  ant-junit
BuildRequires:  javapackages-local-openjdk25

Provides:       javax.wsdl

%description
The Web Services Description Language for Java Toolkit (WSDL4J) allows the
creation, representation, and manipulation of WSDL documents describing
services.  This code base will eventually serve as a reference implementation
of the standard created by JSR110.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-1_6_3

# Set source/target to 1.8 for building with Java 17
sed -i 's/<javac/<javac source="1.8" target="1.8"/' build.xml
sed -i 's/<javadoc/<javadoc source="1.8"/' build.xml

%mvn_file ":{*}" @1

%build
ant compile javadocs
# inject OSGi manifests
jar ufm build/lib/%{name}.jar %{SOURCE1}

%install
%mvn_artifact %{SOURCE2} build/lib/%{name}.jar
%mvn_artifact %{name}:qname:%{version} build/lib/qname.jar
%mvn_install -J build/javadocs

install -d -m 755 %{buildroot}%{_javadir}/javax.wsdl/
ln -sf ../%{name}.jar %{buildroot}%{_javadir}/javax.wsdl/
ln -sf ../qname.jar %{buildroot}%{_javadir}/javax.wsdl/

%files -f .mfiles
%license license.html
%{_javadir}/javax.wsdl/

%files javadoc -f .mfiles-javadoc
%license license.html

%changelog
%autochangelog
