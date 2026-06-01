%global source0_hash b1d9a603f4fa75f0702ef84af5bcc11d03e721b6317daec1b1f81c31904bed00

%bcond_with bootstrap

Name:           xz-java
Version:        1.9
Release:        %autorelease
Summary:        Java implementation of XZ data compression
License:        LicenseRef-Public-Domain
URL:            https://tukaani.org/xz/java.html
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://tukaani.org/xz/xz-java-%{version}.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.9-25

%description
A complete implementation of XZ data compression in Java.

It features full support for the .xz file format specification version 1.0.4,
single-threaded streamed compression and decompression, single-threaded
decompression with limited random access support, raw streams (no .xz headers)
for advanced users, including LZMA2 with preset dictionary.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n xz-java-1.9

%mvn_file : %{name} xz

%build
# During documentation generation the upstream build.xml tries to download
# package-list from oracle.com. Create a dummy package-list to prevent that.
mkdir -p extdoc && touch extdoc/package-list

%ant -Dsourcever=8 maven

%install
%mvn_artifact build/maven/xz-%{version}.pom build/jar/xz.jar

%mvn_install

%files -f .mfiles
%doc README THANKS
%license COPYING

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.9-1
- Import
