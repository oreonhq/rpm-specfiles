Name:           ongres-stringprep
Version:        2.2
Release:        %autorelease
Summary:        RFC 3454 Preparation of Internationalized Strings in pure Java
License:        BSD-2-Clause
URL:            https://github.com/ongres/stringprep
Source0:        https://github.com/ongres/stringprep/archive/%{version}/stringprep-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 ff4791d5d9d3b96f942b38b901b3053f20a141b3e51747430dd38762929b1798
%global source0_file stringprep-2.2.tar.gz
# oreon url source checksums end
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.2-3

%description
The stringprep protocol does not stand on its own; it has to be used by other
protocols at precisely-defined places in those other protocols.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/stringprep-2.2.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "ff4791d5d9d3b96f942b38b901b3053f20a141b3e51747430dd38762929b1798" || { echo "oreon: Source0 SHA256 mismatch for stringprep-2.2.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -n "stringprep-%{version}"
find \( -name '*.jar' -o -name '*.class' \) -delete

%pom_remove_dep org.junit:junit-bom parent

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# codegenerator is only needed at build time, and has extra dependencies
%mvn_package com.ongres.stringprep:codegenerator __noinstall

# codegen is only needed for specific build profile that we do not use
rm -r codegen

%pom_xpath_inject 'pom:plugin[pom:artifactId="maven-jar-plugin"]/pom:configuration/pom:archive' '
<manifestEntries>
  <Multi-Release>true</Multi-Release>
</manifestEntries>
' parent

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2-1
- Prepare for Oreon 11 (RP1)
