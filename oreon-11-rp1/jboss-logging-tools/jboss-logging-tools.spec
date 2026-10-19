%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash f3275efdea6f52f2d8b8544e156de05809231cea57416dd206f8823da98dc40b
%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}
Name:             jboss-logging-tools
Version:          2.2.1
Release:        1%{?dist}
Summary:        JBoss Logging I18n Annotation Processor
License:          Apache-2.0 and LGPL-2.0-or-later
URL:              https://github.com/jboss-logging/jboss-logging-tools
Source0:        https://github.com/jboss-logging/jboss-logging-tools/archive/refs/tags/2.2.1.Final.tar.gz#/jboss-logging-tools-2.2.1.Final.tar.gz
Source1:          https://www.apache.org/licenses/LICENSE-2.0.txt
Patch1:           0001-Add-getEnclosingMethod-to-DelegatingExecutableElemen.patch
BuildArch:        noarch
ExclusiveArch:    %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.jboss.jdeparser:jdeparser)
BuildRequires:  mvn(org.jboss.logging:jboss-logging)
BuildRequires:  mvn(org.jboss:jboss-parent:pom:)
# /oreon:deps
%description
This pacakge contains JBoss Logging I18n Annotation Processor

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-22
- Prepare for Oreon 11 (RP1)
