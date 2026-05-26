Name:           maven-reporting-api
Version:        4.0.0
Release:        6%{?dist}
Epoch:          1
Summary:        API to manage report generation
License:        Apache-2.0
URL:            https://maven.apache.org/shared/maven-reporting-api
VCS:            git:https://github.com/apache/maven-reporting-api.git

Source0:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip
# Source file signature
Source1:        https://archive.apache.org/dist/maven/reporting/%{name}-%{version}-source-release.zip.asc
# Apache Maven public key
Source2:        https://downloads.apache.org/maven/KEYS
# oreon url source checksums begin
%global source0_sha256 a4fbb1f99ed82903029a5a16ad0424b687dc7eb6db13947d1ae6387d8b1912ac
%global source0_file maven-reporting-api-4.0.0-source-release.zip
# oreon url source checksums end

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  gpgverify
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-components:pom:)
BuildRequires:  mvn(org.apache.maven.doxia:doxia-sink-api)

%{?javadoc_package}

%description
API to manage report generation.  Maven-reporting-api is included in the Maven
2.x core distribution, but was moved to shared components to achieve report
decoupling from the Maven 3 core.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/maven-reporting-api-4.0.0-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a4fbb1f99ed82903029a5a16ad0424b687dc7eb6db13947d1ae6387d8b1912ac" || { echo "oreon: Source0 SHA256 mismatch for maven-reporting-api-4.0.0-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
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

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.0-6
- Prepare for Oreon 11 (RP1)
