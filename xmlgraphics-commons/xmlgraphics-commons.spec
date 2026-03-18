Name:           xmlgraphics-commons
Version:        2.11
Release:        6%{?dist}
Epoch:          0
Summary:        XML Graphics Commons

License:        Apache-2.0 
URL:            http://xmlgraphics.apache.org/
Source0:        http://archive.apache.org/dist/xmlgraphics/commons/source/xmlgraphics-commons-%{version}-src.tar.gz
Patch1:         jdk25.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(xml-resolver:xml-resolver)

%description
Apache XML Graphics Commons is a library that consists of
several reusable components used by Apache Batik and
Apache FOP. Many of these components can easily be used
separately outside the domains of SVG and XSL-FO. You will
find components such as a PDF library, an RTF library,
Graphics2D implementations that let you generate PDF &
PostScript files, and much more.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q %{name}-%{version}
patch -p1 < %{PATCH1}
find -name "*.jar" -delete

# Disable plugins not needed for RPM build
%pom_remove_plugin :maven-checkstyle-plugin

# Make into OSGi bundle
%pom_xpath_inject pom:project '<packaging>bundle</packaging>'
%pom_add_plugin org.apache.felix:maven-bundle-plugin . \
" <extensions>true</extensions>
  <configuration>
    <instructions>
      <Bundle-SymbolicName>org.apache.xmlgraphics</Bundle-SymbolicName>
    </instructions>
  </configuration>"

%build
%mvn_file : %{name}
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE
%doc README

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.11-6
- Prepare for Oreon 11 (RP1)
