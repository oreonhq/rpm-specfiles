%global source0_hash 82359f0a2e638a7cd30f46888dc892b262915a7145a57303b0256d01fac2c9d8

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
%bcond bootstrap 0

Name:           plexus-xml
Version:        4.0.4
Release:        %autorelease
Summary:        Plexus XML Utilities
# Licensing breakdown:
# Apache-1.1: src/main/java/org/codehaus/plexus/util/xml/StringUtils.java
# xpp: src/main/java/org/codehaus/plexus/util/xml/pull/MXParser.java
# Everything else is Apache-2.0
License:        Apache-1.1 AND Apache-2.0 AND xpp
URL:            https://codehaus-plexus.github.io/plexus-xml/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz#/plexus-xml-4.0.4.tar.gz

# https://github.com/codehaus-plexus/plexus-xml/pull/53
Patch:          0001-Upgrade-to-Maven-4.0.0-rc-2.patch
# https://github.com/codehaus-plexus/plexus-xml/pull/65
Patch:          0002-Bump-org.apache.maven-maven-xml-from-4.0.0-rc-3-to-4.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.maven:maven-xml:4.0.0-rc-4)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.0.4-5

%description
A collection of various utility classes to ease working with XML.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n plexus-xml-plexus-xml-4.0.4
%autosetup -p1 -n plexus-xml-plexus-xml-4.0.4

%build
# Test dependencies are not packaged
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license NOTICE.txt LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.4-1
- Prepare for Oreon 11 (RP1)
