%global source0_hash 31d182e5dc857666dba640caf9529158c679075f4f137deceff128e268d9195a

Name:           apache-commons-pool
Version:        1.6
Release:        44%{?dist}
Summary:        Apache Commons Pool Package
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://commons.apache.org/pool/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        http://www.apache.org/dist/commons/pool/source/commons-pool-%{version}-src.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

%description
The goal of Pool package is it to create and maintain an object (instance)
pooling package to be distributed under the ASF license. The package should
support a variety of pool implementations, but encourage support of an
interface that makes these implementations interchangeable.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n commons-pool-%{version}-src

# Compatibility links
%mvn_alias : org.apache.commons:commons-pool
%mvn_file : commons-pool %{name}

%build
%mvn_build -- -Dcommons.packageId=pool

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc README.txt RELEASE-NOTES.txt

%changelog
%autochangelog
