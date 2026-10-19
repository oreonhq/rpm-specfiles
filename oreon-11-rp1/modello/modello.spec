%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash a1c546949847eb2cb24b55f4083b51e2fd08e66cea7d9d56170700e719dc80ad
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
Name:           modello
Version:        2.8.1
Release:        1%{?dist}
Summary:        Modello Data Model toolkit
License:        MIT AND Apache-2.0 AND Plexus
URL:            https://codehaus-plexus.github.io/modello
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://repo1.maven.org/maven2/org/codehaus/%{name}/%{name}/%{version}/%{name}-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
%if %{with bootstrap}
%else
%endif
Obsoletes:      %{name}-javadoc < 2.8.1-23
# oreon:deps
BuildRequires:  javapackages-bootstrap
# /oreon:deps
%description
Modello is a Data Model toolkit in use by the Apache Maven Project.

Modello is a framework for code generation from a simple model.
Modello generates code from a simple model format based on a plugin
architecture, various types of code and descriptors can be generated
from the single model, including Java POJOs, XML
marshallers/unmarshallers, XSD and documentation.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
cp -p %{SOURCE1} LICENSE
# We don't generate site; don't pull extra dependencies.
%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep :plexus-xml modello-core
%pom_add_dep com.google.inject:guice modello-core

%pom_remove_dep :jackson-bom
%pom_disable_module modello-plugin-jackson modello-plugins
%pom_disable_module modello-plugin-jsonschema modello-plugins
%pom_remove_dep :modello-plugin-jackson modello-maven-plugin
%pom_remove_dep :modello-plugin-jsonschema modello-maven-plugin

%pom_disable_module modello-plugin-snakeyaml modello-plugins
%pom_remove_dep :modello-plugin-snakeyaml modello-maven-plugin

%pom_disable_module modello-test

%build

%mvn_build -j -f
%install
%mvn_install
%jpackage_script org.codehaus.modello.ModelloCli "" "" modello:sisu/org.eclipse.sisu.plexus:sisu/org.eclipse.sisu.inject:google-guice:aopalliance:atinject:plexus-containers/plexus-component-annotations:plexus/classworlds:plexus/utils:plexus/plexus-build-api:guava:velocity/velocity-engine-core %{name} true
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
