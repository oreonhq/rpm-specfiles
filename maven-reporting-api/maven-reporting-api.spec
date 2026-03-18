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
