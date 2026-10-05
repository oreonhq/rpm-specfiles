%global source0_hash 1a87ca58aac92c7d5967806ea8a742707fe75c0136ab1276d2be28ee2f63b385

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
          if string.byte(s, 1) == 37 and string.byte(s, 2) == 105 and string.byte(s, 3) == 102 and string.find(s, "{with bootstrap}", 1, true) then
            armed = true
            depth = 1
          end
        elseif string.byte(s, 1) == 37 and string.byte(s, 2) == 105 and string.byte(s, 3) == 102 then
          depth = depth + 1
        elseif string.byte(s, 1) == 37 and string.byte(s, 2) == 101 and string.byte(s, 3) == 110 and string.byte(s, 4) == 100 and string.byte(s, 5) == 105 and string.byte(s, 6) == 102 then
          depth = depth - 1
          if depth == 0 then break end
        elseif depth == 1 and string.byte(s, 1) == 37 and string.byte(s, 2) == 101 and string.byte(s, 3) == 108 and string.byte(s, 4) == 115 and string.byte(s, 5) == 101 then
          in_else = true
        elseif in_else and depth == 1 and string.lower(string.sub(s, 1, 14)) == "buildrequires:" then
          local dep = trim(string.sub(s, 15))
          if dep ~= "" and string.byte(dep, 1) ~= 37 and miss(dep) then
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
%global upstream_version %(echo '%{version}' | tr '~' '-')

Name:           maven-surefire
Version:        3.6.0
Release:        %autorelease
Summary:        Test framework project
License:        Apache-2.0 AND CPL-1.0
URL:            https://maven.apache.org/surefire/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/apache/maven/surefire/surefire/%{version}/surefire-%{version}-source-release.zip
# Remove bundled binaries which cannot be easily verified for licensing
Source1:        https://www.eclipse.org/legal/cpl-v10.html


%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(commons-io:commons-io)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin) >= 3.6.4
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-shared-utils)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-parent:pom:)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.codehaus.plexus:plexus-component-metadata)
BuildRequires:  mvn(org.codehaus.plexus:plexus-java)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.fusesource.jansi:jansi)
BuildRequires:  mvn(org.junit.platform:junit-platform-launcher)
%endif
# PpidChecker relies on /usr/bin/ps to check process uptime
Requires:       procps-ng
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.6.0-19

%description
Surefire is a test framework project.

%package plugin
Summary:        Surefire plugin for maven
Requires:       (%{name}-provider-junit5 = %{version}-%{release} if junit5)

%description plugin
Maven surefire plugin for running tests via the surefire framework.

%package provider-junit5
Summary:        JUnit 5 provider for Maven Surefire

%description provider-junit5
JUnit 5 provider for Maven Surefire.

%package -n maven-failsafe-plugin
Summary:        Maven plugin for running integration tests

%description -n maven-failsafe-plugin
The Failsafe Plugin is designed to run integration tests while the
Surefire Plugins is designed to run unit. The name (failsafe) was
chosen both because it is a synonym of surefire and because it implies
that when it fails, it does so in a safe way.

If you use the Surefire Plugin for running tests, then when you have a
test failure, the build will stop at the integration-test phase and
your integration test environment will not have been torn down
correctly.

The Failsafe Plugin is used during the integration-test and verify
phases of the build lifecycle to execute the integration tests of an
application. The Failsafe Plugin will not fail the build during the
integration-test phase thus enabling the post-integration-test phase
to execute.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n surefire-%{upstream_version}
%autopatch -p1
cp -p %{SOURCE1} .


# Disable strict doclint
sed -i /-Xdoclint:all/d pom.xml

%pom_disable_module maven-surefire-report-plugin
%pom_disable_module surefire-report-parser
%pom_disable_module surefire-shadefire

%pom_remove_dep org.junit:junit-bom
%pom_remove_dep org.mockito:mockito-bom

%pom_remove_dep -r org.apache.maven.surefire:surefire-shadefire

# Help plugin is needed only to evaluate effective Maven settings.
# For building RPM package default settings will suffice.
%pom_remove_plugin :maven-help-plugin surefire-its

# QA plugin useful only for upstream
%pom_remove_plugin -r :jacoco-maven-plugin
# Not wanted
%pom_remove_plugin -r :maven-shade-plugin

find -name *.java -exec sed -i -e s/org.apache.maven.surefire.shared.utils/org.apache.maven.shared.utils/ -e s/org.apache.maven.surefire.shared.io/org.apache.commons.io/ -e s/org.apache.maven.surefire.shared.lang3/org.apache.commons.lang3/ -e s/org.apache.maven.surefire.shared.compress/org.apache.commons.compress/ {} \;
%pom_add_dep org.apache.maven.shared:maven-shared-utils
%pom_add_dep commons-io:commons-io
%pom_add_dep org.apache.commons:commons-lang3
%pom_add_dep org.apache.commons:commons-compress

# Not in Fedora
%pom_remove_plugin -r :animal-sniffer-maven-plugin
# Complains
%pom_remove_plugin -r :apache-rat-plugin
# We don't need site-source
%pom_remove_plugin :maven-assembly-plugin maven-surefire-plugin
%pom_remove_dep -r ::::site-source

%build
%mvn_package ":*{surefire-plugin}*" @1
%mvn_package ":*junit-platform*" junit5
%mvn_package ":*{failsafe-plugin}*" @1
%mvn_package ":*tests*" __noinstall
# tests turned off because they need jmock
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE NOTICE cpl-v10.html

%files plugin -f .mfiles-surefire-plugin

%files provider-junit5 -f .mfiles-junit5

%files -n maven-failsafe-plugin -f .mfiles-failsafe-plugin

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2.2-1
- Import
