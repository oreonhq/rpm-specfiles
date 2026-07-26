%global source0_hash 1f6ac68ea7e3e946a221b49a99986aa650a00392ccd5f188158d7c88b1d5a206

%global scm_release Rhino%(v=%{version}; echo ${v//\./_})_Release
%global test262_commit f94fc660cc3c59b1f2f9f122fc4d44b4434b935c
%global test262_shortcommit %(c=%{test262_commit}; echo ${c:0:7})

Name:           rhino
Version:        1.7.14
Release:        17%{?dist}
Summary:        Rhino

# rhino itself is MPLv2.0 but use other codes, breakdown:
# BSD: toolsrc/org/mozilla/javascript/tools/debugger/treetable/*
#      src/org/mozilla/javascript/v8dtoa/* except FastDtoaBuilder.java
# Automatically converted from old format: MPLv2.0 and BSD - review is highly recommended.
License:        MPL-2.0 AND LicenseRef-Callaway-BSD
URL:            https://mozilla.github.io/rhino
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
ExcludeArch:    %{ix86}

Source0:        %{url}/archive/%{scm_release}/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/mozilla/%{name}/%{version}/%{name}-%{version}.pom
Source2:        https://repo1.maven.org/maven2/org/mozilla/%{name}-engine/%{version}/%{name}-engine-%{version}.pom
Source3:        https://repo1.maven.org/maven2/org/mozilla/%{name}-runtime/%{version}/%{name}-runtime-%{version}.pom
# required for tests
Source4:        https://github.com/tc39/test262/archive/%{test262_shortcommit}/test262-%{test262_shortcommit}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(jakarta.xml.soap:jakarta.xml.soap-api)
Requires:       javapackages-tools

%description
Rhino is an open-source implementation of JavaScript written entirely in Java.
It is typically embedded into Java applications to provide scripting to end
users. Full jar including tools, excluding the JSR-223 Script Engine wrapper.

%package -n %{name}-engine
Summary:        Rhino Engine
%description -n %{name}-engine
Rhino Javascript JSR-223 Script Engine wrapper.

%package -n %{name}-runtime
Summary:        Rhino Runtime
%description -n %{name}-runtime
Rhino JavaScript runtime jar, excludes tools & JSR-223 Script Engine wrapper.

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{scm_release}

# Uncomment to include test262
tar --extract --strip-component=1 --file=%{SOURCE4} --directory=test262

# jar in tests is used by requireJarTest
find -type f '(' -name '*.jar' -o -name '*.class' ')' -not -path './testsrc/*' -print -delete

# requires netscape.security
rm -rf testsrc/tests/src

mkdir %{name}
mkdir %{name}-engine
mkdir %{name}-runtime

# use simplest pom as parent pom
cp %{SOURCE1} pom.xml
cp %{SOURCE1} %{name}/pom.xml
cp %{SOURCE2} %{name}-engine/pom.xml
cp %{SOURCE3} %{name}-runtime/pom.xml

%pom_add_dep junit:junit:4.13.2:test %{name}
%pom_add_dep org.yaml:snakeyaml:1.28:test %{name}
%pom_add_dep jakarta.xml.soap:jakarta.xml.soap-api:1.4.0:test %{name}

# needed by surefire plugin
%pom_add_dep org.apache.commons:commons-lang3:3.8.1:test %{name}
%pom_add_dep commons-io:commons-io:2.6:test %{name}

%pom_xpath_set pom:artifactId %{name}-parent
%pom_xpath_set pom:name %{name}-parent
%pom_xpath_inject pom:project '<packaging>pom</packaging>'

%pom_remove_parent . \
    %{name} \
    %{name}-engine \
    %{name}-runtime

%pom_xpath_inject pom:project '
    <modules>
      <module>%{name}</module>
      <module>%{name}-engine</module>
      <module>%{name}-runtime</module>
    </modules>'

%pom_add_plugin org.codehaus.mojo:build-helper-maven-plugin \
    %{name} '
    <executions>
      <execution>
        <id>add-source</id>
        <goals>
          <goal>add-source</goal>
        </goals>
        <configuration>
          <sources>
            <source>${project.basedir}/../src</source>
            <source>${project.basedir}/../toolsrc</source>
            <source>${project.basedir}/../xmlimplsrc</source>
          </sources>
        </configuration>
      </execution>
      <execution>
        <id>add-test-source</id>
        <goals>
          <goal>add-test-source</goal>
        </goals>
        <configuration>
          <sources>
            <source>${project.basedir}/../examples</source>
            <source>${project.basedir}/../testsrc</source>
          </sources>
        </configuration>
      </execution>
    </executions>'

%pom_xpath_inject pom:project/pom:build '
    <resources>
      <resource>
        <directory>${project.basedir}/../src</directory>
        <excludes>
          <exclude>**/*.java</exclude>
          <exclude>build.xml</exclude>
          <exclude>manifest</exclude>
        </excludes>
      </resource>
      <resource>
        <directory>${project.basedir}/../toolsrc</directory>
        <excludes>
          <exclude>**/*.java</exclude>
          <exclude>build.xml</exclude>
          <exclude>manifest</exclude>
        </excludes>
      </resource>
    </resources>
    <testResources>
      <testResource>
        <directory>${project.basedir}/../testsrc</directory>
        <excludes>
          <exclude>**/*.java</exclude>
        </excludes>
      </testResource>
    </testResources>' \
      %{name}

%pom_add_plugin :maven-surefire-plugin \
    %{name} '
    <configuration>
      <argLine>
        -Xss1280k
        -Dfile.encoding=UTF-8
        --add-opens java.desktop/javax.swing.table=ALL-UNNAMED
      </argLine>
      <excludes>
        <exclude>**/benchmarks/**</exclude>
      </excludes>
      <forkCount>64</forkCount>
      <reuseForks>false</reuseForks>
      <systemPropertyVariables>
        <java.awt.headless>true</java.awt.headless>
        <mozilla.js.tests>testsrc/tests</mozilla.js.tests>
        <mozilla.js.tests.timeout>60000</mozilla.js.tests.timeout>
        <user.language>en</user.language>
        <user.country>US</user.country>
        <user.timezone>America/Los_Angeles</user.timezone>
        <TEST_OPTLEVEL>-1</TEST_OPTLEVEL>
        <TEST_262_OPTLEVEL>-1</TEST_262_OPTLEVEL>
        <test262properties>testsrc/test262.properties</test262properties>
      </systemPropertyVariables>
      <workingDirectory>${project.basedir}/../</workingDirectory>
    </configuration>'

%pom_add_plugin :maven-resources-plugin \
    %{name}-engine \
    %{name}-runtime '
    <executions>
      <execution>
        <id>copy-resources</id>
        <phase>generate-sources</phase>
        <goals>
          <goal>copy-resources</goal>
        </goals>
        <configuration>
          <outputDirectory>${project.build.outputDirectory}</outputDirectory>
          <resources>
            <resource>
              <directory>${project.basedir}/../%{name}/target/classes</directory>
            </resource>
          </resources>
        </configuration>
      </execution>
    </executions>'

%pom_add_plugin :maven-jar-plugin \
    %{name} '
    <configuration>
      <archive>
        <manifestEntries>
          <Main-Class>org.mozilla.javascript.tools.shell.Main</Main-Class>
          <Implementation-Title>Mozilla Rhino</Implementation-Title>
          <Implementation-Version>${project.version}</Implementation-Version>
          <Automatic-Module-Name>org.mozilla.rhino</Automatic-Module-Name>
          <Bundle-SymbolicName>org.mozilla.rhino</Bundle-SymbolicName>
        </manifestEntries>
      </archive>
      <excludes>
        <exclude>META-INF/services/**</exclude>
        <exclude>org/mozilla/javascript/engine/**</exclude>
      </excludes>
    </configuration>'

%pom_add_plugin :maven-jar-plugin \
    %{name}-engine '
    <configuration>
      <archive>
        <manifestEntries>
          <Automatic-Module-Name>org.mozilla.rhino.engine</Automatic-Module-Name>
        </manifestEntries>
      </archive>
      <includes>
        <include>META-INF/services/**</include>
        <include>org/mozilla/javascript/engine/**</include>
      </includes>
    </configuration>'

%pom_add_plugin :maven-jar-plugin \
    %{name}-runtime '
    <configuration>
      <archive>
        <manifestEntries>
          <Bundle-SymbolicName>org.mozilla.rhino-runtime</Bundle-SymbolicName>
        </manifestEntries>
      </archive>
      <excludes>
        <exclude>META-INF/services/**</exclude>
        <exclude>org/mozilla/javascript/engine/**</exclude>
        <exclude>org/mozilla/javascript/tools/**</exclude>
      </excludes>
    </configuration>'

%mvn_package :%{name}-parent \
    __noinstall

# Compatibility
%mvn_alias :%{name} rhino:js
%mvn_file :%{name} rhino/%{name} %{name}

%build
# Ignore test
%mvn_build -f -s -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8

%install
%mvn_install

%jpackage_script org.mozilla.javascript.tools.shell.Main "" "" rhino rhino true
%jpackage_script org.mozilla.javascript.tools.debugger.Main "" "" rhino rhino-debugger true
%jpackage_script org.mozilla.javascript.tools.jsc.Main "" "" rhino rhino-jsc true

mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 man/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files -n %{name} -f .mfiles-%{name}
%{_bindir}/%{name}
%{_bindir}/%{name}-debugger
%{_bindir}/%{name}-jsc
%{_mandir}/man1/%{name}.1*
%license LICENSE.txt NOTICE.txt NOTICE-tools.txt
%doc README.md CODE_OF_CONDUCT.md RELEASE-NOTES.md

%files -n %{name}-engine -f .mfiles-%{name}-engine
%license LICENSE.txt
%doc README.md CODE_OF_CONDUCT.md RELEASE-NOTES.md

%files -n %{name}-runtime -f .mfiles-%{name}-runtime
%license LICENSE.txt NOTICE.txt
%doc README.md CODE_OF_CONDUCT.md RELEASE-NOTES.md

%changelog
%autochangelog
