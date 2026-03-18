%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jboss-logging-tools
Version:          2.2.1
Release:          22%{?dist}
Summary:          JBoss Logging I18n Annotation Processor
# Not available license file https://issues.jboss.org/browse/LOGTOOL-107
# ./annotations/src/main/java/org/jboss/logging/annotations/*.java: Apache (v2.0)
License:          Apache-2.0 and LGPL-2.0-or-later
URL:              https://github.com/jboss-logging/jboss-logging-tools
Source0:          %{url}/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Source1:          http://www.apache.org/licenses/LICENSE-2.0.txt
Patch1:           0001-Add-getEnclosingMethod-to-DelegatingExecutableElemen.patch

BuildArch:        noarch
ExclusiveArch:    %{java_arches} noarch

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:    maven-local
%else
BuildRequires:    maven-local-openjdk25
%endif

BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)
BuildRequires:    mvn(org.jboss.jdeparser:jdeparser)
BuildRequires:    mvn(org.jboss.logging:jboss-logging)

%description
This pacakge contains JBoss Logging I18n Annotation Processor

%prep
%autosetup -n %{name}-%{namedversion} -p 1

cp %{SOURCE1} .

# roaster is not packaged for Fedora, so:
# - Remove the dependency
# - Remove the test that requires it
%pom_remove_dep -r org.jboss.forge.roaster:
rm processor/src/test/java/org/jboss/logging/processor/generated/GeneratedSourceAnalysisTest.java

# Skip docs module
%pom_disable_module docs

%build
%mvn_build -f -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt
%doc README.adoc

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-22
- Prepare for Oreon 11 (RP1)
