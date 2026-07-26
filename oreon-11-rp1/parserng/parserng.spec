%global source0_hash 5d116882f3b0852876c339782773c48ee30935f2219cfadb1f3ee52b210a2990

Summary: %{nice_name} is a powerful open-source tool that parses and evaluates algebraic and mathematical expressions
%global nice_name ParserNG
Name: parserng
Version: 0.1.9
Release: 11%{?dist}
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License: Apache-2.0
URL: https://github.com/gbenroscience/ParserNG
# tarred cloned repo without hidden files and without idea iml
# usptream do not tag, but uses maven versionining
# so this is f619fad1fefa21116bab4a0abba2dd0ebe719e45
# which set pom to 0.1.9 and moved it to maven repos
# git clone https://github.com/gbenroscience/ParserNG &&  cd ParserNG  && git checkout f619fad1fefa21116bab4a0abba2dd0ebe719e45 && tar -cJf parserng-0.1.9.tar.xz *
Source0: %{name}-%{version}.tar.xz
Source1: parserng
Patch1: jdk21rounding.patch

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: maven-local-openjdk25
BuildRequires: junit5
BuildRequires: ant-junit5
BuildRequires: junit
BuildRequires: ant-junit
BuildRequires: maven-surefire-provider-junit
BuildRequires: maven-surefire-provider-junit5
BuildRequires: maven-surefire
BuildRequires: maven-surefire-plugin
BuildRequires: maven-clean-plugin
BuildRequires: java-25-devel
Requires: java-25-headless
Provides: ParserNG
Provides: parser-ng

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

%files -f .mfiles
%license LICENSE
%{_bindir}/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
