%global source0_hash faa7aea9ee077388758971d541702fcc9df65b986a2406e8d93793c07b64e704

Name:           javaewah
Version:        1.1.13
Release:        16%{?dist}
Summary:        A word-aligned compressed variant of the Java bitset class

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/lemire/javaewah
Source0:        https://github.com/lemire/javaewah/archive/JavaEWAH-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)

%description
JavaEWAH is a word-aligned compressed variant of the Java bitset class.
It uses a 64-bit run-length encoding (RLE) compression scheme.

The goal of word-aligned compression is not to achieve the best
compression, but rather to improve query processing time. Hence, we try
to save CPU cycles, maybe at the expense of storage. However, the EWAH
scheme we implemented is always more efficient storage-wise than an
uncompressed bitmap (implemented in Java as the BitSet class). Unlike
some alternatives, javaewah does not rely on a patented scheme.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn javaewah-JavaEWAH-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Add missing test dep
%pom_add_dep org.apache.commons:commons-lang3:3.12.0:test

# Plugins that are unnecessary for RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG README.md
%license LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE-2.0.txt

%changelog
%autochangelog
