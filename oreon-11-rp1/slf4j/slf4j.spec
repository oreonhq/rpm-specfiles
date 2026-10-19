%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash 843a728aace3c454e08bb1574c470a06551256e6f0389ced7bc520740d9667e9
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
Name:           slf4j
Version:        2.0.20
Release:        1%{?dist}
Summary:        Simple Logging Facade for Java
License:        MIT AND Apache-2.0
URL:            https://www.slf4j.org/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/qos-ch/slf4j/archive/v_%{version}.tar.gz#/slf4j-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
%if %{with bootstrap}
%else
%endif
Obsoletes:      %{name}-javadoc < 2.0.19-13
Obsoletes:      %{name}-manual < 2.0.19-13
# oreon:deps
BuildRequires:  javapackages-bootstrap
# /oreon:deps
%description
The Simple Logging Facade for Java or (SLF4J) is intended to serve
as a simple facade for various logging APIs allowing to the end-user
to plug in the desired implementation at deployment time. SLF4J also
allows for a gradual migration path away from
Jakarta Commons Logging (JCL).

Logging API implementations can either choose to implement the
SLF4J interfaces directly, e.g. NLOG4J or SimpleLogger. Alternatively,
it is possible (and rather easy) to write SLF4J adapters for the given
API implementation, e.g. Log4jLoggerAdapter or JDK14LoggerAdapter..

%package jdk14
Summary:        SLF4J JDK14 Binding
%description jdk14
SLF4J JDK14 Binding.

%package jcl
Summary:        SLF4J JCL Binding
%description jcl
SLF4J JCL Binding.

%package -n jcl-over-%{name}
Summary:        JCL 1.1.1 implemented over SLF4J
%description -n jcl-over-%{name}
JCL 1.1.1 implemented over SLF4J.

%package -n jul-to-%{name}
Summary:        JUL to SLF4J bridge
%description -n jul-to-%{name}
JUL to SLF4J bridge.

%package -n log4j-over-%{name}
Summary:        Log4j implemented over SLF4J
%description -n log4j-over-%{name}
Log4j implemented over SLF4J.

%package migrator
Summary:        SLF4J Migrator
%description migrator
SLF4J Migrator.

%package sources
Summary:        SLF4J Source JARs
%description sources
SLF4J Source JARs.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n slf4j-v_%{version}
%mvn_compat_version : 2.0.17
find -name '*.jar' -delete
install -p -m 0644 %{SOURCE1} LICENSE-2.0.txt

%pom_disable_module integration
%pom_disable_module osgi-over-slf4j
%pom_disable_module slf4j-ext
%pom_disable_module slf4j-log4j12
%pom_disable_module slf4j-reload4j

# Port to maven-antrun-plugin 3.0.0
sed -i s/tasks/target/ slf4j-api/pom.xml

# Because of a non-ASCII comment in slf4j-api/src/main/java/org/slf4j/helpers/MessageFormatter.java
%pom_xpath_inject "pom:project/pom:properties" "
    <project.build.sourceEncoding>ISO-8859-1</project.build.sourceEncoding>"

# Fix javadoc links
%pom_xpath_inject "pom:plugin[pom:artifactId[text()='maven-javadoc-plugin']]/pom:configuration" "
    <detectJavaApiLink>false</detectJavaApiLink>
    <isOffline>false</isOffline>
    <links><link>/usr/share/javadoc/java</link></links>"

# dos2unix
find -name '*.css' -o -name '*.js' -o -name '*.txt' -exec sed -i 's/\r//' {} +

# Remove wagon-ssh build extension
%pom_xpath_remove pom:extensions

# slf4j 2.x generates its OSGi manifest at build time; no static MANIFEST.MF to patch

# Source JARs for are required by Maven 3.4.0
%mvn_package :::sources: sources

%mvn_package :slf4j-parent __noinstall
%mvn_package :slf4j-site __noinstall
%mvn_package :slf4j-api
%mvn_package :slf4j-simple
%mvn_package :slf4j-nop

# Compat symlinks
%mvn_file ':slf4j-{*}' %{name}/slf4j-@1 %{name}/@1

%build

%mvn_build -j -f -s -- -Drequired.jdk.version=1.8
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n slf4j-jdk14 -f %{oreon_filedir}/slf4j-jdk14.list
%files -n slf4j-jcl -f %{oreon_filedir}/slf4j-jcl.list
%files -n jcl-over-slf4j -f %{oreon_filedir}/jcl-over-slf4j.list
%files -n jul-to-slf4j -f %{oreon_filedir}/jul-to-slf4j.list
%files -n log4j-over-slf4j -f %{oreon_filedir}/log4j-over-slf4j.list
%files -n slf4j-migrator -f %{oreon_filedir}/slf4j-migrator.list
%files -n slf4j-sources -f %{oreon_filedir}/slf4j-sources.list

%changelog

%autochangelog
