Name:           apache-commons-collections4
Summary:        Extension of the Java Collections Framework
Version:        4.4
Release:        21%{?dist}
License:        Apache-2.0

URL:            http://commons.apache.org/proper/commons-collections/
Source0:        http://archive.apache.org/dist/commons/collections/source/commons-collections4-%{version}-src.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.easymock:easymock)

%description
Commons-Collections seek to build upon the JDK classes by providing
new interfaces, implementations and utilities.


%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.


%prep
%setup -q -n commons-collections4-%{version}-src
%mvn_file : commons-collections4 %{name}


%build
%mvn_build -- -Dcommons.osgi.symbolicName=org.apache.commons.collections4


%install
%mvn_install


%files -f .mfiles
%doc RELEASE-NOTES.txt
%license LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.4-21
- Prepare for Oreon 11 (RP1)
