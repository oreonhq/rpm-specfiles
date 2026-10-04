%global source0_hash 323603483db8574eeda542c19e8257562e185be31d7f3454b4770d0bd2fca8b6

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
    local p = io.popen("dnf -q repoquery --latest-limit 1 --whatprovides '" .. dep .. "' 2>/dev/null")
    if not p then return true end
    local out = p:read("*a") or ""
    p:close()
    local i = 1
    while i <= #out do
      local b = string.byte(out, i)
      if b ~= 32 and b ~= 9 and b ~= 10 and b ~= 13 then return false end
      i = i + 1
    end
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

Name:           easymock
Version:        5.7.0
Release:        %autorelease
Summary:        Easy mock objects
License:        Apache-2.0
URL:            https://www.easymock.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/easymock/%{name}/archive/refs/tags/%{name}-%{version}.tar.gz#/easymock-%{version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
# Forwarded: https://github.com/easymock/easymock/pull/807

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(net.bytebuddy:byte-buddy)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-junit-platform)
BuildRequires:  mvn(org.apache.maven.surefire:surefire-testng)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.junit.vintage:junit-vintage-engine)
BuildRequires:  mvn(org.objenesis:objenesis)
BuildRequires:  mvn(org.ow2.asm:asm)
BuildRequires:  mvn(org.testng:testng)
%endif
%if %{without bootstrap}
# xmvn-builddep misses this:
BuildRequires:  mvn(org.apache:apache-jar-resource-bundle)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.3-23
Provides:       %{name}3 = %{version}-%{release}

%description
EasyMock provides Mock Objects for interfaces in JUnit tests by generating
them on the fly using Java's proxy mechanism. Due to EasyMock's unique style
of recording expectations, most refactorings will not affect the Mock Objects.
So EasyMock is a perfect fit for Test-Driven Development.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{name}-%{version}


%pom_remove_plugin -r :maven-javadoc-plugin
%pom_remove_plugin -r :maven-source-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin
%pom_remove_plugin :animal-sniffer-maven-plugin core

%pom_remove_plugin :maven-gpg-plugin test-testng
%pom_remove_plugin :maven-gpg-plugin test-java8
%pom_remove_plugin :maven-gpg-plugin test-junit5

# remove android support
rm core/src/main/java/org/easymock/internal/Android*.java
rm core/src/test/java/org/easymock/tests2/ClassExtensionHelperTest.java
%pom_disable_module test-android
%pom_remove_dep :dexmaker core

# unbundle asm and cglib
%pom_disable_module test-nodeps

# missing test deps
%pom_disable_module test-integration
%pom_disable_module test-osgi

# remove some warning caused by unavailable plugin
%pom_remove_plugin org.codehaus.mojo:versions-maven-plugin

# For compatibility reasons
%mvn_file ":easymock{*}" easymock@1 easymock3@1

# ssh not needed during our builds
%pom_xpath_remove pom:extensions

# Force Surefire to run tests with JUnit, not with TestNG
# (easymock 5.7 core/pom.xml no longer declares surefire, so add it with our config)
%pom_add_plugin :maven-surefire-plugin core "<configuration>
    <testNGArtifactName>none:none</testNGArtifactName>
    <argLine>--add-opens=java.base/java.lang=ALL-UNNAMED --add-opens=java.base/java.io=ALL-UNNAMED</argLine></configuration>"
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" \
    "<argLine>--add-opens=java.base/java.lang=ALL-UNNAMED</argLine>" test-testng
%pom_add_plugin :maven-surefire-plugin test-java8 "<configuration>
    <argLine>--add-opens=java.base/java.lang=ALL-UNNAMED</argLine></configuration>"
%pom_add_plugin :maven-surefire-plugin test-junit5 "<configuration>
    <argLine>--add-opens=java.base/java.lang=ALL-UNNAMED</argLine></configuration>"

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license core/LICENSE.txt

%changelog
%autochangelog
