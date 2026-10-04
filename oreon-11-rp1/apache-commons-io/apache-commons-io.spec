%global source0_hash 9a8e6d731e06edb10a35e2221aeea7f539b3ff4d5b90538bf119726e72644ff4

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
Name:           apache-commons-io
Epoch:          1
Version:        2.22.0
Release:        %autorelease
Summary:        Utilities to assist with developing IO functionality
License:        Apache-2.0
URL:            https://commons.apache.org/proper/commons-io/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://archive.apache.org/dist/commons/io/source/commons-io-%{version}-src.tar.gz

BuildRequires:  jurand
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-lang3)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.apache.maven.plugins:maven-antrun-plugin)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:2.16.1-13

%description
Commons-IO contains utility classes, stream implementations,
file filters, and endian classes. It is a library of utilities
to assist with developing IO functionality.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n commons-io-%{version}-src

sed -i 's/\r//' *.txt

# Run tests in multiple reusable forks to improve test performance
sed -i -e /reuseForks/d -e /forkCount/d pom.xml
sed -i '/<argLine>/d' pom.xml

%mvn_file : commons-io %{name}
%mvn_alias : org.apache.commons:

%pom_remove_dep org.junit-pioneer:junit-pioneer
jurand -i -s -a src -n DefaultLocale

%pom_remove_dep com.google.jimfs:jimfs
rm src/test/java/org/apache/commons/io/input/ReversedLinesFileReaderParamFileTest.java
rm src/test/java/org/apache/commons/io/file/PathUtilsContentEqualsTest.java

%build
# See "-DcommonsIoVersion" in maven-surefire for the tested version

# The following tests fail on tmpfs/nfs:
#  * PathUtilsDeleteDirectoryTest.testDeleteDirectory1FileSize0OverrideReadOnly:80->testDeleteDirectory1FileSize0:68 » FileSystem
#  * PathUtilsDeleteFileTest.testDeleteReadOnlyFileDirectory1FileSize1:114 » FileSystem
#  * PathUtilsDeleteFileTest.testSetReadOnlyFileDirectory1FileSize1:134 » FileSystem
#  * PathUtilsDeleteTest.testDeleteDirectory1FileSize0OverrideReadonly:97->testDeleteDirectory1FileSize0:69 » FileSystem
#  * PathUtilsDeleteTest.testDeleteDirectory1FileSize1OverrideReadOnly:145->testDeleteDirectory1FileSize1:117 » FileSystem

# moditect profile generates module-info.class
%mvn_build -j -f -- -Dcommons.osgi.symbolicName=org.apache.commons.io

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt

%changelog
%autochangelog
