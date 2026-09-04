%global source0_hash 652c4f0f572675fec969a29872dfbe98bdead4c16ed5d9650e9e3d6810c4d1a3

%global project     clojure
%global groupId     org.clojure
%global artifactId  clojure
%global archivename %{project}-%{artifactId}
%define add_determinism_options --handler=-jar

Name:           clojure
Epoch:          1
Version:        1.12.6
Release:        1%{?dist}
Summary:        A dynamic programming language that targets the Java Virtual Machine

License:        EPL-1.0
URL:            http://clojure.org/
Source0:        https://github.com/%{name}/%{name}/archive/%{name}-%{version}.zip

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.clojure:core.specs.alpha)
BuildRequires:  mvn(org.clojure:spec.alpha)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
Requires:       javapackages-tools

%description 
Clojure is a dynamic programming language that targets the Java
Virtual Machine. It is designed to be a general-purpose language,
combining the approachability and interactive development of a
scripting language with an efficient and robust infrastructure for
multithreaded programming. Clojure is a compiled language - it
compiles directly to JVM bytecode, yet remains completely
dynamic. Every feature supported by Clojure is supported at
runtime. Clojure provides easy access to the Java frameworks, with
optional type hints and type inference, to ensure that calls to Java
can avoid reflection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{archivename}-%{version}

%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-javadoc-plugin

%build
%mvn_build -f -j

%install

%mvn_install

# startup script
%jpackage_script clojure.main "" "" clojure:clojure-spec-alpha:clojure-core-specs-alpha clojure false

%files -f .mfiles
%license epl-v10.html 
%doc changes.md readme.txt 
%{_bindir}/%{name}

%changelog
%autochangelog
