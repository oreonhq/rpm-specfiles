Name:           plexus-velocity
Version:        2.2.1
Release:        4%{?dist}
Summary:        Plexus Velocity Component
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://codehaus-plexus.github.io/plexus-velocity/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz
Source1:        http://www.apache.org/licenses/LICENSE-2.0.txt
# oreon url source checksums begin
%global source0_sha256 d0b5cff1ebafed63b7ffa4d5f3534eaa6c8415575a48b28a860d72a8f91f3576
%global source0_file plexus-velocity-2.2.1.tar.gz
# oreon url source checksums end

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.inject:guice)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.apache.velocity:velocity-engine-core)
BuildRequires:  mvn(org.codehaus.plexus:plexus-components:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

%description
This package provides Plexus Velocity component - a wrapper for
Apache Velocity template engine, which allows easy use of Velocity
by applications built on top of Plexus container.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/plexus-velocity-2.2.1.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "d0b5cff1ebafed63b7ffa4d5f3534eaa6c8415575a48b28a860d72a8f91f3576" || { echo "oreon: Source0 SHA256 mismatch for plexus-velocity-2.2.1.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n %{name}-%{name}-%{version}

find -name '*.jar' -delete

cp -p %{SOURCE1} LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.2.1-4
- Import
