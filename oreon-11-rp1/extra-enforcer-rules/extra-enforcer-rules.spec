%global source0_hash 215cbb2ec3e9b41c5f5d817be4553c94cc3014bed257dcdf9d969014530d92b4

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
Name:           extra-enforcer-rules
Version:        1.12.1
Release:        %autorelease
Summary:        Extra rules for maven-enforcer-plugin
License:        Apache-2.0
URL:            https://github.com/mojohaus/extra-enforcer-rules
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://repo1.maven.org/maven2/org/codehaus/mojo/extra-enforcer-rules/%{version}/extra-enforcer-rules-%{version}-source-release.zip

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.enforcer:enforcer-api)
BuildRequires:  mvn(org.apache.maven.shared:maven-common-artifact-filters)
BuildRequires:  mvn(org.apache.maven.shared:maven-dependency-tree)
BuildRequires:  mvn(org.apache.maven:maven-core)
BuildRequires:  mvn(org.codehaus.mojo:mojo-parent:pom:)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.8.0-11

%description
Apache's Maven Enforcer Plugin is used to apply and enforce rules on Maven
projects. The Enforcer plugin ships with a set of standard rules. This project
provides extra rules which are not part of the standard rule set.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

# Integration tests fetch upstream poms
%pom_remove_plugin :maven-invoker-plugin

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt
%doc README.md

%changelog
%autochangelog
