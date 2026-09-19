%global source0_hash 2a87a553256f9b5514a174bcbb2dbd16ed53f9994c9437c232b35b229a2dc5ad

%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             hibernate-jpa-2.0-api
Version:          1.0.1
Release:          45%{?dist}
Summary:          Java Persistence 2.0 (JSR 317) API
License:          EPL-1.0 OR BSD-3-Clause
URL:              http://www.hibernate.org/
# svn export http://anonsvn.jboss.org/repos/hibernate/jpa-api/tags/hibernate-jpa-2.0-api-1.0.1.Final/ hibernate-jpa-2.0-api-1.0.1.Final
# tar -zcvf hibernate-jpa-2.0-api-1.0.1.Final.tar.gz hibernate-jpa-2.0-api-1.0.1.Final
Source0:          %{name}-%{namedversion}.tar.gz
Patch0:           %{name}-%{namedversion}-encoding.patch
Patch1:           %{name}-%{namedversion}-osgi-manifest.patch

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:    maven-local-openjdk25

%description
Hibernate definition of the Java Persistence 2.0 (JSR 317) API.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{namedversion}
%patch -P0 -p1
%patch -P1 -p1

%pom_xpath_remove pom:build/pom:extensions

%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin

# remove maven-compiler-plugin configuration that is broken with Java 11
%pom_xpath_remove 'pom:plugin[pom:artifactId="maven-compiler-plugin"]/pom:configuration'

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc readme.txt
%license license.txt

%files javadoc -f .mfiles-javadoc
%license license.txt

%changelog
%autochangelog
