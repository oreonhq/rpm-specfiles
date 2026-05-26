%bcond_without bootstrap

Name:           plexus-resources
Version:        1.3.0
Release:        %autorelease
Summary:        Plexus Resource Manager
License:        Apache-2.0 AND MIT
URL:            https://github.com/codehaus-plexus/plexus-resources
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-resources/archive/plexus-resources-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 b43ee470cd18db6c8dc3acd3cb1e88e6a3e69e1110be44cb7f271e37e6716897
%global source0_file plexus-resources-1.3.0.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus-xml)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.3.0-13

%description
The Plexus project seeks to create end-to-end developer tools for
writing applications. At the core is the container, which can be
embedded or for a full scale application server. There are many
reusable components for hibernate, form processing, jndi, i18n,
velocity, etc. Plexus also includes an application server which
is like a J2EE application server, without all the baggage.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-resources-1.3.0.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "b43ee470cd18db6c8dc3acd3cb1e88e6a3e69e1110be44cb7f271e37e6716897" || { echo "oreon: Source0 SHA256 mismatch for plexus-resources-1.3.0.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1

%build
%mvn_file  : plexus/resources
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3.0-1
- Prepare for Oreon 11 (RP1)
