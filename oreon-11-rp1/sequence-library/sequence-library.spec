%global source0_hash 90a2dd8ac29b592ed41f4c2973ed776f0f950550b494880d66c3774f9e1fea7b

Name:           sequence-library
Version:        1.0.3
Release:        23%{?dist}
Summary:        Textual diff and merge library

License:        BSD-3-Clause
URL:            http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/

# Tarball generated with:
#  svn export http://svn.svnkit.com/repos/3rdparty/de.regnis.q.sequence/tags/1.0.3/ sequence-library-1.0.3 && \
#      tar caf sequence-library-1.0.3.tar.gz sequence-library-1.0.3/
Source0:        %{name}-%{version}.tar.gz
Source1:        http://repo1.maven.org/maven2/de/regnis/q/sequence/sequence-library/%{version}/sequence-library-%{version}.pom
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)

%description
A textual diff and merge library.

%package javadoc
Summary: Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

find -name '*.jar' -o -name '*.class' -delete

cp -pr %{SOURCE1} pom.xml

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
