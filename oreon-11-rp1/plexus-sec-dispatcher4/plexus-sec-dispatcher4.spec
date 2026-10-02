%global source0_hash 7c704c6268630b4a2e68f974653dacb1f1fc8bca621ac8a5af80b8a34bf4abf3

%bcond_with bootstrap

Name:           plexus-sec-dispatcher4
Version:        4.2.0
Release:        %autorelease
Summary:        Plexus Security Dispatcher Component
License:        Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-sec-dispatcher
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/sec-dispatcher-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.modello:modello-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.inject)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.slf4j:slf4j-api:2.0.17)
BuildRequires:  mvn(org.slf4j:slf4j-simple:2.0.17)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.0.3-3

%description
Plexus Security Dispatcher Component

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n plexus-sec-dispatcher-sec-dispatcher-%{version}
cp %{SOURCE1} .
%mvn_compat_version : 4.2.0 4.1.0

%build
# XXX Some tests may hang in some cases.
# Need to investigate which ones and why.
%mvn_build -f -j -- -Dversion.slf4j=2.0.17

%install
%mvn_install

%files -f .mfiles
%license LICENSE-2.0.txt

%changelog
%autochangelog
