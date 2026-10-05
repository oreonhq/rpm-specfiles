%global source0_hash 8a21d8e3756d041580dfb91afe8070f7988e52a766ab6fba41bbcac7f96f4b6c

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
%global srcname JCTools

Name:           jctools
Version:        4.0.7
Release:        %autorelease
Summary:        Java Concurrency Tools for the JVM
License:        Apache-2.0
URL:            https://github.com/JCTools/JCTools
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/JCTools/JCTools/archive/v4.0.5/JCTools-4.0.5.tar.gz#/jctools-4.0.5.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.guava:guava-testlib)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.hamcrest:hamcrest-all)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 4.0.2-15

%description
This project aims to offer some concurrent data structures
currently missing from the JDK:

° SPSC/MPSC/SPMC/MPMC Bounded lock free queues
° SPSC/MPSC Unbounded lock free queues
° Alternative interfaces for queues
° Offheap concurrent ring buffer for ITC/IPC purposes
° Single Writer Map/Set implementations
° Low contention stats counters
° Executor

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n JCTools-4.0.5

# drop some failure-prone tests (race conditions?)
rm jctools-core/src/test/java/org/jctools/queues/MpqSanityTestMpscCompound.java

# set correct version in all pom.xml files
%pom_xpath_set pom:project/pom:version %{version}
%pom_xpath_set pom:parent/pom:version %{version} jctools-{build,core,channels,experimental}

# remove plugins unnecessary for RPM builds
%pom_remove_plugin :coveralls-maven-plugin jctools-core
%pom_remove_plugin :jacoco-maven-plugin jctools-core
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :maven-source-plugin jctools-core
%pom_remove_plugin :maven-javadoc-plugin jctools-core

# remove tests with additional kotlin dependencies
rm -r jctools-core/src/test/java/org/jctools/maps/linearizability_test/

# disable unused modules with unavailable dependencies
%pom_disable_module jctools-benchmarks
%pom_disable_module jctools-concurrency-test

# incompatible with Java 11 and unused in fedora:
# https://github.com/JCTools/JCTools/issues/254
%pom_disable_module jctools-channels
%pom_disable_module jctools-experimental

%pom_disable_module jctools-build
%pom_remove_plugin :exec-maven-plugin jctools-core

# do not install internal build tools
%mvn_package :jctools-build __noinstall

# do not install unused parent POM
%mvn_package :jctools-parent __noinstall

%build
# Tests time out in Koji
%mvn_build -j -s -f

%install
%mvn_install

%files -f .mfiles-jctools-core
%doc README.md
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.0.5-1
- Import
