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
%global upstream_version %(echo %{version} | tr '~' '-')

Name:           hamcrest
Version:        3.0
Release:        %autorelease
Summary:        Library of matchers for building test expressions
License:        BSD-3-Clause
URL:            https://github.com/hamcrest/JavaHamcrest
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/hamcrest/JavaHamcrest/archive/v%{upstream_version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/hamcrest/hamcrest/%{upstream_version}/hamcrest-%{upstream_version}.pom

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 3.0-7

%description
Provides a library of matcher objects (also known as constraints or predicates)
allowing 'match' rules to be defined declaratively, to be used in other
frameworks. Typical scenarios include testing frameworks, mocking libraries and
UI validation rules.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n JavaHamcrest-3.0
%autosetup -p1 -n JavaHamcrest-3.0

pushd hamcrest
cp -p %{SOURCE1} pom.xml
%pom_add_dep junit:junit::test
%pom_xpath_inject pom:project '
<build>
  <plugins>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-compiler-plugin</artifactId>
      <version>any</version>
      <configuration>
        <source>1.8</source>
        <target>1.8</target>
      </configuration>
    </plugin>
    <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-jar-plugin</artifactId>
      <version>any</version>
      <configuration>
        <archive>
          <manifestEntries>
            <Automatic-Module-Name>org.hamcrest</Automatic-Module-Name>
          </manifestEntries>
        </archive>
      </configuration>
    </plugin>
  </plugins>
</build>'

%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-all
%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-core
%mvn_alias org.hamcrest:hamcrest org.hamcrest:hamcrest-library

%build
pushd hamcrest
%mvn_build -j
popd

%install
pushd hamcrest
%mvn_install
popd

%files -f hamcrest/.mfiles
%doc README.md
%license LICENSE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.0-1
- Import
