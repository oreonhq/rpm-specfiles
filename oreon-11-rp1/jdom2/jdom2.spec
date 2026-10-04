%global source0_hash 18639399104d5c57b92fd6791823a74393651e80499b67ae3067294d62df083e

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

Name:           jdom2
Version:        2.0.6.1
Release:        %autorelease
Summary:        Java manipulation of XML made easy
License:        Saxpath
URL:            http://www.jdom.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/hunterhacker/jdom/archive/refs/tags/JDOM-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Bnd tool configuration
Source3:        bnd.properties
# Remove bundled jars that might not have clear licensing
# Use system libraries
# Disable gpg signatures
# Process contrib and junit pom files
Patch:        0001-Adapt-build.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
BuildRequires:  ant-junit
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.0.6.1-21

%description
JDOM is a Java-oriented object model which models XML documents.
It provides a Java-centric means of generating and manipulating
XML documents. While JDOM inter-operates well with existing
standards such as the Simple API for XML (SAX) and the Document
Object Model (DOM), it is not an abstraction layer or
enhancement to those APIs. Rather, it seeks to provide a robust,
light-weight means of reading and writing XML data without the
complex and memory-consumptive options that current API
offerings provide.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n jdom-JDOM-%{version}


sed -i 's/\r//' LICENSE.txt

# Unable to run coverage: use log4j12 but switch to log4j 2.x
sed -i.coverage "s|coverage, jars|jars|" build.xml

# XPath functionality is not needed
rm -rf core/src/java/org/jdom2/xpath/
sed -i '/import org.jdom2.xpath.XPathFactory/d' core/src/java/org/jdom2/JDOMConstants.java

%build
mkdir lib
%ant -Dversion=%{version} -Dcompile.source=1.8 -Dcompile.target=1.8 maven

# Make jar into an OSGi bundle
# XXX disabled until BND is fixed
#bnd wrap --output build/package/jdom-%%{version}.bar --properties %%{SOURCE3} \
#         --version %%{version} build/package/jdom-%%{version}.jar
#mv build/package/jdom-%%{version}.bar build/package/jdom-%%{version}.jar

%install
%mvn_artifact build/maven/core/%{name}-%{version}.pom build/package/jdom-%{version}.jar
%mvn_install

%files -f .mfiles
%doc CHANGES.txt COMMITTERS.txt README.md TODO.txt
%license LICENSE.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.6.1-1
- Import
