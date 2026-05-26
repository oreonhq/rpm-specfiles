# oreon source sha256 begin
# URL sources: global sourceN_sha256 = 64-char hex from sha256sum. Omit a sourceN_sha256 line to skip verify for that source.
%global source0_sha256 94b05d8c19eed87fdb0cf4f2344e6f86ad674bb226e0462498b3e95de37bfa4a
%global oreon_verify_sources \
%{?source0_sha256:%(test -z "%{source0_sha256}" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_sha256}" || { echo "oreon: Source0 sha256 mismatch" >&2; exit 1; }; })}
%(true)
# oreon source sha256 end

Name:           xmlstreambuffer
Version:        2.1.0
Release:        11%{?dist}
Summary:        Stream Based Representation for XML Infoset
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://github.com/eclipse-ee4j/metro-xmlstreambuffer
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/eclipse-ee4j/metro-xmlstreambuffer/archive/2.1.0/metro-xmlstreambuffer-2.1.0.tar.gz

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
%oreon_verify_sources
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
