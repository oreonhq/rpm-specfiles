%global source0_hash none

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
%global tarball_name RELEASE_%(echo '%{version}' | tr . _)

Name:           cglib
Version:        3_3_0
Release:        %autorelease
Summary:        Code Generation Library for Java
# ASM MethodVisitor is based on ASM code and therefore
# BSD-licensed. Everything else is ASL 2.0.
License:        Apache-2.0 AND BSD-3-Clause
URL:            https://github.com/cglib/cglib
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/cglib/cglib/archive/%{tarball_name}.tar.gz#/cglib-3.3.0.tar.gz

Patch:          0001-Remove-unused-import.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.ant:ant)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.ow2.asm:asm)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3_3_0-38

%description
cglib is a powerful, high performance and quality code generation library
for Java. It is used to extend Java classes and implements interfaces
at run-time.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n cglib-RELEASE_3_3_0
%autosetup -p1 -n cglib-RELEASE_3_3_0

# remove unnecessary dependency on parent POM
%pom_remove_parent

%pom_disable_module cglib-nodep
%pom_disable_module cglib-integration-test
%pom_disable_module cglib-jmh
%pom_xpath_set pom:packaging 'bundle' cglib
%pom_xpath_inject pom:build/pom:plugins '<plugin>
                                           <groupId>org.apache.felix</groupId>
                                           <artifactId>maven-bundle-plugin</artifactId>
                                           <version>1.4.0</version>
                                           <extensions>true</extensions>
                                           <configuration>
                                             <instructions>
                                               <Bundle-SymbolicName>net.sf.cglib.core</Bundle-SymbolicName>
                                               <Export-Package>net.*</Export-Package>
                                               <Import-Package>org.apache.tools.*;resolution:=optional,*</Import-Package>
                                             </instructions>
                                           </configuration>
                                         </plugin>' cglib
%pom_remove_plugin org.apache.maven.plugins:maven-gpg-plugin
%pom_remove_plugin org.apache.maven.plugins:maven-jarsigner-plugin cglib-sample
%pom_remove_plugin -r :maven-javadoc-plugin

%mvn_alias :cglib "net.sf.cglib:cglib" "cglib:cglib-full" "cglib:cglib-nodep" "org.sonatype.sisu.inject:cglib"

%build
# 5 tests fail with OpenJDK 11
# Forwarded upstream: https://github.com/cglib/cglib/issues/119
%mvn_build -j -f -- -Djava.version.source=1.8 -Djava.version.target=1.8

%install
%mvn_install

%files -f .mfiles
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.3.0-1
- Import
