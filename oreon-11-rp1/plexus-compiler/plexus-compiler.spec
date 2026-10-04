%global source0_hash c26e9cdb8152921d16ac4d734d25a9d2fc347667a39db5d35c3b1b15661da1e0

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

Name:           plexus-compiler
Version:        2.17.1
Release:        %autorelease
Summary:        Compiler call initiators for Plexus
# extras subpackage has a bit different licensing
# parts of compiler-api are Apache-2.0/MIT
License:        MIT AND Apache-2.0
URL:            https://github.com/codehaus-plexus/plexus-compiler
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/codehaus-plexus/%{name}/archive/%{name}-%{version}.tar.gz#/plexus-compiler-%{version}.tar.gz
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
Source2:        https://raw.githubusercontent.com/codehaus-plexus/plexus-compiler/HEAD/LICENSE.MIT

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.inject:javax.inject)
BuildRequires:  mvn(org.codehaus.plexus:plexus-utils)
BuildRequires:  mvn(org.codehaus.plexus:plexus:pom:)
BuildRequires:  mvn(org.eclipse.sisu:org.eclipse.sisu.plexus)
BuildRequires:  mvn(org.eclipse.sisu:sisu-maven-plugin)
BuildRequires:  mvn(org.slf4j:slf4j-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.17.1-11

%description
Plexus Compiler adds support for using various compilers from a
unified api. Support for javac is available in main package. For
additional compilers see %{name}-extras package.

%package extras
Summary:        Extra compiler support for %{name}
# Apache-2.0: src/main/java/org/codehaus/plexus/compiler/util/scan/
#          ...codehaus/plexus/compiler/csharp/CSharpCompiler.java
# Apache-1.1/MIT: ...codehaus/plexus/compiler/jikes/JikesCompiler.java
License:        MIT AND Apache-2.0 AND Apache-1.1

%description extras
Additional support for csharp, eclipse and jikes compilers

%package pom
Summary:        Maven POM files for %{name}

%description pom
This package provides %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n plexus-compiler-plexus-compiler-%{version}

find -name '.class' -delete

cp %{SOURCE1} LICENSE
cp %{SOURCE2} LICENSE.MIT


%pom_disable_module plexus-compiler-aspectj plexus-compilers
# missing com.google.errorprone:error_prone_core
%pom_disable_module plexus-compiler-javac-errorprone plexus-compilers

%pom_disable_module plexus-compiler-eclipse plexus-compilers

# don't build/install compiler-test module, it needs maven2 test harness
%pom_disable_module plexus-compiler-test
%pom_disable_module plexus-compiler-its

# don't install sources jars
%mvn_package ":*::sources:" __noinstall

%mvn_package ":plexus-compiler{,s}" pom
%mvn_package ":*{csharp,eclipse,jikes}*" extras

# don't generate requires on test dependency (see #1007498)
%pom_xpath_remove "pom:dependency[pom:artifactId[text()='plexus-compiler-test']]" plexus-compilers

%pom_remove_plugin :maven-site-plugin
%pom_remove_plugin :maven-enforcer-plugin

%pom_remove_dep -r org.codehaus.plexus:plexus-compiler-javac-errorprone
%pom_remove_dep org.codehaus.plexus:plexus-xml plexus-compiler-manager

%build
# Tests are skipped because of unavailable plexus-compiler-test artifact
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE LICENSE.MIT

%files extras -f .mfiles-extras

%files pom -f .mfiles-pom

%changelog
%autochangelog
