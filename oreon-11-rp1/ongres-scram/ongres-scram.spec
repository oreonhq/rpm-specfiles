%global source0_hash d0a623d2b313f9fa8290bbd2b19c2e4c803d05716aa35a623b281e0851c07176

%global upstream_version 3.2

Name:           ongres-scram
Version:        %(echo %{upstream_version} | sed 's/-/~/g')
Release:        %autorelease
Summary:        Salted Challenge Response Authentication Mechanism (SCRAM) - Java Implementation
License:        BSD-2-Clause
URL:            https://github.com/ongres/scram
Source0:        https://github.com/ongres/scram/archive/refs/tags/3.2/scram-3.2.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  jurand

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.ongres.stringprep:saslprep)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.1-3

%description
This is a Java implementation of SCRAM (Salted Challenge Response
Authentication Mechanism) which is part of the family of Simple
Authentication and Security Layer (SASL, RFC 4422) authentication
mechanisms. It is described as part of RFC 5802 and RFC7677.

%package client
Summary:        Client for %{name}

%description client
This package contains the client for %{name}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n "scram-%{upstream_version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :maven-invoker-plugin

%pom_remove_dep org.jetbrains:annotations scram-parent

%java_remove_annotations . -s -n NotNull -n Unmodifiable -n Nullable

%mvn_package com.ongres.scram:scram-aggregator __noinstall
%mvn_package com.ongres.scram:scram-parent __noinstall

%pom_xpath_inject 'pom:plugin[pom:artifactId = "maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' scram-parent

%build
%mvn_build -j -s

%install
%mvn_install

%files -f .mfiles-scram-common
%license LICENSE

%files client -f .mfiles-scram-client
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2-1
- Import
