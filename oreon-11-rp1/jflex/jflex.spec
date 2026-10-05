%global source0_hash e0c1e9eef91ff6df04d73fa5eaff13f3a02b679fee1474e5ccae007224df6df6

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
Name:           jflex
Version:        1.9.1
Release:        %autorelease
Summary:        Fast Scanner Generator
License:        BSD-3-Clause
URL:            https://jflex.de/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://jflex.de/release/jflex-1.9.1.tar.gz
Source4:        %{name}.1

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(java_cup:java_cup)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.ant:ant)
%endif
%if %{without bootstrap}
BuildRequires:  jflex
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.9.1-44

%description
JFlex is a lexical analyzer generator (also known as scanner
generator) for Java, written in Java.  It is also a rewrite of the
very useful tool JLex which was developed by Elliot Berk at Princeton
University.  As Vern Paxson states for his C/C++ tool flex: They do
not share any code though.  JFlex is designed to work together with
the LALR parser generator CUP by Scott Hudson, and the Java
modification of Berkeley Yacc BYacc/J by Bob Jamison.  It can also be
used together with other parser generators like ANTLR or as a
standalone tool.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1
find . -name '*.jar' -delete
rm -rf src/main/java/java_cup examples
%mvn_file : %{name}
%pom_add_dep java_cup:java_cup

%pom_remove_plugin :jflex-maven-plugin
%pom_remove_plugin :cup-maven-plugin
%pom_remove_plugin :maven-shade-plugin
%pom_remove_dep :java-cup-runtime

# Tests fail with 320k stacks (default on i686), so lets increase
# stack to 16M to avoid stack overflows.  See rhbz#1119308
%pom_xpath_inject "pom:plugin[pom:artifactId='maven-surefire-plugin']/pom:configuration" "<argLine>-Xss16384k</argLine>"

%pom_xpath_remove "pom:plugin[pom:artifactId='maven-site-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='fmt-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='cup-maven-plugin']" parent.xml
%pom_xpath_remove "pom:plugin[pom:artifactId='maven-shade-plugin']" parent.xml

%pom_xpath_remove "pom:profile[pom:id='error-prone']" parent.xml

sed -i /%%inputstreamctor/d src/main/jflex/LexScan.flex

%build
%{?jpb_env}
cup -parser LexParse -interface -destdir src/main/java src/main/cup/LexParse.cup
jflex -d src/main/java/jflex --skel src/main/jflex/skeleton.nested src/main/jflex/LexScan.flex
%mvn_build -j -- -P\!error-prone -Djflex.jdk.version=1.8

%install
%mvn_install

# wrapper script for direct execution
%jpackage_script jflex.Main "" "" jflex:java_cup jflex true

# manpage
install -d -m 755 %{buildroot}%{_mandir}/man1
install -p -m 644 %{SOURCE4} %{buildroot}%{_mandir}/man1

%files -f .mfiles
%doc doc
%license COPYRIGHT
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.7.0-1
- Prepare for Oreon 11 (RP1)
