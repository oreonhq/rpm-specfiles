%global source0_hash 80d786485f89ff60fe8935d293e30343861497167d14129d02be1f4159480ee5

%global namedreltag  -alpha-11
%global namedversion %{version}%{?namedreltag}
%global dotreltag    %(echo %{namedreltag} | tr - .)

Name:          maven-native
Version:       1.0
Release:       0.24%{dotreltag}%{?dist}
Summary:       Compile c and c++ source under Maven
# Automatically converted from old format: ASL 2.0 and MIT - review is highly recommended.
License:       Apache-2.0 AND LicenseRef-Callaway-MIT
Url:           https://github.com/mojohaus/maven-native/
Source0:       https://repo1.maven.org/maven2/org/codehaus/mojo/natives/%{name}/%{namedversion}/%{name}-%{namedversion}-source-release.zip
Source1:       plexus_components-bcc.xml
Source2:       plexus_components-generic-c.xml
Source3:       plexus_components-manager.xml
Source4:       plexus_components-msvc.xml

BuildRequires: maven-local-openjdk25
BuildRequires: mojo-parent
BuildRequires: mvn(aopalliance:aopalliance)
BuildRequires: mvn(bcel:bcel)
BuildRequires: mvn(junit:junit)
BuildRequires: mvn(net.sf.cglib:cglib)
BuildRequires: mvn(org.apache.maven:maven-artifact)
BuildRequires: mvn(org.apache.maven:maven-model)
BuildRequires: mvn(org.apache.maven:maven-plugin-api)
BuildRequires: mvn(org.apache.maven:maven-compat)
BuildRequires: mvn(org.apache.maven:maven-core)
BuildRequires: mvn(org.apache.maven.plugins:maven-enforcer-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires: mvn(org.apache.maven.plugin-testing:maven-plugin-testing-harness)
BuildRequires: mvn(org.codehaus.plexus:plexus-archiver)
BuildRequires: mvn(org.codehaus.plexus:plexus-container-default)
BuildRequires: mvn(org.codehaus.plexus:plexus-utils)

BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

%description
Maven Native - compile C and C++ source under Maven
with compilers such as GCC, MSVC, GCJ etc ...

%package components
Summary:       Maven Native Components

%description components
%{summary}.

%package -n native-maven-plugin
Summary:       Native Maven Plugin

%description -n native-maven-plugin
%{summary}.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{namedversion}

for d in LICENSE ; do
  iconv -f iso8859-1 -t utf-8 $d.txt > $d.txt.conv && mv -f $d.txt.conv $d.txt
  sed -i 's/\r//' $d.txt
done

# use jvm apis
%pom_remove_dep backport-util-concurrent:backport-util-concurrent
%pom_remove_dep backport-util-concurrent:backport-util-concurrent maven-native-api
sed -i "s|edu.emory.mathcs.backport.java.util.concurrent|java.util.concurrent|" \
 maven-native-api/src/main/java/org/codehaus/mojo/natives/compiler/AbstractCompiler.java

sed -i 's|<artifactId>maven-project|<artifactId>maven-compat|' pom.xml
%pom_remove_plugin com.github.ekryd.sortpom:sortpom-maven-plugin
%pom_remove_plugin org.codehaus.plexus:plexus-component-metadata maven-native-components
%pom_remove_plugin org.codehaus.plexus:plexus-component-metadata native-maven-plugin
%pom_add_dep org.apache.maven:maven-compat native-maven-plugin
%pom_add_dep org.apache.maven:maven-core native-maven-plugin

# missing test deps
%pom_add_dep aopalliance:aopalliance::test native-maven-plugin
%pom_add_dep net.sf.cglib:cglib::test native-maven-plugin

%mvn_package ":%{name}" %{name}
%mvn_package ":%{name}-api" %{name}
%mvn_package ":%{name}-components" components
%mvn_package ":%{name}-bcc" components
%mvn_package ":%{name}-generic-c" components
%mvn_package ":%{name}-javah" components
%mvn_package ":%{name}-manager" components
%mvn_package ":%{name}-msvc" components
%mvn_package ":%{name}-mingw" components
%mvn_package ":native-maven-plugin" native-maven-plugin

mkdir -p ./maven-native-components/maven-native-{bcc,generic-c,manager,msvc}/src/main/resources/META-INF/plexus/
for CMP in bcc generic-c manager msvc
do
	cp -a %{_sourcedir}/plexus_components-$CMP.xml ./maven-native-components/maven-native-$CMP/src/main/resources/META-INF/plexus/components.xml
done

%build

#  junit.framework.AssertionFailedError: Failed to create plexus container.
# native-maven-plugin with maven3 test failures:
# Caused by: java.lang.ClassNotFoundException: org.apache.maven.artifact.repository.Authentication
#  java.lang.VerifyError: (class: org/apache/maven/project/MavenProject, 
# method: getSnapshotArtifactRepository signature: ()Lorg/apache/maven/artifact/repository/ArtifactRepository;)
# Incompatible argument to function
# force org.codehaus.plexus plexus-container-default 1.5.5 apis
# test skipped cause: [ERROR] Failed to execute goal org.apache.maven.plugins:maven-surefire-plugin:2.15:test (default-test) on project native-maven-plugin: Execution default-test of goal org.apache.maven.plugins:maven-surefire-plugin:2.15:test failed: There was an error in the forked process
# [ERROR] java.lang.NoClassDefFoundError: org/sonatype/aether/RepositorySystemSession
%mvn_build -f -s --xmvn-javadoc -- -Dmaven.test.failure.ignore=true

%install
%mvn_install

%files -f .mfiles-%{name}
%dir %{_javadir}/%{name}
%license LICENSE.txt

%files components -f .mfiles-components
%license LICENSE.txt

%files -n native-maven-plugin -f .mfiles-native-maven-plugin
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt

%changelog
%autochangelog
