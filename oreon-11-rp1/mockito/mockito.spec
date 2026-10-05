%global source0_hash 7e2614a4fe1f463cc3b64907b18309b734971ca57a64036804aef77a7471e159
%global source3_hash 718074bfcba3592e3283a1cbcff2eb0163dddd742e2ed22d54a78eafedadc062
%global source4_hash 40b153c904cc535cc18cd8f679aad01d77b7278917fb70a163f573f5907d5e17

%{lua:
if macros.orbs_chain_plan == nil and macros._without_bootstrap == nil then
  local spec
  local cmd = io.open("/proc/self/cmdline", "rb")
  if cmd then
    local data = cmd:read("*a") or ""
    cmd:close()
    local cur = ""
    local function take(arg)
      if string.sub(arg, -5) == ".spec" then spec = arg end
    end
    for i = 1, #data do
      local c = string.sub(data, i, i)
      if string.byte(c) == 0 then
        take(cur)
        cur = ""
      else
        cur = cur .. c
      end
    end
    take(cur)
  end
  local function trim(s)
    local a, b = 1, #s
    while a <= b do
      local c = string.sub(s, a, a)
      if c ~= " " and string.byte(c) ~= 9 then break end
      a = a + 1
    end
    while b >= a do
      local c = string.sub(s, b, b)
      if c ~= " " and string.byte(c) ~= 9 then break end
      b = b - 1
    end
    return string.sub(s, a, b)
  end
  local function miss(dep)
    local p = io.popen("dnf -q install --assumeno '" .. dep .. "' 2>&1")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    if string.find(out, "nothing provides", 1, true) then return true end
    if string.find(out, "No match", 1, true) then return true end
    if string.find(out, "Failed to resolve", 1, true) then return true end
    if string.find(out, "Nothing to do", 1, true) then return false end
    if string.find(out, "Operation aborted", 1, true) then return false end
    if string.find(out, "already installed", 1, true) then return false end
    return true
  end
  if spec then
    local f = io.open(spec, "r")
    if f then
      local depth, in_else, armed = 0, false, false
      for line in f:lines() do
        local s = trim(line)
        if not armed then
          if string.sub(s, 1, 3) == "%%if" and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.sub(s, 1, 3) == "%%if" then
          depth = depth + 1
        elseif string.sub(s, 1, 6) == "%%endif" then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.sub(s, 1, 5) == "%%else" then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.sub(dep, 1, 1) ~= "%%" and miss(dep) then
            rpm.define("_with_bootstrap 1")
            break
          end
        end
      end
      f:close()
    end
  end
end
}
%bcond_with bootstrap

Name:           mockito
Version:        5.24.0
Release:        %autorelease
Summary:        Tasty mocking framework for unit tests in Java
License:        MIT
URL:            https://site.mockito.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/mockito/mockito/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        generate-tarball.sh
# A custom build script to allow building with maven instead of gradle
Source2:        aggregator.pom
# Maven central POMs for subprojects
Source3:        https://repo1.maven.org/maven2/org/mockito/mockito-core/%{version}/mockito-core-%{version}.pom
Source4:        https://repo1.maven.org/maven2/org/mockito/mockito-junit-jupiter/%{version}/mockito-junit-jupiter-%{version}.pom

# Mockito expects byte-buddy to have a shaded/bundled version of ASM, but
# we don't bundle in Fedora, so this patch makes mockito use ASM explicitly
Patch:          use-unbundled-asm.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-agent)
BuildRequires:  mvn(net.bytebuddy:byte-buddy-dep)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.opentest4j:opentest4j)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 5.8.0-16

%description
Mockito is a mocking framework that tastes really good. It lets you write
beautiful tests with clean & simple API. Mockito doesn't give you hangover
because the tests are very readable and they produce clean verification
errors.

%package junit-jupiter
Summary:        Mockito JUnit 5 support
Requires:       %{name} = %{version}-%{release}

%description junit-jupiter
Mockito JUnit 5 support.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source3_hash}" = "none" || { f="%{SOURCE3}"; test -f "$f" || { echo "oreon: missing Source3 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source3_hash}" || { echo "oreon: Source3 hash mismatch" >&2; exit 1; }; }
test "%{source4_hash}" = "none" || { f="%{SOURCE4}"; test -f "$f" || { echo "oreon: missing Source4 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source4_hash}" || { echo "oreon: Source4 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n mockito-%{version}

cp %{SOURCE2} aggregator.pom
cp %{SOURCE3} mockito-core/pom.xml
cp %{SOURCE4} mockito-extensions/mockito-junit-jupiter/pom.xml

# Disable failing test
# TODO check status: https://github.com/mockito/mockito/issues/2162
sed -i '/add_listeners_concurrently_sanity_check/i @org.junit.Ignore' mockito-core/src/test/java/org/mockitousage/debugging/StubbingLookupListenerCallbackTest.java

# Compatibility alias
%mvn_alias org.%{name}:%{name}-core org.%{name}:%{name}-all

%pom_add_dep junit:junit mockito-core
%pom_add_dep net.bytebuddy:byte-buddy-dep mockito-core
%pom_remove_dep org.objenesis:objenesis mockito-core
%pom_add_dep org.objenesis:objenesis mockito-core
%pom_add_dep org.opentest4j:opentest4j mockito-core

%pom_remove_dep org.junit.jupiter:junit-jupiter-api mockito-extensions/mockito-junit-jupiter
%pom_add_dep org.junit.jupiter:junit-jupiter-api mockito-extensions/mockito-junit-jupiter

mkdir -p mockito-core/src/main/resources/mockito-extensions
echo 'member-accessor-module' > mockito-core/src/main/resources/mockito-extensions/org.mockito.plugins.MemberAccessor
echo 'mock-maker-subclass' > mockito-core/src/main/resources/mockito-extensions/org.mockito.plugins.MockMaker

# see gradle/mockito-core/inline-mock.gradle
%pom_add_plugin org.apache.maven.plugins:maven-antrun-plugin mockito-core '
  <executions>
    <execution>
      <phase>process-classes</phase>
      <configuration>
        <target>
          <copy file="${project.build.outputDirectory}/org/mockito/internal/creation/bytebuddy/inject/MockMethodDispatcher.class"
            tofile="${project.build.outputDirectory}/org/mockito/internal/creation/bytebuddy/inject/MockMethodDispatcher.raw"/>
        </target>
      </configuration>
      <goals>
        <goal>run</goal>
      </goals>
    </execution>
  </executions>
'
%pom_add_plugin org.apache.maven.plugins:maven-jar-plugin mockito-core '
  <configuration>
    <excludes>
      <exclude>org/mockito/internal/creation/bytebuddy/inject/*.class</exclude>
    </excludes>
  </configuration>
'

%mvn_package :aggregator __noinstall

%build
%mvn_build -j -f -- -Dmaven.compiler.release=11 -Dproject.build.sourceEncoding=UTF-8 -f aggregator.pom

%mvn_package org.mockito:mockito-junit-jupiter junit-jupiter

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md doc/design-docs/custom-argument-matching.md

%files junit-jupiter -f .mfiles-junit-jupiter

%changelog
%autochangelog
