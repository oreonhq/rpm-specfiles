%global source0_hash 5d116882f3b0852876c339782773c48ee30935f2219cfadb1f3ee52b210a2990
Summary:        ParserNG is a powerful open-source tool that parses and evaluates algebraic and mathematical expressions
%global nice_name ParserNG
Name: parserng
Version: 3.0.7
Release:        1%{?dist}
License: Apache-2.0
URL: https://github.com/gbenroscience/ParserNG
Source0:        %{name}-%{version}.tar.xz
Source1: parserng
Patch1: jdk21rounding.patch
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Requires: java-25-headless
Provides: ParserNG
Provides: parser-ng
# oreon:deps
BuildRequires:  ant-junit
BuildRequires:  ant-junit5
BuildRequires:  java-25-devel
BuildRequires:  junit
BuildRequires:  junit5
BuildRequires:  maven-clean-plugin
BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-surefire
BuildRequires:  maven-surefire-plugin
BuildRequires:  maven-surefire-provider-junit
BuildRequires:  maven-surefire-provider-junit5
# /oreon:deps
%description
Rich and Performant, Cross Platform Java Library(100% Java)...
Now allows the differentiation function to be differentiated with
respect to any variable(not just x).  Next to math.Main main cmdline entry point 
also parser.MathExpression and parser.cmd.ParserCmd  are here for cmdline service

%package javadoc
Summary: Javadoc for %{name}
Requires: %{name} = %{version}-%{release}
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -c %{name}-%{version}
%patch -P1 -p1
for x in `find | grep pom.xml` ; do
    sed "s;<maven.compiler.source>.*7.*;<maven.compiler.source>8</maven.compiler.source>;g" -i $x;
    sed "s;<maven.compiler.target>.*7.*;<maven.compiler.target>8</maven.compiler.target>;g" -i $x;
done

%build

%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%mvn_build
%install
%mvn_install
install -d -m 755 $RPM_BUILD_ROOT%{_bindir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_bindir}/
chmod 755 $RPM_BUILD_ROOT%{_bindir}/%{name}
install -d -m 755 $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n parserng-javadoc -f %{oreon_filedir}/parserng-javadoc.list

%changelog

%autochangelog
