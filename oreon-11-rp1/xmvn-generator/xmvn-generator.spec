%global source0_hash none

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
%bcond bootstrap 0

Name:           xmvn-generator
Version:        2.1.1
Release:        %autorelease
Summary:        RPM dependency generator for Java
License:        Apache-2.0
URL:            https://github.com/fedora-java/xmvn-generator
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source:        https://github.com/fedora-java/xmvn-generator/archive/refs/tags/%{version}.tar.gz#/xmvn-generator-%{version}.tar.gz

# https://github.com/fedora-java/xmvn-generator/pull/37
Patch:          0001-Add-commons-lang3-to-generator-classpath.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(io.kojan:dola-bsx-api)
BuildRequires:  mvn(org.apache.commons:commons-compress)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
Requires:       dola-bsx
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0.2-9

%description
XMvn Generator is a dependency generator for RPM Package Manager
written in Java and Lua.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
%mvn_file : %{name}

%build
%mvn_build -j -- -P\!quality

%install
%mvn_install
install -D -p -m 644 src/main/lua/xmvn-generator.lua %{buildroot}%{_rpmluadir}/xmvn-generator.lua
install -D -p -m 644 src/main/rpm/macros.xmvngen %{buildroot}%{_rpmmacrodir}/macros.xmvngen
install -D -p -m 644 src/main/rpm/macros.xmvngenhook %{buildroot}%{_sysconfdir}/rpm/macros.xmvngenhook
install -D -p -m 644 src/main/rpm/xmvngen.attr %{buildroot}%{_fileattrsdir}/xmvngen.attr
install -D -p -m 644 src/main/conf/xmvn-generator.conf %{buildroot}%{_javaconfdir}/dola/classworlds/90-xmvn-generator.conf

%files -f .mfiles
%{_rpmluadir}/*
%{_rpmmacrodir}/*
%{_fileattrsdir}/*
%{_sysconfdir}/rpm/*
%{_javaconfdir}/dola/classworlds/90-xmvn-generator.conf
%license LICENSE NOTICE
%doc README.md

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.1-1
- Import
