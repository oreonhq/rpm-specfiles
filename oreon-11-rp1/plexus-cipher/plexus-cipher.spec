%global source0_hash none

%bcond bootstrap 0

Name:           plexus-cipher
Version:        2.0
Release:        %autorelease
Summary:        Plexus encryption/decryption component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-cipher/archive/plexus-cipher-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
%endif

Obsoletes:      %{name}-javadoc < 2.0-28

%description
Plexus Cipher is a Java-based library from the Plexus project,
primarily used by Apache Maven to encrypt and decrypt sensitive data
in configuration files, such as passwords stored in settings.xml.
It enables developers to securely store encrypted credentials instead
of plain-text secrets when accessing Maven repositories or other
protected services.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n plexus-cipher-plexus-cipher-%{version}

%mvn_file : plexus/cipher
%mvn_alias : org.sonatype.plexus:plexus-cipher

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0-1
- Import
