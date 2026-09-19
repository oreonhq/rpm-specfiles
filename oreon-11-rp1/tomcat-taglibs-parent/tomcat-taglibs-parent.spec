%global source0_hash none

Name:           tomcat-taglibs-parent
Version:        3
Release:        30%{?dist}
Summary:        Apache Taglibs Parent

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://tomcat.apache.org/taglibs/
Source0:        https://github.com/apache/tomcat-taglibs-parent/raw/master/pom.xml
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache:apache:pom:)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
Apache Taglibs Parent pom used for building purposes.

%prep
%setup -q -c -T
cp -p %{SOURCE0} .

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_mavenpomdir}/%{name}

%changelog
%autochangelog
