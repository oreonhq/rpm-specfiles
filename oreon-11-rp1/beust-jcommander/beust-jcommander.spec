%global source0_hash 4adddcef38265d5339ec28a0e34fc2a7c2f59cf7d6fb988b4e56380c0de0f96b

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

Name:           beust-jcommander
Version:        1.82
Release:        %autorelease
Summary:        Java framework for parsing command line parameters
License:        Apache-2.0
URL:            https://jcommander.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/cbeust/jcommander/archive/dcf154b6d40dd3865e317de7250b7019044543a9.tar.gz#/beust-jcommander-1.82.tar.gz
Source1:        https://repo1.maven.org/maven2/com/beust/jcommander/%{version}/jcommander-%{version}.pom
# Cleaned up bundled jars whose licensing cannot be easily verified
Patch:          0001-ParseValues-NullPointerException-patch.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.testng:testng)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.82-23

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n jcommander-dcf154b6d40dd3865e317de7250b7019044543a9
chmod -x license.txt

cp -p %SOURCE1 pom.xml
%pom_xpath_set "pom:project/pom:version" "%{version}"

# maven-surefire-plugin requires explicit version >= 4.7
%pom_add_dep org.testng:testng:4.7:test

%mvn_file : %{name}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license license.txt notice.md
%doc README.markdown

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.82-1
- Import
