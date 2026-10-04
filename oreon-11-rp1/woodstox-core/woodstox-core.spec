%global source0_hash 295b33f73296cf1bc2574f2b3f143072d7aef121900c20efb52c4033b2b70650

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

Name:           woodstox-core
Version:        7.2.2
Release:        %autorelease
Summary:        High-performance XML processor
License:        Apache-2.0
URL:            https://github.com/FasterXML/woodstox
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        %{url}/archive/%{name}-%{version}.tar.gz

# Port to latest OSGi APIs
Patch:          0001-Allow-building-against-OSGi-APIs-newer-than-R4.patch
# Drop requirements on defunct optional dependencies: msv and relaxng
Patch:          0002-Patch-out-optional-support-for-msv-and-relax-schema-.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(biz.aQute.bnd:biz.aQute.bnd.annotation)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.woodstox:stax2-api)
BuildRequires:  mvn(org.mockito:mockito-core)
BuildRequires:  mvn(org.osgi:osgi.core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 7.2.2-5

%description
Woodstox is a high-performance namespace-aware StAX-compliant
(JSR-173) Open Source XML-processor written in Java.  XML processor
means that it handles both input (parsing) and output (writing,
serialization), as well as supporting tasks such as validation.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n woodstox-woodstox-core-%{version}
%pom_remove_parent
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :jacoco-maven-plugin

# comment in src/moditect/module-info.java explains it...
# // hand-crafted on 14-Jul-2019 -- probably all wrong
%pom_remove_plugin :moditect-maven-plugin

# Patch out optional support for msv and relax schema validation
%pom_remove_dep net.java.dev.msv:
%pom_remove_dep :relaxngDatatype
%pom_remove_dep :isorelax
%pom_remove_plugin :maven-shade-plugin
rm -r src/main/java/com/ctc/wstx/msv
rm src/test/java/failing/{RelaxNGTest,TestRelaxNG189,TestRelaxNG190,TestW3CSchema189,W3CDefaultValuesTest,W3CSchemaTypesTest}.java
rm src/test/java/stax2/vwstream/{W3CSchemaWrite16Test,W3CSchemaWrite23Test}.java
rm src/test/java/wstxtest/msv/{TestW3CSchema,TestW3CSchemaTypes,TestWsdlValidation}.java
rm src/test/java/wstxtest/vstream/{TestRelaxNG,TestW3CSchemaComplexTypes}.java

%build
%mvn_build -j -- -Dversion.junit=4.12

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
%autochangelog
