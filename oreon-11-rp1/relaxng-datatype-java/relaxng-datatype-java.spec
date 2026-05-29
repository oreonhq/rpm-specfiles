%global source0_hash bca3509ed30aacbb6bf6cbc5108d1f19fec40c0db7f01e22c38a3213ffc98167

Name:           relaxng-datatype-java
Version:        2011.1
Release:        %autorelease
Summary:        The relaxng datatype library for Java
# License file is not present in the source repository, the file was retrieved
# from SourceForge where the previous version is hosted
# https://sourceforge.net/projects/relaxng/files/datatype%20%28java%29/Ver.1.0/relaxngDatatype-1.0.zip/download
License:        BSD-3-Clause
URL:            https://relaxng.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/java-schema-utilities/relaxng-datatype-java/archive/refs/tags/relaxngDatatype-2011.1.tar.gz
Source1:        copying.txt

BuildRequires:  maven-local-openjdk25
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2011.1-14

%description
Interface between RELAX NG validators and datatype libraries.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1
cp %{SOURCE1} .

%pom_remove_parent

%pom_xpath_remove 'pom:build/pom:extensions'

%mvn_alias com.github.relaxng:relaxngDatatype relaxngDatatype:relaxngDatatype

%build
%mvn_build -j -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license copying.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2011.1-1
- Import
