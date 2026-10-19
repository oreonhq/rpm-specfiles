%global source2_hash 1e53a10e6b65c64ae0f5a241c8ef289c7578f1109d8a78512dff7de2b29117b3
%global source1_hash 55cb8d469b68416e6bccf02db6b3191490752861ad3a1ded39dbcedc7ac863ba
%global source0_hash a4fbb1f99ed82903029a5a16ad0424b687dc7eb6db13947d1ae6387d8b1912ac
Name:           maven-reporting-api
Version:        4.0.0
Release:        1%{?dist}
Epoch:          1
Summary:        API to manage report generation
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-reporting-api
VCS:            git:https://github.com/apache/maven-reporting-api.git
Source0:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip
Source1:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip.asc
Source2:        https://downloads.apache.org/maven/KEYS
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
%{?javadoc_package}
# oreon:deps
BuildRequires:  gpgverify
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
# /oreon:deps
%description
API to manage report generation.  Maven-reporting-api is included in the Maven
2.x core distribution, but was moved to shared components to achieve report
decoupling from the Maven 3 core.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --data=%{SOURCE0} --signature=%{SOURCE1} --keyring=%{SOURCE2}
%autosetup

# Fix end of line encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.0-6
- Prepare for Oreon 11 (RP1)
