%global source0_hash 88cd112bd9132b613c18d5898f133e380f22ce4cb35d1ec5ddeb5088846b7be8

%global url     https://github.com/tdunning/%{name}

Name:           t-digest
Version:        3.2
Release:        14%{?dist}
Summary:        A new data structure for on-line accumulation of statistics
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            %{url}
Source0:        %{url}/archive/%{name}-%{version}.tar.gz
#grep -ir -e "<p/>"
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/TreeDigest.java
#sed "s;<p/>;<br>;g"  -i src/main/java/com/tdunning/math/stats/ArrayDigest.java
Patch0:         jdk8-javadoc.patch
Patch1:         sourceTarget.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25

Requires:       java-25

%description
A new data structure for accurate on-line accumulation of rank-based statistics
eg. quantiles and trimmed means. The t-digest algorithm is also very parallel
friendly making it useful in map-reduce and parallel streaming applications.

%package        javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}
#%%patch0
%patch -P1
# Useless tasks, pom_remove_plugin is in maven-local pkg
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin com.carrotsearch.randomizedtesting

%build
#skipping tests, they requires currently unpacked depndences
%mvn_build --force

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICES

%files javadoc  -f .mfiles-javadoc
%license LICENSE NOTICES

%changelog
%autochangelog
