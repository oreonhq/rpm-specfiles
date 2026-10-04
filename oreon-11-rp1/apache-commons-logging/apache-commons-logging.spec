%global source0_hash 3596de02a6b4d4f11b4353f4db7964cb248fdc18252a4636eb1496149a5fcd9e

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
Name:           apache-commons-logging
Version:        1.4.0
Release:        %autorelease
Summary:        Apache Commons Logging
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-logging/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://www.apache.org/dist/commons/logging/source/commons-logging-%{version}-src.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.servlet:javax.servlet-api)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-1.2-api)
BuildRequires:  mvn(org.apache.logging.log4j:log4j-api)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-failsafe-plugin)
BuildRequires:  mvn(org.moditect:moditect-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.3.4-8

%description
The commons-logging package provides a simple, component oriented
interface (org.apache.commons.logging.Log) together with wrappers for
logging systems. The user can choose at runtime which system they want
to use. In addition, a small number of basic implementations are
provided to allow users to use the package standalone.
commons-logging was heavily influenced by Avalon's Logkit and Log4J. The
commons-logging abstraction is meant to minimize the differences between
the two, and to allow a developer to not tie himself to a particular
logging implementation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n commons-logging-%{version}-src

%pom_remove_dep :avalon-framework
%pom_remove_dep :logkit
rm src/main/java/org/apache/commons/logging/impl/AvalonLogger.java
rm src/main/java/org/apache/commons/logging/impl/LogKitLogger.java
rm -r src/test/java/org/apache/commons/logging/{avalon,logkit}
rm src/test/java/org/apache/commons/logging/pathable/{Parent,Child}FirstTestCase.java

# Avoid hard-coded versions in OSGi metadata
%pom_xpath_set "pom:properties/pom:commons.osgi.import" '*;resolution:=optional'

%pom_remove_plugin :maven-scm-publish-plugin
%pom_remove_plugin :maven-enforcer-plugin

sed -i 's/\r//' RELEASE-NOTES.txt LICENSE.txt NOTICE.txt

# for compatibility reasons
%mvn_file ":commons-logging{*}" "commons-logging@1" "%{name}@1"
%mvn_alias ":commons-logging{*}" "org.apache.commons:commons-logging@1" "apache:commons-logging@1"

%mvn_package ":::{*}:"

# Remove log4j12 tests
rm -rf src/test/java/org/apache/commons/logging/log4j/log4j12

%build
# missing test dependencies
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc PROPOSAL.html RELEASE-NOTES.txt

%changelog
%autochangelog
