%global source0_hash 84afe6ee3c42b2165aa129f3730972634b9d3d8d774e5cf1fcccc739cec42e2f

Name:           ant-antunit
Version:        1.4.1
Release:        17%{?dist}
Summary:        Unit Test Framework for Ant Tasks
License:        Apache-2.0
URL:            https://ant.apache.org/antlibs/antunit
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/ant/antlibs/antunit/source/apache-%{name}-%{version}-src.tar.bz2
Source1:        https://archive.apache.org/dist/ant/antlibs/antunit/source/apache-%{name}-%{version}-src.tar.bz2.asc
Source2:        https://archive.apache.org/dist/ant/KEYS

BuildRequires:  gnupg2
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.ant:ant-testutil)

%description
This library contains tasks that enables Ant task developers to test their tasks
with Ant and without JUnit.  It contains a few assertion tasks and an antunit
task that runs build files instead of test classes and is modelled after the
JUnit task.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n apache-%{name}-%{version}

find -type f '(' -iname '*.jar' -o -iname '*.class' ')' -print -delete

mv %{name}-%{version}.pom pom.xml

%pom_xpath_inject pom:project/pom:build '
    <resources>
      <resource>
        <directory>${project.basedir}/src/main</directory>
        <includes>
          <include>**/antlib.xml</include>
        </includes>
      </resource>
    </resources>'

# EatYourOwnDogFoodTest
sed -i 's|build/test-classes|target/test-classes|g' src/etc/testcases/antunit/java-io.xml

# AssertTest
sed -i 's|build/classes|target/classes|g' src/etc/testcases/assert.xml src/tests/junit/org/apache/ant/antunit/AssertTest.java

%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%check
# enable tests
%pom_xpath_set pom:maven.test.skip false

# compile tests
xmvn test-compile -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

# run tests
java -cp target/classes:target/test-classes:$(build-classpath junit hamcrest ant/ant-testutil ant ant/ant-launcher) \
       org.junit.runner.JUnitCore \
       $(find src/tests/junit/ -name '*.java' -printf '%%P\n' | cut -f 1 -d '.' | tr / .)

%install
%mvn_install

%files -f .mfiles
%license common/LICENSE NOTICE

%changelog
%autochangelog
