%global source0_hash b999d69cde60dc151d98f5fdb7dc58502456f982ec9f1441306237dde3160cf8

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
%bcond bootstrap 0

Name:           jline
Version:        4.4.6
Release:        %autorelease
Summary:        Java library for handling console input
License:        BSD-3-Clause AND Apache-2.0
URL:            https://github.com/jline/jline3
ExclusiveArch:  %{java_arches}

Source0:        https://github.com/jline/jline3/archive/refs/tags/%{version}.tar.gz#/jline-%{version}.tar.gz

# Fedora/RHEL specific: JNI shared objects MUST be placed in %%{_prefix}/lib/%%{name}
Patch:          0001-Load-native-library-form-usr-lib-jline.patch
# Patch out unwanted optional dependency on universalchardet
Patch:          0002-Remove-optional-dependency-on-universalchardet.patch

BuildRequires:  gcc
%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.google.code.findbugs:jsr305)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.easymock:easymock)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-params)
%endif
# TODO remove in Fedora 46
Obsoletes:      %{name}-builtins < 3.29.0
Obsoletes:      %{name}-console < 3.29.0
Obsoletes:      %{name}-javadoc < 3.29.0
Obsoletes:      %{name}-native < 3.29.0
Obsoletes:      %{name}-parent < 3.29.0
Obsoletes:      %{name}-reader < 3.29.0
Obsoletes:      %{name}-remote-ssh < 3.29.0
Obsoletes:      %{name}-remote-telnet < 3.29.0
Obsoletes:      %{name}-style < 3.29.0
Obsoletes:      %{name}-terminal < 3.29.0
Obsoletes:      %{name}-terminal-jansi < 3.29.0
Obsoletes:      %{name}-terminal-jna < 3.29.0

%description
JLine is a Java library for handling console input.  It is similar in
functionality to BSD editline and GNU readline but with additional
features that bring it in par with the ZSH line editor.  Those familiar
with the readline/editline capabilities for modern shells (such as bash
and tcsh) will find most of the command editing features of JLine to be
familiar.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
# GitHub archive of tag %%{version} unpacks as jline3-%%{version}.
%autosetup -p1 -n jline3-%{version}
cp -p console-ui/LICENSE.txt LICENSE-APACHE.txt

# Remove local Maven extensions not needed for RPM build
rm -r .mvn/

# Remove prebuilt native objects
rm -r native/src/main/resources/org/jline/nativ/*/

# -Werror is considered harmful for downstream packaging
sed -i /-Werror/d $(find -name pom.xml)

# Optional dependency on juniversalchardet was removed via a patch
%pom_remove_dep -r :juniversalchardet

# Disable test that requires "nano" text editor
rm builtins/src/test/java/org/jline/builtins/SyntaxHighlighterTest.java

# Disable test that uses unpackaged jimfs dependency
%pom_remove_dep :jimfs builtins
rm builtins/src/test/java/org/jline/builtins/SyntaxHighlighterJimFsTest.java

# Disable unwanted modules
%pom_disable_module groovy
%pom_disable_module remote-ssh
%pom_disable_module remote-telnet
%pom_disable_module demo
%pom_disable_module graal

# Unnecessary plugins for an rpm build
%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :spotless-maven-plugin

# There is no need to re-generate jni-config.json for GraalVM
# as is already present under native/src/main/resources/
%pom_remove_plugin :exec-maven-plugin native
%pom_remove_dep :picocli-codegen native

%build
# Build a native object
gcc -Wall %{build_cflags} -fPIC -fvisibility=hidden -shared -I native/src/main/native \
  -I %{_jvmdir}/java/include -I %{_jvmdir}/java/include/linux %{build_ldflags} \
  -o libjlinenative.so native/src/main/native/{jlinenative,clibrary}.c

# Build the Java artifacts
%mvn_build -j -- -P\!bundle -Dlibrary.jline.path=$PWD

%install
%mvn_install
install -d -m 755 %{buildroot}%{_prefix}/lib/%{name}/
install -p -m 755 libjlinenative.so %{buildroot}%{_prefix}/lib/%{name}/

%files -f .mfiles
%{_prefix}/lib/%{name}
%doc README.md
%license LICENSE.txt LICENSE-APACHE.txt

%changelog
%autochangelog
