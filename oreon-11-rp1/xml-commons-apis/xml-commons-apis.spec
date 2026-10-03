%global source0_hash d34bd88dc89c5c1ed2545ec5c61e4606fc28beb200a6fecf8c3ed17694181866

Name:           xml-commons-apis
Version:        1.4.01
Release:        %autorelease
Summary:        APIs for DOM, SAX, and JAXP
License:        Apache-2.0 AND W3C AND SAX-PD-2.0
URL:            https://xerces.apache.org/xml-commons/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# From source control because the published tarball doesn't include some docs:
#   svn export http://svn.apache.org/repos/asf/xml/commons/tags/xml-commons-external-1_4_01/java/external/
#   tar czf xml-commons-external-1.4.01-src.tar.gz external
Source0:        https://archive.apache.org/dist/xerces/xml-commons/source/xml-commons-external-%{version}-src.tar.gz
Source1:        %{name}-MANIFEST.MF
Source2:        %{name}-ext-MANIFEST.MF
Source3:        https://repo1.maven.org/maven2/xml-apis/xml-apis/2.0.2/xml-apis-2.0.2.pom
Source4:        https://repo1.maven.org/maven2/xml-apis/xml-apis-ext/1.3.04/xml-apis-ext-1.3.04.pom

BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
BuildRequires:  apache-parent
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.4.01-59
Provides:       xml-commons = %{version}-%{release}

%description
xml-commons-apis is designed to organize and have common packaging for
the various externally-defined standard interfaces for XML. This
includes the DOM, SAX, and JAXP.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -c -n %{name}-%{version}
# Make sure upstream hasn't sneaked in any jars we don't know about
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

# Fix file encodings
iconv -f iso8859-1 -t utf-8 LICENSE.dom-documentation.txt > \
  LICENSE.dom-doc.temp && mv -f LICENSE.dom-doc.temp LICENSE.dom-documentation.txt
iconv -f iso8859-1 -t utf-8 LICENSE.dom-software.txt > \
  LICENSE.dom-sof.temp && mv -f LICENSE.dom-sof.temp LICENSE.dom-software.txt

# remove bogus section from poms
cp %{SOURCE3} %{SOURCE4} .
sed -i '/distributionManagement/,/\/distributionManagement/ {d}' *.pom

%mvn_file :xml-apis xml-commons-apis jaxp13 jaxp xml-commons-jaxp-1.3-apis
%mvn_file :xml-apis-ext xml-commons-apis-ext
%mvn_alias :xml-apis-ext xerces:dom3-xml-apis

%build
mkdir -p build/classes build/ext-classes build/docs/javadoc
javac --release 8 -d build/classes $(find javax org/apache org/xml -name '*.java')
jar cf build/xml-apis.jar -C build/classes .
javac --release 8 -d build/ext-classes $(find org/w3c -name '*.java')
jar cf build/xml-apis-ext.jar -C build/ext-classes .

# inject OSGi manifests
jar ufm build/xml-apis.jar %{SOURCE1}
jar ufm build/xml-apis-ext.jar %{SOURCE2}

%mvn_artifact xml-apis-[0-9]*.pom build/xml-apis.jar
%mvn_artifact xml-apis-ext*.pom build/xml-apis-ext.jar

%install
%mvn_install

# prevent apis javadoc from being included in doc
rm -rf build/docs/javadoc

%files -f .mfiles
%doc LICENSE NOTICE
%doc LICENSE.dom-documentation.txt README.dom.txt
%doc LICENSE.dom-software.txt LICENSE.sac.html
%doc LICENSE.sax.txt README.sax.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.01-1
- Import
