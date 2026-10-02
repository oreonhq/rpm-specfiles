%global source0_hash d244d9c4f14e00f362d851064c9b7a89b612a8f98caa1f3cc864d22d8698389b

%bcond_with bootstrap

Name:           plexus-interpolation
Version:        1.30.0
Release:        %autorelease
Summary:        Plexus Interpolation API
# Most of the code is ASL 2.0, a few source files are ASL 1.1 and some tests are MIT
License:        Apache-2.0 AND Apache-1.1 AND MIT
URL:            https://github.com/codehaus-plexus/plexus-interpolation
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-interpolation/archive/refs/tags/plexus-interpolation-%{version}.tar.gz#/plexus-interpolation-%{version}.tar.gz

Patch:          0001-Use-PATH-env-variable-instead-of-JAVA_HOME.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.30.0-13

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n plexus-interpolation-plexus-interpolation-%{version}
%pom_add_dep junit:junit:4.13.1:test
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-scm-publish-plugin

%build
%mvn_file : plexus/interpolation
%mvn_build -j

%install
%mvn_install

%files -f .mfiles

%changelog
%autochangelog
