%global source0_hash 587b12eae125a916b9cef2217694def2a42715339f2f239bd8c00d2783a1da82

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

Name:           google-gson
Version:        2.14.0
Release:        %autorelease
Summary:        Java lib for conversion of Java objects into JSON representation
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:        Apache-2.0
URL:            https://github.com/google/gson
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/google/gson/archive/gson-parent-%{version}.tar.gz#/google-gson-%{version}.tar.gz

BuildRequires:  jurand
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.annotation:jsr250-api)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.14.0-3

%description
Gson is a Java library that can be used to convert a Java object into its
JSON representation. It can also be used to convert a JSON string into an
equivalent Java object. Gson can work with arbitrary Java objects including
pre-existing objects that you do not have source-code of.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n gson-gson-parent-%{version}

%pom_remove_plugin -r :maven-enforcer-plugin
%pom_remove_plugin -r :spotless-maven-plugin
%pom_remove_plugin -r :maven-artifact-plugin
%pom_remove_plugin -r :maven-failsafe-plugin
%pom_remove_plugin :bnd-maven-plugin gson
%pom_remove_plugin :maven-jar-plugin gson
%pom_remove_plugin :maven-compiler-plugin

%pom_remove_dep -r :error_prone_annotations
%java_remove_annotations gson extras -s \
  -p com[.]google[.]errorprone[.]annotations[.] \

# The test EnumWithObfuscatedTest requires the plugins copy-rename-maven-plugin, proguard-maven-plugin and maven-resources-plugin to work correctly because it tests Gson interaction with a class obfuscated by ProGuard.
# https://github.com/google/gson/issues/2045
rm ./gson/src/test/java/com/google/gson/functional/EnumWithObfuscatedTest.java

# to check later
rm ./gson/src/test/java/com/google/gson/internal/bind/DefaultDateTypeAdapterTest.java
# remove unnecessary dependency on parent POM
# POM doesn't specify parent.
#%%pom_remove_parent

%pom_remove_plugin :proguard-maven-plugin gson

%pom_remove_plugin  :moditect-maven-plugin gson

# Remove dependency on unavailable templating-maven-plugin
%pom_remove_plugin  org.codehaus.mojo:templating-maven-plugin gson
sed 's/${project.version}/%{version}/' gson/src/main/java-templates/com/google/gson/internal/GsonBuildConfig.java >gson/src/main/java/com/google/gson/internal/GsonBuildConfig.java

#depends on com.google.caliper
%pom_disable_module metrics

#depends on com.google.protobuf:protobuf-java:jar:4.0.0-rc-2 and com.google.truth:truth:jar:1.1.3
%pom_disable_module proto

%pom_disable_module test-jpms
%pom_disable_module test-graal-native-image
%pom_disable_module test-shrinker

%build
%mvn_build -j -f

%install
%mvn_install

%files -f .mfiles
%license LICENSE
%doc README.md CHANGELOG.md UserGuide.md

%changelog
%autochangelog
