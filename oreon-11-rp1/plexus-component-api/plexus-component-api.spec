%global source0_hash c5592d14a955856aba22a0cf3ca9392bc8c2e89358b6b5ad28507dca978388e4

%define project_version 1.0-alpha-15

Name:           plexus-component-api
Version:        1.0
Release:        0.38.alpha15%{?dist}
Summary:        Plexus Component API

# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/
#svn export http://svn.codehaus.org/plexus/plexus-containers/tags/plexus-containers-1.0-alpha-15/plexus-component-api/ plexus-component-api-1.0-alpha-15
#tar zcf plexus-component-api-1.0-alpha-15.tar.gz plexus-component-api-1.0-alpha-15/
Source0:        https://github.com/sonatype/plexus-containers/archive/plexus-containers-1.0-alpha-15.tar.gz#/plexus-component-api-1.0-alpha-15.tar.gz

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds

%description
Plexus Component API

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n plexus-containers-plexus-containers-1.0-alpha-15/%{name}-%{project_version}
%pom_remove_parent 2>/dev/null || :

%build
%mvn_build -j -- -Dmaven.compiler.release=8

%install
%mvn_install

%pre javadoc
# workaround for rpm bug, can be removed in F-20
[ $1 -gt 1 ] && [ -L %{_javadocdir}/%{name} ] && \
rm -rf $(readlink -f %{_javadocdir}/%{name}) %{_javadocdir}/%{name} || :

%files -f .mfiles
%dir %{_javadir}/%{name}
%files javadoc -f .mfiles-javadoc

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-0.38.alpha15
- Import
