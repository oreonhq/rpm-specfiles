%global source0_hash 0b3032e6d66bfdb166c956c6f9bdf661010be652f67900099f8ffd83ae07a8c2
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
Name:           sisu
Epoch:          1
Version:        1.1.0
Release:        1%{?dist}
Summary:        Eclipse dependency injection framework
License:        EPL-1.0 AND BSD-3-Clause
URL:            https://eclipse.org/sisu/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/eclipse-sisu/sisu-project/archive/refs/tags/milestones/0.9.0.M3.tar.gz#/sisu-%{version}.tar.gz
Patch:          0001-Add-ASM-support-for-Java-24-and-25.patch
%if %{with bootstrap}
%else
%endif
Obsoletes:      %{name}-javadoc < 1:1.1.0-14
Provides:       %{name}-inject = %{epoch}:%{version}-%{release}
Provides:       %{name}-plexus = %{epoch}:%{version}-%{release}
Provides:       bundled(objectweb-asm)
# oreon:deps
BuildRequires:  javapackages-bootstrap
# /oreon:deps
%description
Java dependency injection framework with backward support for plexus and bean
style dependency injection.

%package maven-plugin
Summary:        Sisu plugin for Apache Maven
Obsoletes:      sisu-mojos < 1:1.1.0
%description maven-plugin
The Sisu Plugin for Maven provides mojos to generate
META-INF/sisu/javax.inject.Named index files for the Sisu container.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n sisu-project-milestones-0.9.0.M3
%autosetup -p1 -n sisu-project-milestones-0.9.0.M3

%pom_disable_module org.eclipse.sisu.inject.extender
%pom_disable_module org.eclipse.sisu.plexus.extender

%pom_remove_dep :junit-bom
%pom_change_dep :plexus-utils :::provided org.eclipse.sisu.plexus
%pom_change_dep :plexus-xml :::provided org.eclipse.sisu.plexus

%pom_remove_plugin -r :bnd-maven-plugin
%pom_remove_plugin -r :maven-jar-plugin
%pom_remove_plugin -r :jacoco-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :maven-dependency-plugin
%pom_remove_plugin -r :maven-clean-plugin

%mvn_package :sisu-maven-plugin maven-plugin
%mvn_alias :org.eclipse.sisu.inject :::no_asm:
%mvn_alias :org.eclipse.sisu.plexus org.sonatype.sisu:sisu-inject-plexus org.codehaus.plexus:plexus-container-default

%build

%mvn_build -j -f
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n sisu-maven-plugin -f %{oreon_filedir}/sisu-maven-plugin.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.9.0~M3-1
- Import
