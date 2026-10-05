%global source0_hash 88efcb52da0b1983724d7daf33969229401f297911c5c3ddead2e34fda46cff6

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
%bcond_with bootstrap

Name:           xmlunit
Version:        2.13.0
Release:        %autorelease
Summary:        Provides classes to do asserts on xml
# The whole package is ASL 2.0 except for xmlunit-legacy which is BSD
License:        Apache-2.0
URL:            https://www.xmlunit.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/xmlunit/xmlunit/releases/download/v%{version}/%{name}-%{version}-src.tar.gz#/%{name}-%{version}.tar.gz
# Remove bundled binaries which cannot be easily verified for licensing
Patch:        0001-Disable-tests-requiring-network-access.patch
# This also solves the problem of tests requiring network. The files that would
# be fetched are identical to the local file
Patch:        0003-Drop-support-for-JAXB.patch
Patch:        0004-Port-to-assertj-core-3.patch

BuildRequires:  jurand
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-core)
BuildRequires:  mvn(org.hamcrest:hamcrest-library)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.13.0-8

%description
XMLUnit provides you with the tools to verify the XML you emit is the one you
want to create. It provides helpers to validate against an XML Schema, assert
the values of XPath queries or compare XML documents against expected outcomes.

%package assertj
Summary:        Assertj for %{name}

%description assertj
This package provides %{summary}.

%package core
Summary:        Core package for %{name}

%description core
This package provides %{summary}.

%package legacy
Summary:        Legacy package for %{name}
License:        BSD-3-Clause

%description legacy
This package provides %{summary}.

%package matchers
Summary:        Matchers for %{name}

%description matchers
This package provides %{summary}.

%package placeholders
Summary:        Placeholders for %{name}

%description placeholders
This package provides %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-%{version}-src


rm -r xmlunit-core/src/main/java/org/xmlunit/builder/javax_jaxb\
 xmlunit-core/src/main/java/org/xmlunit/builder/JaxbBuilderFactory.java\
 xmlunit-core/src/main/java/org/xmlunit/builder/JaxbBuilderFactoryLocator.java\
 xmlunit-core/src/test/java/org/xmlunit/builder/javax_jaxb\
;


# Port to hamcrest 2.1
%java_remove_annotations xmlunit-matchers -p org[.]hamcrest[.]Factory

%pom_disable_module xmlunit-assertj
%pom_disable_module xmlunit-jakarta-jaxb-impl

%pom_remove_plugin org.codehaus.mojo:buildnumber-maven-plugin
%pom_remove_plugin :maven-assembly-plugin
%pom_remove_plugin -r :maven-shade-plugin
%pom_remove_plugin -r org.cyclonedx:cyclonedx-maven-plugin

%mvn_alias org.xmlunit:xmlunit-legacy xmlunit:xmlunit
%mvn_alias org.xmlunit:xmlunit-assertj3 org.xmlunit:xmlunit-assertj

# JAXB and JAF are not available in JDK11
%pom_remove_dep org.glassfish.jaxb: xmlunit-core
%pom_remove_dep jakarta.xml.bind: xmlunit-core
rm -rf xmlunit-core/src/{main,test}/java/org/xmlunit/builder/{jaxb/,JaxbBuilder.java,JaxbBuilderTest.java}

%build
%mvn_build -j -s -- -Dmaven.compile.source=1.8 -Dmaven.compile.target=1.8

%install
%mvn_install

%files -f .mfiles-xmlunit-parent
%doc README.md CONTRIBUTING.md RELEASE_NOTES.md
%license LICENSE

%files assertj -f .mfiles-xmlunit-assertj3

%files core -f .mfiles-xmlunit-core

%files legacy -f .mfiles-xmlunit-legacy

%files matchers -f .mfiles-xmlunit-matchers

%files placeholders -f .mfiles-xmlunit-placeholders

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10.0-1
- Import
