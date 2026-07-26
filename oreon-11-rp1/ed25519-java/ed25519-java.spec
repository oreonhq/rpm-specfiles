%global source0_hash a89a2331afb1db0bd06ce029c731db2d24684cebf111e796b51deb6e2a20a310

Name:          ed25519-java
Version:       0.3.0
Release:       27%{?dist}
Summary:       Implementation of EdDSA (Ed25519) in Java
# Automatically converted from old format: CC0 - review is highly recommended.
License:       CC0-1.0
URL:           https://github.com/str4d/ed25519-java
Source0:       https://github.com/str4d/ed25519-java/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/str4d/ed25519-java/commit/e0ac35769db8553fb714b09f0d3f3d2b001fd033
Patch0: 0001-EdDSAEngine.initVerify-Handle-any-non-EdDSAPublicKey.patch

Patch1: 0002-Disable-test-that-relies-on-internal-sun-JDK-classes.patch

BuildRequires: maven-local-openjdk25
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.hamcrest:hamcrest-all)

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
This is an implementation of EdDSA in Java. Structurally, it
is based on the ref10 implementation in SUPERCOP (see
http://ed25519.cr.yp.to/software.html).

There are two internal implementations:

* A port of the radix-2^51 operations in ref10
  - fast and constant-time, but only useful for Ed25519.
* A generic version using BigIntegers for calculation
  - a bit slower and not constant-time, but compatible
    with any EdDSA parameter specification.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{version}
%patch -P0 -p1
%patch -P1 -p1

# Unwanted tasks
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
# Unavailable plugin
%pom_remove_plugin :nexus-staging-maven-plugin

%mvn_file net.i2p.crypto:eddsa %{name} eddsa

# Remove hard-coded source/target
%pom_xpath_remove pom:plugin/pom:configuration/pom:target
%pom_xpath_remove pom:plugin/pom:configuration/pom:source

%build
%mvn_build -- -Dmaven.compiler.release=11

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
