%global source0_hash e091f16cb6096d3556e6dc33cb58d0f58c5f355f6ff1f35bfbddfc1e97d35cfd

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

Name:           dola
Version:        1.3.2
Release:        %autorelease
Summary:        Declarative system for Java RPM packaging
License:        Apache-2.0
URL:            https://github.com/mizdebsk/dola
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:         https://github.com/mizdebsk/dola/releases/download/%{version}/dola-%{version}.tar.zst

# https://github.com/mizdebsk/dola/pull/30
Patch:          0001-Update-to-XMvn-5.1.0.patch
# https://github.com/mizdebsk/dola/pull/32
Patch:          0002-Ensure-os_install_post-commands-are-NL-terminated.patch
# https://github.com/mizdebsk/dola/pull/33
Patch:          0003-Switch-to-OpenJDK-for-runtime.patch
# https://github.com/mizdebsk/dola/pull/42
Patch:          0004-Add-commons-lang3-to-dola-generator-classpath.patch
# https://github.com/mizdebsk/dola/pull/53
Patch:          0005-Allow-override-of-classworlds-configuration-dir.patch

Requires:       %{name}-bsx = %{version}-%{release}
Requires:       %{name}-generator = %{version}-%{release}
Requires:       dola-gleaner
Requires:       dola-transformer
Requires:       xmvn5-minimal
Requires:       xmvn5-mojo
Requires:       xmvn5-tools

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
BuildRequires:  lujavrite
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.codehaus.plexus:plexus-classworlds)
%endif

%description
Dola is a modern, declarative system for RPM packaging of Maven-based
Java projects.  It enables package maintainers to entirely avoid
writing `%%prep`, `%%build`, or `%%install` scriptlets in RPM spec files.
Instead, all build configuration is expressed using BuildOption tags
(introduced in RPM 4.20), resulting in cleaner, more maintainable spec
files.

%package bsx
Summary:        Runtime layer for running Dola inside RPM builds
Requires:       java-25-openjdk-headless
Requires:       lujavrite
Requires:       rpm-build

%description bsx
Dola BSX is a minimal execution layer that bridges the gap between
rpmbuild and high-level packaging logic implemented in Java via Dola.
Acting as a microkernel, BSX exposes a structured API for I/O, macro
evaluation, logging, and event handling.

%package generator
Summary:        RPM dependency generator for Java
Requires:       %{name}-bsx = %{version}-%{release}

%description generator
Dola Generator is a dependency generator for RPM Package Manager
written in Java and Lua, that uses LuJavRite library to call Java code
from Lua.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%pom_remove_parent
%if %{with bootstrap}
%pom_xpath_inject pom:project "<groupId>io.kojan</groupId>"
%mvn_package :dola-bsx dola-bsx
%mvn_package :dola-bsx-api dola-bsx-api
%mvn_package :dola-dbs dola-dbs
%mvn_package :dola-parent dola-parent
%mvn_package :dola-generator dola-generator
%endif

%build
%mvn_build -j -- -Dmaven.compiler.release=21

%install
%mvn_install
# BSX
install -D -p -m 644 dola-bsx/src/main/lua/dola-bsx.lua %{buildroot}%{_rpmluadir}/dola-bsx.lua
install -D -p -m 644 dola-bsx/src/main/rpm/macros.dola-bsx %{buildroot}%{_rpmmacrodir}/macros.dola-bsx
install -D -p -m 644 dola-bsx/src/main/conf/dola-bsx.conf %{buildroot}%{_javaconfdir}/dola/classworlds/00-dola-bsx.conf
install -D -p -m 644 dola-bsx-api/src/main/conf/dola-bsx-api.conf %{buildroot}%{_javaconfdir}/dola/classworlds/01-dola-bsx-api.conf
# DBS
install -D -p -m 644 dola-dbs/src/main/lua/dola-dbs.lua %{buildroot}%{_rpmluadir}/dola-dbs.lua
install -D -p -m 644 dola-dbs/src/main/rpm/macros.dola-dbs %{buildroot}%{_rpmmacrodir}/macros.zzz-dola-dbs
install -D -p -m 644 dola-dbs/src/main/conf/dola-dbs.conf %{buildroot}%{_javaconfdir}/dola/classworlds/04-dola-dbs.conf
# Generator
install -D -p -m 644 dola-generator/src/main/lua/dola-generator.lua %{buildroot}%{_rpmluadir}/dola-generator.lua
install -D -p -m 644 dola-generator/src/main/rpm/macros.dola-generator %{buildroot}%{_rpmmacrodir}/macros.dola-generator
install -D -p -m 644 dola-generator/src/main/rpm/macros.dola-generator-etc %{buildroot}%{_sysconfdir}/rpm/macros.dola-generator-etc
install -D -p -m 644 dola-generator/src/main/rpm/dolagen.attr %{buildroot}%{_fileattrsdir}/dolagen.attr
install -D -p -m 644 dola-generator/src/main/conf/dola-generator.conf %{buildroot}%{_javaconfdir}/dola/classworlds/03-dola-generator.conf

%files bsx -f .mfiles-dola-bsx -f .mfiles-dola-bsx-api
%{_rpmluadir}/dola-bsx.lua
%{_rpmmacrodir}/macros.dola-bsx
%dir %{_javaconfdir}/dola
%dir %{_javaconfdir}/dola/classworlds
%{_javaconfdir}/dola/classworlds/00-dola-bsx.conf
%{_javaconfdir}/dola/classworlds/01-dola-bsx-api.conf
%license LICENSE NOTICE

%files -f .mfiles-dola-dbs -f .mfiles-dola-parent
%{_rpmluadir}/dola-dbs.lua
%{_rpmmacrodir}/macros.zzz-dola-dbs
%{_javaconfdir}/dola/classworlds/04-dola-dbs.conf
%doc README.md

%files generator -f .mfiles-dola-generator
%{_rpmluadir}/dola-generator.lua
%{_rpmmacrodir}/macros.dola-generator
%{_sysconfdir}/rpm/macros.dola-generator-etc
%{_fileattrsdir}/dolagen.attr
%{_javaconfdir}/dola/classworlds/03-dola-generator.conf

%changelog
%autochangelog
