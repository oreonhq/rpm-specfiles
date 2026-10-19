%global source16_hash 100f793ba27f8b4e4204edb46171ebf36e54e0f94cfc02527fea07a0bb1fceb7
%global source15_hash 88fbda4b912596b9f56e8e12e580cc954bacfb51776ecfddd3e18fc1cf56dc4c
%global source14_hash b45e82655aa5a48f33d13a43e4345426b156335b35e24b5aea12db5823c16a16
%global source13_hash f66ce72e965e5301cb0f020e54d2ba6ad76feb91b3cbfc30dbbf00c06a6df6d7
%global source12_hash 09ca961a122ab9d5d1ce991fd40120e9ec9c111e028bcaa2ae504b61f896d1d0
%global source11_hash 7ce07334cc00d76370cf3731dc3676701816f9b0c98c4babd11df8df79824329
%global source10_hash 962555d234024ba737989bf0c1d9f868b322891e4bbb52b4240aae112cb4a480
%global source9_hash 7ef52a4e25ea2472a0ae62ae1d5ccaa7ef23be188289ad225fcb8a452a1b738d
%global source8_hash a7b54c6afbc51b7b970438a7e64d55591a1538b087bdeb4ddcc3036de36de664
%global source7_hash e076e8ba2d2f8802a82d889fb244e7ac552afa95ff879deb3ae991a2babc0689
%global source6_hash a9b240744ac20f97972da42ead1a8b6df465c2000d5bb9ba297b1e1e74f0fe26
%global source5_hash 3c0890dec71174eb3ba3d404ca9e341901ff6b0421808b00713b0dbb1306c17c
%global source4_hash 58caabc40c9f74b0b5993fd868e0f64a50c0759094e6a251aaafad98edfc7a3b
%global source3_hash d00121f847deddacc29e6a515c4d47c69d81c21e07ed30f589c11f85fdb8207b
%global source2_hash 29bfb0d6a4531644378b68d2c11a51450949bd640fd40e15f169efbeb8afa425
%global source1_hash 34702dcbb6d52877aaaede6de4a685bc57e4680f7e029f8aa97906042ba90e27
%global source0_hash 34702dcbb6d52877aaaede6de4a685bc57e4680f7e029f8aa97906042ba90e27
%global antlr_version 3.5.3
%global javascript_runtime_version 3.1
%global baserelease 18
%bcond bootstrap 0
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
Release:        1%{?dist}
License:        BSD-3-Clause
SourceLicense:  %{license} AND (BSD-3-Clause OR GPL-1.0-or-later OR Artistic-1.0-Perl) AND Apache-2.0 AND MIT AND FSFAP AND LicenseRef-Fedora-Public-Domain
URL:            https://www.antlr3.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/%{version}/%{name}-%{version}.tar.gz
Source1:        http://www.antlr3.org/download/antlr-javascript-runtime-%{javascript_runtime_version}.zip
%if %{with bootstrap}
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
Patch:          osgi-manifest.patch
Patch:          0002-conversion-timeout.patch
Patch:          0003-fix-c-template.patch
Patch:          0004-eof-token.patch
Patch:          0005-reproducible-parsers.patch
Patch:          0006-antlr3memory.hpp-fix-for-C-20-mode.patch
Patch:          0007-update-java-target.patch
Patch:          0008-unconst-cyclicdfa-gcc-14.patch
%if %{without bootstrap}
%endif
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Obsoletes:      %{name}-C < 3.5.3-18
Obsoletes:      %{name}-C-devel < 3.5.3-18
Obsoletes:      %{name}-C++-devel < 3.5.3-18
Obsoletes:      %{name}-C-docs < 3.5.3-18
Provides:       %{name}-C = %{version}-%{release}
Provides:       %{name}-C-devel = %{version}-%{release}
Provides:       %{name}-C++-devel = %{version}-%{release}
Provides:       %{name}-C-docs = %{version}-%{release}
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  make
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.antlr:ST4)
BuildRequires:  mvn(org.antlr:antlr)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  mvn(org.antlr:stringtemplate)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-compiler-api)
# /oreon:deps
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
install -m 644 antlr-ant/main/antlr3-task/ant-antlr3.jar -D $RPM_BUILD_ROOT%{_javadir}/ant/ant-antlr3.jar
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/ant.d
cat > $RPM_BUILD_ROOT%{_sysconfdir}/ant.d/ant-antlr3 << EOF
ant/ant-antlr3 antlr3
EOF
%jpackage_script org.antlr.Tool '' '' 'stringtemplate4/ST4.jar:antlr3.jar:antlr3-runtime.jar' antlr3 true
pushd antlr-javascript-runtime-%{javascript_runtime_version}
install -pm 644 *.js $RPM_BUILD_ROOT%{_datadir}/antlr/
popd
%oreon_autofiles antlr3-tool usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles antlr3-java usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles antlr3-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles antlr3-javascript usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n antlr3-tool -f %{oreon_filedir}/antlr3-tool.list
%files -n antlr3-java -f %{oreon_filedir}/antlr3-java.list
%files -n antlr3-javadoc -f %{oreon_filedir}/antlr3-javadoc.list
%files -n antlr3-javascript -f %{oreon_filedir}/antlr3-javascript.list

%changelog

%autochangelog
