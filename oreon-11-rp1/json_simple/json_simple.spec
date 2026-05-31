%global source0_hash a380f6605c0d7c9c97451f57f206e641b3a437322f9008b1c04beaa8d1b6421b

Name:           json_simple
Version:        1.1.1
Release:        40%{?dist}
Summary:        Simple Java toolkit for JSON
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://code.google.com/p/json-simple/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# svn export http://json-simple.googlecode.com/svn/tags/tag_release_1_1_1/ json-simple-1.1.1
# tar czf json-simple-1.1.1-src-svn.tar.gz json-simple-1.1.1
Source0:        json-simple-1.1.1-src-svn.tar.gz

#https://code.google.com/p/json-simple/issues/detail?id=97
Patch0:         json-simple-hash-java-1.8.patch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
JSON.simple is a simple Java toolkit for JSON. You can use JSON.simple 
to encode or decode JSON text. 
  * Full compliance with JSON specification (RFC4627) and reliable 
  * Provides multiple functionalities such as encode, decode/parse 
    and escape JSON text while keeping the library lightweight 
  * Flexible, simple and easy to use by reusing Map and List interfaces 
  * Supports streaming output of JSON text 
  * Stoppable SAX-like interface for streaming input of JSON text 
  * Heap based parser 
  * High performance (see performance testing) 
  * No dependency on external libraries 
  * Both of the source code and the binary are JDK1.2 compatible 

%package javadoc
Summary:       API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n json-simple-%{version}
find . -name '*.jar' -exec rm -f '{}' \;
# All the files have dos line endings, remove them.
find . -type f -exec %{__sed} -i 's/\r//' {} \;

%patch -P0 -p1

# Remove hard-coded compiler settings
%pom_remove_plugin :maven-compiler-plugin

%mvn_file : %{name}

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc AUTHORS.txt ChangeLog.txt README.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.1-40
- Import
