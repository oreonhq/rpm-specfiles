%global source0_hash none

Name:           jline2
Version:        2.14.6
Release:        17%{?dist}
Summary:        Java library for handling console input
License:        BSD-3-Clause
URL:            http://jline.github.io/jline2/

Source0:        https://github.com/jline/jline2/archive/jline-%{version}.tar.gz

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.fusesource.jansi:jansi:1)

%description
JLine is a Java library for handling console input.  It is similar in
functionality to BSD editline and GNU readline.  People familiar with
the readline/editline capabilities for modern shells (such as bash and
tcsh) will find most of the command editing features of JLine to be
familiar.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n jline2-jline-%{version}

# remove unnecessary dependency on parent POM
%pom_remove_parent

# Remove maven-shade-plugin usage
%pom_remove_plugin "org.apache.maven.plugins:maven-shade-plugin"
# Remove animal sniffer plugin in order to reduce deps
%pom_remove_plugin "org.codehaus.mojo:animal-sniffer-maven-plugin"

# Remove unavailable and unneeded deps
%pom_xpath_remove "pom:build/pom:extensions"
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-javadoc-plugin

# Makes the build fail on deprecation warnings from jansi
%pom_xpath_remove 'pom:arg[text()="-Werror"]'

# Do not import non-existing internal package
%pom_xpath_remove "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Import-Package"
%pom_xpath_inject "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions" "<Import-Package>javax.swing;resolution:=optional,org.fusesource.jansi,!org.fusesource.jansi.internal</Import-Package>"

# Be sure to export jline.internal, but not org.fusesource.jansi.
# See https://bugzilla.redhat.com/show_bug.cgi?id=1317551
%pom_xpath_set "pom:build/pom:plugins/pom:plugin[pom:artifactId = 'maven-bundle-plugin']/pom:executions/pom:execution/pom:configuration/pom:instructions/pom:Export-Package" "jline.*;-noimport:=true"

# Update required version of jansi 1.x
%pom_xpath_set //pom:jansi.version 1.18

# drop a nondeterministic test
find -name TerminalFactoryTest.java -delete
# it's also the only test that uses powermock, so drop the powermock dependency
%pom_remove_dep org.powermock:

# Fix javadoc generation on java 11
%pom_xpath_inject pom:build/pom:plugins "<plugin>
<artifactId>maven-javadoc-plugin</artifactId>
<configuration><source>1.8</source></configuration>
</plugin>"

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%files -f .mfiles
%doc CHANGELOG.md README.md
%license LICENSE.txt

%changelog
%autochangelog

