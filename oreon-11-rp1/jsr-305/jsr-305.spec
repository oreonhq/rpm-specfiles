%global source0_hash 8af3a7cf71c365163eb0409491ac7f8c28b0db61da1e35935ad1c6d50afc6df5
%global source1_hash 57d47e633507ce6e039dd52752720fdc96262093d58e1f43a117a995e312cf09

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

Name:           jsr-305
Version:        3.0.2
Release:        %autorelease
Summary:        Correctness annotations for Java code
# The majority of code is BSD-licensed.
# JCIP annotations are Apache-licensed.
License:        BSD-3-Clause AND Apache-2.0
URL:            https://code.google.com/p/jsr-305
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/amaembo/jsr-305/archive/d7734b13c61492982784560ed5b4f4bd6cf9bb2c/%{name}-%{version}.tar.gz#/jsr-305-3.0.2.tar.gz
Source1:        https://github.com/stephenc/jcip-annotations/archive/refs/tags/jcip-annotations-1.0-1.tar.gz#/jcip-annotations-1.0-1.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.0.2-39

%description
This package contains reference implementations, test cases, and other
documents for Java Specification Request 305: Annotations for Software Defect
Detection.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n %{name}-d7734b13c61492982784560ed5b4f4bd6cf9bb2c

# Replace javax.annotation.concurrent annotations (that are based on
# code from https://jcip.net/ and are licensed under CC-BY-2.5, which
# is not Fedora-approved for code) with a clean-room implementation
# under Apache-2.0 from https://github.com/stephenc/jcip-annotations
tar xf %{SOURCE1}
rm -rf ri/src/main/java/javax/annotation/concurrent
mv jcip-annotations-jcip-annotations-1.0-1/src/main/java/net/jcip/annotations ri/src/main/java/javax/annotation/concurrent
sed -i /^package/s/net.jcip.annotations/javax.annotation.concurrent/ ri/src/main/java/javax/annotation/concurrent/*

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/*" 1.8
%pom_remove_plugin :maven-compiler-plugin ri

%pom_xpath_set '/pom:project/pom:groupId' 'org.jsr-305' ri/pom.xml
%pom_xpath_set '/pom:project/pom:artifactId' 'ri' ri/pom.xml

%mvn_file :ri %{name}
%mvn_alias :ri com.google.code.findbugs:jsr305
%mvn_package ":{proposedAnnotations,tcl}" __noinstall

# do not build sampleUses module - it causes Javadoc generation to fail
%pom_disable_module sampleUses

%pom_remove_parent ri
%pom_add_parent org.jsr-305:jsr-305:0.1-SNAPSHOT ri

%pom_remove_plugin org.sonatype.plugins:nexus-staging-maven-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-source-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-javadoc-plugin ri
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin ri

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license ri/LICENSE jcip-annotations-jcip-annotations-1.0-1/LICENSE.txt
%doc sampleUses

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0.2-1
- Import
