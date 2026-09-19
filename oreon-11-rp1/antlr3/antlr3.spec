%global source0_hash 34702dcbb6d52877aaaede6de4a685bc57e4680f7e029f8aa97906042ba90e27

%global antlr_version 3.5.3
%global javascript_runtime_version 3.1
%global baserelease 18

# This package needs itself to build.  Use this to bootstrap on a new system.
%bcond bootstrap 0

# Component versions to use when bootstrapping
%global antlr2_version 2.7.7
%global bootstrap_version 3.5
%global ST4ver1 4.0.7
%global ST4ver2 4.0.8
%global stringtemplatever 3.2.1

%global giturl  https://github.com/antlr/antlr3

Summary:        ANother Tool for Language Recognition
Name:           antlr3
Epoch:          1
Version:        %{antlr_version}
Release:        %{baserelease}%{?dist}
# Sources are BSD-3-Clause with the following exceptions:
# BSD-3-Clause OR GPL-1.0-or-later OR Artistic-1.0-Perl:
#   runtime/Perl5/Build.PL, runtime/Perl5/lib/ANTLR/Runtime.pm
# Apache-2.0: antlr-ant/main/antlr3-task/antlr3-src/org/apache/tools/ant/antlr/ANTLR3.java
# MIT: runtime/CSharp2/Sources/Antlr3.Runtime/Antlr.Runtime.JavaExtensions/Check.cs
# FSFAP: runtime/C/INSTALL
# LicenseRef-Fedora-Public-Domain: runtime/Python/xmlrunner.py
# LicenseRef-Unicode-legacy-source-code (not allowed in Fedora):
#    runtime/C/include/antlr3convertutf.h
#    runtime/C/src/antlr3convertutf.c
#    runtime/Cpp/include/antlr3convertutf.hpp
# Unknown: runtime/CSharp2/LICENSE.TXT and runtime/Delphi/LICENSE.TXT add a
#   copyleft clause to BSD-3-Clause.  SPDX has no name for it.  We don't ship
#   anything derived from C# or Delphi files in the binary RPM.
License:        BSD-3-Clause
SourceLicense:  %{license} AND (BSD-3-Clause OR GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0 AND MIT AND FSFAP AND LicenseRef-Fedora-Public-Domain
URL:            https://www.antlr3.org/
VCS:            git:%{giturl}.git

Source0:        %{giturl}/archive/%{antlr_version}/%{name}-%{antlr_version}.tar.gz
Source1:        http://www.antlr3.org/download/antlr-javascript-runtime-%{javascript_runtime_version}.zip
%if %{with bootstrap}
# Get prebuilt versions to bootstrap
Source2:        https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver1}/ST4-%{ST4ver1}.jar
Source3:        https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver1}/ST4-%{ST4ver1}.pom
Source4:        https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver2}/ST4-%{ST4ver2}.jar
Source5:        https://repo1.maven.org/maven2/org/antlr/ST4/%{ST4ver2}/ST4-%{ST4ver2}.pom
Source6:        https://repo1.maven.org/maven2/org/antlr/antlr/%{bootstrap_version}/antlr-%{bootstrap_version}.jar
Source7:        https://repo1.maven.org/maven2/org/antlr/antlr/%{bootstrap_version}/antlr-%{bootstrap_version}.pom
Source8:        https://repo1.maven.org/maven2/org/antlr/antlr-master/%{bootstrap_version}/antlr-master-%{bootstrap_version}.pom
Source9:        https://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{bootstrap_version}/antlr-runtime-%{bootstrap_version}.jar
Source10:       https://repo1.maven.org/maven2/org/antlr/antlr-runtime/%{bootstrap_version}/antlr-runtime-%{bootstrap_version}.pom
Source11:       https://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}/antlr3-maven-plugin-%{bootstrap_version}.jar
Source12:       https://repo1.maven.org/maven2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}/antlr3-maven-plugin-%{bootstrap_version}.pom
Source13:       https://repo1.maven.org/maven2/org/antlr/stringtemplate/%{stringtemplatever}/stringtemplate-%{stringtemplatever}.jar
Source14:       https://repo1.maven.org/maven2/org/antlr/stringtemplate/%{stringtemplatever}/stringtemplate-%{stringtemplatever}.pom
Source15:       https://repo1.maven.org/maven2/antlr/antlr/%{antlr2_version}/antlr-%{antlr2_version}.jar
Source16:       https://repo1.maven.org/maven2/antlr/antlr/%{antlr2_version}/antlr-%{antlr2_version}.pom
%endif

Patch:          0001-java8-fix.patch
# Generate OSGi metadata
Patch:          osgi-manifest.patch
# Increase the default conversion timeout to avoid build failures when complex
# grammars are processed on slow architectures.  Patch from Debian.
Patch:          0002-conversion-timeout.patch
# Fix problems with the C template.  Patch from Debian.
Patch:          0003-fix-c-template.patch
# Keep Token.EOF_TOKEN for backwards compatibility.  Patch from Debian.
Patch:          0004-eof-token.patch
# Make parsers reproducible.  Patch from Debian.
Patch:          0005-reproducible-parsers.patch
# Fix for C++20
Patch:          0006-antlr3memory.hpp-fix-for-C-20-mode.patch
# Compile for target 1.8 to fix build with JDK 11
Patch:          0007-update-java-target.patch
# Fix source for tighter gcc template checks
Patch:          0008-unconst-cyclicdfa-gcc-14.patch

BuildRequires:  ant-openjdk25 
BuildRequires:  make
BuildRequires:  maven-local-openjdk25
%if %{without bootstrap}
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.antlr:stringtemplate)
%endif
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# This can be removed when F48 reaches EOL
# The C/C++ backend contains files with the not-allowed
# LicenseRef-Unicode-legacy-source-code license
Obsoletes:      %{name}-C < 3.5.3-18
Obsoletes:      %{name}-C-devel < 3.5.3-18
Obsoletes:      %{name}-C++-devel < 3.5.3-18
Obsoletes:      %{name}-C-docs < 3.5.3-18
Provides:       %{name}-C = %{version}-%{release}
Provides:       %{name}-C-devel = %{version}-%{release}
Provides:       %{name}-C++-devel = %{version}-%{release}
Provides:       %{name}-C-docs = %{version}-%{release}

%description
ANother Tool for Language Recognition, is a language tool that provides a
framework for constructing recognizers, interpreters, compilers, and
translators from grammatical descriptions containing actions in a variety of
target languages.

%package        tool
Summary:        ANother Tool for Language Recognition
License:        BSD-3-Clause AND Apache-2.0
Provides:       %{name} = %{epoch}:%{antlr_version}-%{release}
Obsoletes:      %{name} < %{epoch}:%{antlr_version}-%{release}
Requires:       %{name}-java = %{epoch}:%{antlr_version}-%{release}
# Explicit requires for javapackages-tools since antlr3-script
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description    tool
ANother Tool for Language Recognition, is a language tool that provides a
framework for constructing recognizers, interpreters, compilers, and
translators from grammatical descriptions containing actions in a variety of
target languages.

%package        java
Summary:        Java run-time support for ANTLR-generated parsers

%description    java
Java run-time support for ANTLR-generated parsers

%package        javadoc
Summary:        API documentation for %{name}

%description    javadoc
%{summary}.

%package        javascript
Summary:        Javascript run-time support for ANTLR-generated parsers
Version:        %{javascript_runtime_version}
Release:        %{antlr_version}.%{baserelease}%{?dist}

%description    javascript
Javascript run-time support for ANTLR-generated parsers

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n antlr3-%{antlr_version} -a 1

%conf
sed -i "s,\${buildNumber},`cat %{_sysconfdir}/fedora-release` `date`," tool/src/main/resources/org/antlr/antlr.properties

# remove pre-built artifacts
find -type f -a -name *.jar -delete
find -type f -a -name *.class -delete

%pom_remove_parent

%pom_disable_module antlr3-maven-archetype
%pom_disable_module gunit
%pom_disable_module gunit-maven-plugin
%pom_disable_module antlr-complete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin -r :maven-javadoc-plugin

# workarounds bug in filtering (Mark invalid)
%pom_xpath_remove pom:resource/pom:filtering

%mvn_package :antlr-runtime java
%mvn_package : tool

%mvn_file :antlr antlr3
%mvn_file :antlr-runtime antlr3-runtime
%mvn_file :antlr-maven-plugin antlr3-maven-plugin

%if %{with bootstrap}
# Make the bootstrap JARs and POMs available
mkdir -p .m2/org/antlr/ST4/%{ST4ver1}
cp -p %{SOURCE2} %{SOURCE3} .m2/org/antlr/ST4/%{ST4ver1}
mkdir -p .m2/org/antlr/ST4/%{ST4ver2}
cp -p %{SOURCE4} %{SOURCE5} .m2/org/antlr/ST4/%{ST4ver2}
mkdir -p .m2/org/antlr/antlr/%{bootstrap_version}
cp -p %{SOURCE6} %{SOURCE7} .m2/org/antlr/antlr/%{bootstrap_version}
mkdir -p .m2/org/antlr/antlr-master/%{bootstrap_version}
cp -p %{SOURCE8} .m2/org/antlr/antlr-master/%{bootstrap_version}
mkdir -p .m2/org/antlr/antlr-runtime/%{bootstrap_version}
cp -p %{SOURCE9} %{SOURCE10} .m2/org/antlr/antlr-runtime/%{bootstrap_version}
mkdir -p .m2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}
cp -p %{SOURCE11} %{SOURCE12} .m2/org/antlr/antlr3-maven-plugin/%{bootstrap_version}
mkdir -p .m2/org/antlr/stringtemplate/%{stringtemplatever}
cp -p %{SOURCE13} %{SOURCE14} .m2/org/antlr/stringtemplate/%{stringtemplatever}
mkdir -p .m2/antlr/antlr/%{antlr2_version}
cp -p %{SOURCE15} %{SOURCE16} .m2/antlr/antlr/%{antlr2_version}

# We don't need the parent POM
%pom_remove_parent .m2/org/antlr/ST4/%{ST4ver1}/ST4-%{ST4ver1}.pom
%pom_remove_parent .m2/org/antlr/ST4/%{ST4ver2}/ST4-%{ST4ver2}.pom
%pom_remove_parent .m2/org/antlr/antlr-master/%{bootstrap_version}/antlr-master-%{bootstrap_version}.pom
%endif

%build
%mvn_build -f

# build ant task
pushd antlr-ant/main/antlr3-task/
export CLASSPATH=$(build-classpath ant)
javac -encoding ISO-8859-1 -source 1.8 -target 1.8 \
  antlr3-src/org/apache/tools/ant/antlr/ANTLR3.java
jar cvf ant-antlr3.jar \
  -C antlr3-src org/apache/tools/ant/antlr/antlib.xml \
  -C antlr3-src org/apache/tools/ant/antlr/ANTLR3.class
popd

%install
mkdir -p $RPM_BUILD_ROOT/%{_mandir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/antlr

%mvn_install

# install ant task
install -m 644 antlr-ant/main/antlr3-task/ant-antlr3.jar -D $RPM_BUILD_ROOT%{_javadir}/ant/ant-antlr3.jar
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-antlr3 << EOF
ant/ant-antlr3 antlr3
EOF

# install wrapper script
%jpackage_script org.antlr.Tool '' '' 'stringtemplate4/ST4.jar:antlr3.jar:antlr3-runtime.jar' antlr3 true

# install javascript runtime
pushd antlr-javascript-runtime-%{javascript_runtime_version}
install -pm 644 *.js $RPM_BUILD_ROOT%{_datadir}/antlr/
popd

%files tool -f .mfiles-tool
%doc README.txt tool/{LICENSE.txt,CHANGES.txt}
%{_bindir}/antlr3
%{_javadir}/ant/ant-antlr3.jar
%config(noreplace) %{_sysconfdir}/ant.d/ant-antlr3

%files java -f .mfiles-java
%doc tool/LICENSE.txt

%files javascript
%doc tool/LICENSE.txt
%{_datadir}/antlr/

%files javadoc -f .mfiles-javadoc
%doc tool/LICENSE.txt

%changelog
%autochangelog
