%global source0_hash 6c85f80a054e91b4bc59fc6fc7e26f95645699ecef913ec3489a260a8e82324a

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

Name:           plexus-classworlds
Version:        2.12.1
Release:        %autorelease
Summary:        Plexus Classworlds Classloader Framework
License:        Apache-2.0 AND Plexus
URL:            https://github.com/codehaus-plexus/plexus-classworlds
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/plexus-classworlds/archive/refs/tags/plexus-classworlds-2.8.0.tar.gz#/plexus-classworlds-2.8.0.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.12.1-12

%description
Classworlds is a framework for container developers who require complex
manipulation of Java's ClassLoaders. Java's native ClassLoader mechanisms and
classes can cause much headache and confusion for certain types of application
developers. Projects which involve dynamic loading of components or otherwise
represent a 'container' can benefit from the classloading control provided by
classworlds.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n plexus-classworlds-plexus-classworlds-2.8.0
%mvn_file : %{name} plexus/classworlds
%mvn_alias : classworlds:classworlds

%pom_remove_plugin :maven-dependency-plugin

# These tests depend on artifacts that are not packaged
sed -i /testConfigure_Valid/s/./@org.junit.jupiter.api.Disabled/ src/test/java/org/codehaus/plexus/classworlds/launcher/ConfiguratorTest.java
sed -i /testConfigure_Optionally_Existent/s/./@org.junit.jupiter.api.Disabled/ src/test/java/org/codehaus/plexus/classworlds/launcher/ConfiguratorTest.java

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt LICENSE-Codehaus.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.8.0-1
- Import
