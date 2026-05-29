%global source0_hash b69f0e7f9d07d652e2df2b534de78c569ab11b20cf502a63db73db209927fe15

%bcond_with bootstrap

Name:           jdom2
Version:        2.0.6.1
Release:        %autorelease
Summary:        Java manipulation of XML made easy
License:        Saxpath
URL:            http://www.jdom.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        %{name}-%{version}.tar.gz
# Bnd tool configuration
Source3:        bnd.properties
# Remove bundled jars that might not have clear licensing
Source4:        generate-tarball.sh

# Use system libraries
# Disable gpg signatures
# Process contrib and junit pom files
Patch:          0001-Adapt-build.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
BuildRequires:  ant-junit
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0.6.1-21

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it seeks to provide a robust,
light-weight means of reading and writing XML data without the
complex and memory-consumptive options that current API
offerings provide.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1


sed -i 's/\r//' LICENSE.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

# XPath functionality is not needed
rm -rf core/src/java/org/jdom2/xpath/
sed -i '/import org.jdom2.xpath.XPathFactory/d' core/src/java/org/jdom2/JDOMConstants.java

%build
mkdir lib
%ant -Dversion=%{version} -Dcompile.source=1.8 -Dcompile.target=1.8 maven

# Make jar into an OSGi bundle
# XXX disabled until BND is fixed
#bnd wrap --output build/package/jdom-%%{version}.bar --properties %%{SOURCE3} \
#         --version %%{version} build/package/jdom-%%{version}.jar
#mv build/package/jdom-%%{version}.bar build/package/jdom-%%{version}.jar

%install
%mvn_artifact build/maven/core/%{name}-%{version}.pom build/package/jdom-%{version}.jar
%mvn_install

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.md TODO.txt
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.6.1-1
- Import
