%global source0_hash 5153023b3974b6dcc75efbd2ba62d5083bf684c47edb40ed770862651532a420

%bcond_without bootstrap

Name:           apache-commons-jxpath
Version:        1.4.0
Release:        %autorelease
Summary:        Simple XPath interpreter
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-jxpath/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://www.apache.org/dist/commons/jxpath/source/commons-jxpath-1.4.0-src.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(jdom:jdom)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.3-77

%description
Defines a simple interpreter of an expression language called XPath.
JXPath applies XPath expressions to graphs of objects of all kinds:
JavaBeans, Maps, Servlet contexts, DOM etc, including mixtures thereof.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -n commons-jxpath-%{version}-src

%pom_remove_dep com.mockrunner:

# Remove dependency on glassfish
%pom_remove_dep :servlet-api
%pom_remove_dep :jsp-api
rm src/main/java/org/apache/commons/jxpath/servlet/*Context*.java
rm src/main/java/org/apache/commons/jxpath/servlet/*Handler.java
rm src/test/java/org/apache/commons/jxpath/servlet/JXPathServletContextTest.java

%mvn_file ":{*}" %{name} @1
%mvn_alias : org.apache.commons:

%pom_xpath_inject 'pom:properties' \
  '<commons.osgi.import>org.apache.commons.beanutils;resolution:="optional",org.jdom*;resolution:="optional",org.w3c.dom;resolution:="optional",javax.servlet*;resolution:="optional",*</commons.osgi.import>'

%build
# we are skipping tests because we don't have com.mockrunner in repos yet
%mvn_build -j -f -- -Dcommons.packageId=jxpath

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
* Wed Apr 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-2
- %%autosetup -n commons-jxpath-%%{version}-src for upstream source tarball layout

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.4.0-1
- Prepare for Oreon 11 (RP1)
