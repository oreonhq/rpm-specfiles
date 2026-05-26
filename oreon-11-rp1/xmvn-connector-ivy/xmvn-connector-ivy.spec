Name:           xmvn-connector-ivy
Version:        4.0.0
Release:        %autorelease
Summary:        XMvn Connector for Apache Ivy
License:        Apache-2.0
URL:            https://fedora-java.github.io/xmvn/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/fedora-java/xmvn-connector-ivy/releases/download/%{version}/xmvn-connector-ivy-%{version}.tar.xz
# oreon url source checksums begin
%global source0_sha256 a5357ab35f1123d6f295c393e122a43097d1717fb72b807a795af54ddfe1beb2
%global source0_file xmvn-connector-ivy-4.0.0.tar.xz
# oreon url source checksums end

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/xmvn-connector-ivy-4.0.0.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "a5357ab35f1123d6f295c393e122a43097d1717fb72b807a795af54ddfe1beb2" || { echo "oreon: Source0 SHA256 mismatch for xmvn-connector-ivy-4.0.0.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
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
- Import to oreon 11