%global source0_hash ff2edcea3873a8e1bbe15a5494013c01b602b83a32272cc05c4e1e9ac82b0a17

%bcond_without dom4j

Name:           jaxen
Summary:        An XPath engine written in Java
Epoch:          0
Version:        1.2.0
Release:        23%{?dist}
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

URL:            https://github.com/jaxen-xpath/jaxen
Source0:        https://github.com/jaxen-xpath/jaxen/archive/v1.2.0/jaxen-1.2.0.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xml-apis:xml-apis)
%if %{with dom4j}
BuildRequires:  mvn(dom4j:dom4j)
%endif

%description
Jaxen is an open source XPath library written in Java. It is adaptable
to many different object models, including DOM, XOM, dom4j, and JDOM.
Is it also possible to write adapters that treat non-XML trees such as compiled
Java byte code or Java beans as XML, thus enabling you to query these trees
with XPath too.


%package        demo
Summary:        Samples for %{name}
Requires:       %{name} = 0:%{version}-%{release}

%description    demo
%{summary}.


%package        javadoc
Summary:        Javadoc for %{name}

%description    javadoc
%{summary}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q

# remove unnecessary maven plugins
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%if %{without dom4j}
rm -rf src/java/main/org/jaxen/dom4j
%pom_remove_dep dom4j:dom4j
%endif

rm -rf src/java/main/org/jaxen/xom
%pom_remove_dep xom:xom

%mvn_file : %{name}


%build
%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8


%install
%mvn_install

# demo
install -d -m 755 %{buildroot}%{_datadir}/%{name}/samples
cp -pr src/java/samples/* %{buildroot}%{_datadir}/%{name}/samples


%files -f .mfiles
%doc LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%files demo
%{_datadir}/%{name}


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.2.0-23
- Prepare for Oreon 11 (RP1)
