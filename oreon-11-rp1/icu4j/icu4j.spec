%global source0_hash f06bcab72736ee9d55689033b8198a178562354128cf38edb2afc2e67e3fd931
%global giturl  https://github.com/unicode-org/icu
Name:           icu4j
Version:        78.3
Release:        1%{?dist}
Epoch:          1
Summary:        International Components for Unicode for Java
License:        Unicode-3.0
URL:            https://icu.unicode.org/
VCS:            git:%{giturl}.git
Source0:        https://github.com/unicode-org/icu/archive/refs/tags/release-78.3.tar.gz#/icu4j-78.3.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Obsoletes:      %{name}-localespi < 78
Provides:       %{name}-localespi = 1:%{version}-%{release}
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.gson:gson)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-assembly-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-compiler-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-jar-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-resources-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-shade-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-surefire-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:exec-maven-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus-io)
BuildRequires:  mvn(pl.pragmatists:JUnitParams)
# /oreon:deps
%description
The International Components for Unicode (ICU) library provides robust and
full-featured Unicode services on a wide variety of platforms. ICU supports
the most current version of the Unicode standard, and provides support for
supplementary characters (needed for GB 18030 repertoire support).

Java provides a very strong foundation for global programs, and IBM and the
ICU team played a key role in providing globalization technology into Sun's
Java. But because of its long release schedule, Java cannot always keep
up-to-date with evolving standards. The ICU team continues to extend Java's
Unicode and internationalization support, focusing on improving performance,
keeping current with the Unicode standard, and providing richer APIs, while
remaining as compatible as possible with the original Java text and
internationalization API design.

%package        charset
Summary:        Charset converter library of %{name}
Requires:       %{name} = 1:%{version}-%{release}
%description    charset
Charset converter library of %{name}.

%package        parent
Summary:        Parent POM for %{name}
%description    parent
Parent POM for %{name}.

%package        javadoc
License:        Unicode-3.0 AND MIT
Summary:        API documentation for %{name}
Provides:       bundled(js-jquery)
%description    javadoc
API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n icu-release-%{version}

%conf
cd icu4j
# Unnecessary plugins for an RPM build
%pom_remove_plugin -r :flatten-maven-plugin
%pom_remove_plugin -r :maven-clean-plugin
%pom_remove_plugin -r :maven-deploy-plugin
%pom_remove_plugin :central-publishing-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-install-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :maven-pmd-plugin
%pom_remove_plugin :maven-project-info-reports-plugin
%pom_remove_plugin :maven-release-plugin
%pom_remove_plugin :maven-site-plugin

# Modules we do not want to ship
%pom_disable_module demos
%pom_disable_module perf-tests
%pom_disable_module samples
%pom_disable_module tools/build
%pom_disable_module tools/misc
%pom_disable_module tools/pmd
cd -

%build

cd icu4j
%mvn_build -s
cd -
%install
cd icu4j
%mvn_install
cd -
rm %{buildroot}%{_javadir}/icu4j/{common_tests,framework}.jar
rm %{buildroot}%{_datadir}/maven-metadata/icu4j-{common_tests,framework}.xml
rm %{buildroot}%{_mavenpomdir}/icu4j/{common_tests,framework}.pom
sed -i '/%dir/d' icu4j/.mfiles-{c,f,l,r,t}* icu4j/.mfiles-icu4j-charset
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n icu4j-charset -f %{oreon_filedir}/icu4j-charset.list
%files -n icu4j-parent -f %{oreon_filedir}/icu4j-parent.list
%files -n icu4j-javadoc -f %{oreon_filedir}/icu4j-javadoc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 78.3-1
- Prepare for Oreon 11 (RP1)
