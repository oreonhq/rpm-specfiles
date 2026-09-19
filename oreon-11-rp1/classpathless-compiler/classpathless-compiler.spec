%global source0_hash bdc11f4be08011d4545f8253a7f64785c6bdc65011c86e14bed51899248efd94

%global cli_tool cplc

Name:           classpathless-compiler
Version:        2.4
Release:        %autorelease
Summary:        Tool for recompiling java sources with customizable class providers
License:        Apache-2.0
URL:            https://github.com/mkoncek/classpathless-compiler
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  jurand
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)
BuildRequires:  mvn(org.ow2.asm:asm-tree)

Requires:       beust-jcommander
Requires:       javapackages-tools

# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.3-5

%description
Classpathless compiler (CPLC) is a compiler wrapper used for compiling java
sources with customizable class providers. This tool works differently from the
traditional java compiler in that it doesn't use provided classpath but instead
pulls dependencies using an API.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n classpathless-compiler-%{version}

%java_remove_annotations -s -n SuppressFBWarnings .

%pom_remove_dep :spotbugs-annotations

%pom_remove_plugin :maven-assembly-plugin impl
%pom_remove_plugin :maven-dependency-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin

%build
%mvn_build -j

%install
%mvn_install

%jpackage_script io.github.mkoncek.classpathless.Tool "" "" classpathless-compiler/classpathless-compiler:classpathless-compiler/classpathless-compiler-api:classpathless-compiler/classpathless-compiler-util:beust-jcommander %{cli_tool}

%files -f .mfiles
%{_bindir}/%{cli_tool}

%license LICENSE
%doc README.md

%changelog
%autochangelog
