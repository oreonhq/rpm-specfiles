%bcond_with bootstrap

Name:           plexus-interpolation
Version:        1.27
Release:        %autorelease
Summary:        Plexus Interpolation API
# Most of the code is ASL 2.0, a few source files are ASL 1.1 and some tests are MIT
License:        Apache-2.0 AND Apache-1.1 AND MIT
URL:            https://github.com/codehaus-plexus/plexus-interpolation
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-interpolation/archive/plexus-interpolation-%{version}.tar.gz

Patch:          0001-Use-PATH-env-variable-instead-of-JAVA_HOME.patch
# oreon url source checksums begin
%global source0_sha256 7a5769edbad9a70758dfe68aa4970243088942b136b5f54835f7ccabbd53c5df
%global source0_file plexus-interpolation-1.27.tar.gz
# oreon url source checksums end

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
Obsoletes:      %{name}-javadoc < 1.27-13

%description
Plexus interpolator is the outgrowth of multiple iterations of development
focused on providing a more modular, flexible interpolation framework for
the expression language style commonly seen in Maven, Plexus, and other
related projects.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-interpolation-1.27.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7a5769edbad9a70758dfe68aa4970243088942b136b5f54835f7ccabbd53c5df" || { echo "oreon: Source0 SHA256 mismatch for plexus-interpolation-1.27.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C
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
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.27-1
- Import
