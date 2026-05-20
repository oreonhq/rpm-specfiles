Name:           xmvn-connector-ivy
Version:        4.0.0
Release:        %autorelease
Summary:        XMvn Connector for Apache Ivy
License:        Apache-2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/fedora-java/xmvn-connector-ivy/releases/download/%{version}/xmvn-connector-ivy-%{version}.tar.xz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.ivy:ivy)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fedoraproject.xmvn:xmvn-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.slf4j:slf4j-api)
BuildRequires:  mvn(org.slf4j:slf4j-simple)

%description
This package provides XMvn Connector for Apache Ivy, which provides
integration of Apache Ivy with XMvn.  It provides an adapter which
allows XMvn resolver to be used as Ivy resolver.

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
This package provides %{summary}.

%prep
%setup -q

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Fri May 08 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.0-1
- Import from Fedora f44 dist-git for ivy-local / javapackages-tools chain
