%global source0_hash 2fc18347d4d3f3aa08d3619e86fff9a789239a429a5106459f9226080338574c

%bcond_without activation
%bcond_without cglib
%bcond_without dom4j
%bcond_without jdom
%bcond_without jdom2
%bcond_with jettison
%bcond_with joda-time
%bcond_with kxml2
%bcond_with stax
%bcond_with woodstox
%bcond_with xom
%bcond_with xpp3

Name:           xstream
Version:        1.4.21
Release:        1%{?dist}
Summary:        Java XML serialization library
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://x-stream.github.io
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://repo1.maven.org/maven2/com/thoughtworks/%{name}/%{name}-distribution/%{version}/%{name}-distribution-%{version}-src.zip
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(io.github.x-stream:mxparser)
BuildRequires:  mvn(jakarta.xml.bind:jakarta.xml.bind-api:2)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%if %{with activation}
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api:1)
%endif
%if %{with cglib}
BuildRequires:  mvn(cglib:cglib-nodep)
%endif
%if %{with dom4j}
BuildRequires:  mvn(dom4j:dom4j)
%endif
%if %{with jdom}
BuildRequires:  mvn(org.jdom:jdom)
%endif
%if %{with jdom2}
BuildRequires:  mvn(org.jdom:jdom2)
%endif
%if %{with jettison}
BuildRequires:  mvn(org.codehaus.jettison:jettison)
%endif
%if %{with joda-time}
BuildRequires:  mvn(joda-time:joda-time)
%endif
%if %{with kxml2}
BuildRequires:  mvn(net.sf.kxml:kxml2-min)
%endif
%if %{with stax}
BuildRequires:  mvn(stax:stax)
BuildRequires:  mvn(stax:stax-api)
%endif
%if %{with woodstox}
BuildRequires:  mvn(org.codehaus.woodstox:wstx-asl)
%endif
%if %{with xom}
BuildRequires:  mvn(xom:xom)
%endif
%if %{with xpp3}
BuildRequires:  mvn(xpp3:xpp3_min)
%endif

%description
XStream is a simple library to serialize objects to XML
and back again. A high level facade is supplied that
simplifies common use cases. Custom objects can be serialized
without need for specifying mappings. Speed and low memory
footprint are a crucial part of the design, making it suitable
for large object graphs or systems with high message throughput.
No information is duplicated that can be obtained via reflection.
This results in XML that is easier to read for humans and more
compact than native Java serialization. XStream serializes internal
fields, including private and final. Supports non-public and inner
classes. Classes are not required to have default constructor.
Duplicate references encountered in the object-model will be
maintained. Supports circular references. By implementing an
interface, XStream can serialize directly to/from any tree
structure (not just XML). Strategies can be registered allowing
customization of how particular types are represented as XML.
When an exception occurs due to malformed XML, detailed diagnostics
are provided to help isolate and fix the problem.

%package -n %{name}-benchmark
Summary:        Benchmark module for %{name}
%description -n %{name}-benchmark
Benchmark module for %{name}.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# -n: base directory name
%autosetup -n %{name}-%{version}
# delete precompiled jar and class files
find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete
# change javax to jakarta
# https://jakarta.ee/about/faq#What_happened_with_javax.*_namespace?
%pom_change_dep -r javax.activation:activation jakarta.activation:jakarta.activation-api:1
%pom_change_dep -r javax.xml.bind:jaxb-api jakarta.xml.bind:jakarta.xml.bind-api:2
# remove dependency plugin
%pom_remove_plugin -r :maven-dependency-plugin
# optional dep: activation
%if %{without activation}
%pom_remove_dep -r jakarta.activation:jakarta.activation-api
rm xstream/src/java/com/thoughtworks/xstream/converters/extended/ActivationDataFlavorConverter.java
%endif
# optional dep: cglib
%if %{without cglib}
%pom_remove_dep -r cglib:cglib-nodep
rm xstream/src/java/com/thoughtworks/xstream/converters/reflection/CGLIBEnhancedConverter.java
rm xstream/src/java/com/thoughtworks/xstream/mapper/CGLIBMapper.java
rm xstream/src/java/com/thoughtworks/xstream/security/CGLIBProxyTypePermission.java
%endif
# optional dep: dom4j
%if %{without dom4j}
%pom_remove_dep -r dom4j:dom4j
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JWriter.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Dom4JXmlWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamDom4J.java
%endif
# optional dep: jdom
%if %{without jdom}
%pom_remove_dep -r org.jdom:jdom
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDomWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamJDom.java
%endif
# optional dep: jdom2
%if %{without jdom2}
%pom_remove_dep -r org.jdom:jdom2
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Driver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Reader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/JDom2Writer.java
%endif
# optional dep: jettison
%if %{without jettison}
%pom_remove_dep -r org.codehaus.jettison:jettison
rm xstream/src/java/com/thoughtworks/xstream/io/json/JettisonMappedXmlDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/json/JettisonStaxWriter.java
%endif
# optional dep: joda-time
%if %{without joda-time}
%pom_remove_dep -r joda-time:joda-time
rm xstream/src/java/com/thoughtworks/xstream/core/util/ISO8601JodaTimeConverter.java
%endif
# optional dep: kxml2
%if %{without kxml2}
%pom_remove_dep -r net.sf.kxml:kxml2-min
rm xstream/src/java/com/thoughtworks/xstream/io/xml/KXml2DomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/KXml2Driver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamKXml2.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamKXml2DOM.java
%endif
# optional dep: stax
%if %{without stax}
%pom_remove_dep -r stax:stax
%pom_remove_dep -r stax:stax-api
rm xstream/src/java/com/thoughtworks/xstream/io/xml/BEAStaxDriver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamBEAStax.java
%endif
# optional dep: woodstox
%if %{without woodstox}
%pom_remove_dep -r org.codehaus.woodstox:wstx-asl
%pom_remove_dep -r com.fasterxml.woodstox:woodstox-core
rm xstream/src/java/com/thoughtworks/xstream/io/xml/WstxDriver.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamWoodstox.java
%endif
# optional dep: xom
%if %{without xom}
%pom_remove_dep -r xom:xom
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomReader.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/XomWriter.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXom.java
%endif
# optional dep: xpp3
%if %{without xpp3}
%pom_remove_dep -r xpp3:xpp3_min
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xpp3DomDriver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/Xpp3Driver.java
rm xstream/src/java/com/thoughtworks/xstream/io/xml/xppdom/Xpp3DomBuilder.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXpp3.java
rm xstream-benchmark/src/java/com/thoughtworks/xstream/tools/benchmark/products/XStreamXpp3DOM.java
%endif
# disable module distribution
%pom_disable_module %{name}-distribution
# disable module hibernate
%pom_disable_module %{name}-hibernate
# disable module jmh
%pom_disable_module %{name}-jmh
# don't install parent package
%mvn_package :%{name}-parent __noinstall

%build
%mvn_build -s -f -- -Dversion.java.5=1.8 -Dversion.java.6=1.8 -Dversion.java.source=1.8 -Dversion.java.target=1.8

%install
%mvn_install

%files -n %{name} -f .mfiles-%{name}
%license LICENSE.txt
%doc README.txt
%files -n %{name}-benchmark -f .mfiles-%{name}-benchmark
%license LICENSE.txt
%doc README.txt

%changelog
%autochangelog
