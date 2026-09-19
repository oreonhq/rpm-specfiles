%global source0_hash a71a70dfe7d77f90a2d53762c88d9dd69c4d067fe37f6f1adf1a69b72a7945e3

Name:           CFR
Version:        0.152
Release:        2%{?dist}
Summary:        CFR - Another Java Decompiler

License:        MIT
URL:            https://github.com/leibnitz27/cfr
Source0:        https://github.com/leibnitz27/cfr/archive/refs/tags/%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  maven-compiler-plugin

Requires:       java-headless
Requires:       javapackages-tools

Provides:       cfr
Provides:       Cfr

%global lowercase_name cfr
%global build_folder %{lowercase_name}-%{version}

%description
CFR will decompile modern Java features - including much of Java 9, 12 & 14,21 and 25
but is written entirely in Java 6, so will work anywhere!
It'll even make a decent go of turning class files from other JVM languages back into java!

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{build_folder}
%pom_remove_plugin :git-commit-id-plugin
%pom_remove_plugin :templating-maven-plugin
%pom_remove_plugin :maven-jar-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-gpg-plugin
sed "s;<javaVersion>1.6</javaVersion>;<javaVersion>1.8</javaVersion>;" -i pom.xml

# workaround for template-maven-plugin
sed -i 's/${project.version}/%{version}/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
sed -i 's/${git.commit.id.abbrev}/%{version}/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
sed -i 's/${git.dirty}/false/' %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java
cp %{_builddir}/%{build_folder}/src-templates/org/benf/cfr/reader/util/CfrVersionInfo.java %{_builddir}/%{build_folder}/src/org/benf/cfr/reader/util/CfrVersionInfo.java

%build
%mvn_build

%install
rm -rf $RPM_BUILD_ROOT
%mvn_install
%jpackage_script org.benf.cfr.reader.Main "" "" %{name}/%{name} %{lowercase_name}

%files -f .mfiles
%license LICENSE
%doc README.md
%{_bindir}/%{lowercase_name}

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
