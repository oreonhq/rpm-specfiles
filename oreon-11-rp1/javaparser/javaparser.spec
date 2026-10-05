%global source0_hash 0a02ce2bc8256632beae9564cd52c79a9e6da4cd69f389381294f4855b645fe5

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
%if !0%{?rhel} && %{without bootstrap} || (0%{?oreon} >= 11)
%bcond_without bnd_maven_plugin
%else
%bcond_with bnd_maven_plugin
%endif

Name:           javaparser
Version:        3.28.2
Release:        %autorelease
Summary:        Java 1 to 13 Parser and Abstract Syntax Tree for Java
License:        LGPL-2.0-or-later OR Apache-2.0
URL:            https://javaparser.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/javaparser/javaparser/archive/%{name}-parent-%{version}.tar.gz#/javaparser-%{version}.tar.gz

Patch:          0001-Port-to-OpenJDK-21.patch

%if %{with bnd_maven_plugin}
BuildRequires:  mvn(biz.aQute.bnd:bnd-maven-plugin)
%endif
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.annotation:javax.annotation-api)
BuildRequires:  mvn(net.java.dev.javacc:javacc)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
BuildRequires:  mvn(org.codehaus.mojo:javacc-maven-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.26.3-4

%description
This package contains a Java 1 to 13 Parser with AST generation and
visitor support. The AST records the source code structure, javadoc
and comments. It is also possible to change the AST nodes or create new
ones to modify the source code.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n javaparser-javaparser-parent-%{version}

sed -i 's/\r//' readme.md

%pom_remove_dep -r :junit-bom

# Remove plugins unnecessary for RPM builds
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :central-publishing-maven-plugin

%if %{without bnd_maven_plugin}
%pom_remove_plugin :bnd-maven-plugin javaparser-core
mkdir -p javaparser-core/target/classes/META-INF/
touch javaparser-core/target/classes/META-INF/MANIFEST.MF
%endif

# Compatibility alias
%mvn_alias :javaparser-core com.google.code.javaparser:javaparser

# Fix javacc plugin name
sed -i \
  -e 's/ph-javacc-maven-plugin/javacc-maven-plugin/' \
  -e 's/com.helger.maven/org.codehaus.mojo/' \
  javaparser-core/pom.xml

# This plugin is not in Fedora, so use maven-resources-plugin to accomplish the same thing
%pom_remove_plugin :templating-maven-plugin javaparser-core
%pom_xpath_inject "pom:build" "
<resources>
  <resource>
    <directory>src/main/java-templates</directory>
    <filtering>true</filtering>
    <targetPath>\${basedir}/src/main/java</targetPath>
  </resource>
</resources>" javaparser-core

# Missing dep on jbehave for testing
%pom_disable_module javaparser-core-testing
%pom_disable_module javaparser-core-testing-bdd

# Don't build the symbol solver
%pom_disable_module javaparser-symbol-solver-core
#%pom_disable_module javaparser-symbol-solver-logic
#%pom_disable_module javaparser-symbol-solver-model
%pom_disable_module javaparser-symbol-solver-testing

# Only need to ship the core module
%pom_disable_module javaparser-core-generators
%pom_disable_module javaparser-core-metamodel-generator
%pom_disable_module javaparser-core-serialization

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc readme.md changelog.md
%license LICENSE LICENSE.APACHE LICENSE.GPL LICENSE.LGPL

%changelog
%autochangelog
