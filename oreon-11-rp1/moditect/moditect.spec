%global source0_hash e8623c04c9a018ba8026f7ba55c86902315c501c5ec7b8fa27f66fdd54575021

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
Name:           moditect
Version:        1.3.0.Final
Release:        %autorelease
Summary:        Tooling for the Java Module System
License:        Apache-2.0
URL:            https://github.com/moditect/moditect
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/moditect/moditect/archive/refs/tags/%{version}.tar.gz#/moditect-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.beust:jcommander)
BuildRequires:  mvn(com.github.javaparser:javaparser-core)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugin-tools:maven-plugin-annotations)
BuildRequires:  mvn(org.apache.maven.plugins:maven-plugin-plugin)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.apache.maven:maven-plugin-api)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.eclipse.aether:aether-util)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.3.0.Final-12

%description
The ModiTect project aims at providing productivity tools for working with the
Java module system ("Jigsaw"). Currently the following tasks are supported:
* Generating module-info.java descriptors for given artifacts (Maven
  dependencies or local JAR files)
* Adding module descriptors to your project's JAR as well as existing JAR files
  (dependencies)
* Creating module runtime images

Compared to authoring module descriptors by hand, using ModiTect saves you work
by defining dependence clauses based on your project's dependencies, describing
exported and opened packages with patterns (instead of listing all packages
separately), auto-detecting service usages and more. You also can use ModiTect
to add a module descriptor to your project JAR while staying on Java 8 with your
own build.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%pom_remove_parent parent
%pom_xpath_inject 'pom:project' '<groupId>org.moditect</groupId>' parent

# Missing dependencies in each submodule of integration tests
%pom_disable_module integrationtest

%pom_remove_plugin com.mycila:license-maven-plugin parent
%pom_remove_plugin -r :maven-shade-plugin

%pom_remove_dep -r com.google.testing.compile:compile-testing
rm core/src/test/java/org/moditect/test/AddModuleInfoTest.java
# Test fails with early-access versions of Java
rm core/src/test/java/org/moditect/internal/parser/JavaVersionHelperTest.java

%build
%mvn_build -j -- -Dproject.build.sourceEncoding=UTF-8

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
