%global source0_hash d076d0b1990fc63fc7ad09cdad7cde8cd0c3b0c217c029f322b9af7527c2e06b

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

Name:           jakarta-annotations
Version:        3.0.0
Release:        %autorelease
Summary:        Jakarta Annotations
License:        EPL-2.0 OR GPL-2.0-only WITH Classpath-exception-2.0
URL:            https://jakarta.ee/specifications/annotations/1.3/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jakartaee/common-annotations-api/archive/%{version}/common-annotations-api-%{version}.tar.gz#/jakarta-annotations-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.0.0-41
Provides:       glassfish-annotation-api = %{version}-%{release}

%description
Jakarta Annotations defines a collection of annotations representing
common semantic concepts that enable a declarative style of
programming that applies across a variety of Java technologies.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n common-annotations-api-%{version}

# remove unnecessary dependency on parent POM
# org.eclipse.ee4j:project is not packaged and isn't needed
%pom_remove_parent api

# 3.x has no aggregator POM; only the api module is built

# remove plugins not needed for RPM builds
%pom_remove_plugin :maven-javadoc-plugin api
%pom_remove_plugin :maven-source-plugin api

# Remove use of spec-version-maven-plugin
%pom_remove_plugin :spec-version-maven-plugin api
%pom_xpath_set pom:Bundle-Version '${project.version}' api
%pom_xpath_set pom:Bundle-SymbolicName '${project.artifactId}' api
%pom_xpath_set pom:Extension-Name '${extension.name}' api
%pom_xpath_set pom:Implementation-Version '${project.version}' api
%pom_xpath_set pom:Specification-Version '${spec.version}' api

# provide aliases for the old artifact coordinates
%mvn_alias jakarta.annotation:jakarta.annotation-api \
  javax.annotation:javax.annotation-api \
  javax.annotation:jsr250-api

%build
pushd api
%mvn_build -j
popd

%install
pushd api
%mvn_install
popd

%files -f api/.mfiles
%license LICENSE.md NOTICE.md
%doc README.md

%changelog
%autochangelog
