%global source0_hash 5a9a04a2a6cb9a93a53aa865b6e118f6aa9e5e051acd8333ca99af82148fd211

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
Source0:        %{name}-%{project_version}.tar.gz

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  java-devel >= 1:1.6.0
BuildRequires:  maven-local
BuildRequires:  maven-assembly-plugin
BuildRequires:  maven-resources-plugin
BuildRequires:  maven-plugin-plugin
BuildRequires:  plexus-classworlds
# requires as parent pom
BuildRequires:  plexus-containers

%description
Plexus Component API

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
API documentation for %{name}.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n %{name}-%{project_version}

%build
%mvn_build

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
