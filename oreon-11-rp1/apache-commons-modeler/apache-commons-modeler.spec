%global source0_hash e10a7ac6b6827cba25f40fed43380051023097244fe34b012227aabd5d01e8f0

%global base_name       modeler
%global short_name      commons-%{base_name}

Name:             apache-%{short_name}
Version:          2.0.1
Release:          50%{?dist}
Summary:          Model MBeans utility classes
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:          Apache-2.0
URL:              http://commons.apache.org/%{base_name}/
BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

Source0:          http://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz
# POM file based on the one from an unreleased upstream snapstream
Source1:          pom.xml

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-digester:commons-digester)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(xml-apis:xml-apis)

%description
Commons Modeler makes the process of setting up JMX (Java Management
Extensions) MBeans easier by configuring the required meta data using an XML
descriptor. In addition, Modeler provides a factory mechanism to create the
actual Model MBean instances.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{short_name}-%{version}-src
sed -i 's/\r//' LICENSE.txt
sed -i 's/\r//' RELEASE-NOTES.txt
sed -i 's/\r//' NOTICE.txt

# Copy pom file into place
cp -p %{SOURCE1} .

# Full commons-logging is a transitive dependency (through commons-digester)
%pom_remove_dep :commons-logging-api

# xml-apis is part of JDK
%pom_remove_dep :xml-apis

# Remove redundant dep on mx4j
%pom_remove_dep mx4j:mx4j-jmx

# Fix ant dependency
%pom_remove_dep ant:ant
%pom_add_dep org.apache.ant:ant:1.10

%mvn_alias : org.apache.commons:%{short_name}
%mvn_file : %{name} %{short_name}

%build
%mvn_build -- -Dcommons.packageId=modeler

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
%autochangelog
