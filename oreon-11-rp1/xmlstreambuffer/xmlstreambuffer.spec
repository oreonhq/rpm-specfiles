Name:           xmlstreambuffer
Version:        2.1.0
Release:        11%{?dist}
Summary:        Stream Based Representation for XML Infoset
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/eclipse-ee4j/metro-xmlstreambuffer
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/metro-xmlstreambuffer-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jakarta.activation:jakarta.activation-api)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.jvnet.staxex:stax-ex)
BuildRequires:  mvn(junit:junit)

%description
Stream based representation for XML infoset.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n metro-xmlstreambuffer-%{version}

pushd streambuffer

%pom_remove_parent

%pom_remove_plugin :buildnumber-maven-plugin
%pom_remove_plugin :glassfish-copyright-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep :woodstox-core
popd

%build
pushd streambuffer
%mvn_build
popd

%install
pushd streambuffer
%mvn_install
popd

%files -f streambuffer/.mfiles
%license LICENSE.md NOTICE.md
%doc CONTRIBUTING.md README.md

%files javadoc -f streambuffer/.mfiles-javadoc
%license LICENSE.md NOTICE.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.0-11
- Prepare for Oreon 11 (RP1)
