# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 99b45a9f1b434529cc397116cf6f52ab7a29659f1dc05a0937c73e25596a67fd
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

%bcond bootstrap 0

Name:           plexus-cipher
Version:        2.0
Release:        %autorelease
Summary:        Plexus encryption/decryption component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-cipher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-cipher/archive/plexus-cipher-2.0/plexus-cipher-2.0.tar.gz

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0-28

BuildSystem:    maven
BuildOption:    usesJavapackagesBootstrap
BuildOption:    xmvnToolchain "openjdk25"
BuildOption:    mavenOption "-DjavaVersion=8"
BuildOption:    artifact ":plexus-cipher" {
BuildOption:        file "plexus/plexus-cipher"
BuildOption:        alias "org.sonatype.plexus:"
BuildOption:    }

%description
Plexus Cipher is a Java-based library from the Plexus project,
primarily used by Apache Maven to encrypt and decrypt sensitive data
in configuration files, such as passwords stored in settings.xml.
It enables developers to securely store encrypted credentials instead
of plain-text secrets when accessing Maven repositories or other
protected services.

%files -f .mfiles
%license LICENSE.txt NOTICE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0-1
- Import
