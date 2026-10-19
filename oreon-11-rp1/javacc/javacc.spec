%global source0_hash d1bfebb4ca9261c5c3b16b00280b3278a41b193ca8503f2987f72de453bf99c6
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
%global giturl  https://github.com/javacc/javacc
Name:           javacc
Version:        7.0.13
Release:        1%{?dist}
Summary:        A parser/scanner generator for java
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://javacc.org/
VCS:            git:%{giturl}.git
Source0:        https://github.com/javacc/javacc/archive/refs/tags/javacc-7.0.13.tar.gz#/javacc-7.0.13.tar.gz
Patch:          0001-Fix-javadoc-errors-in-JavaCharStream.template.patch
%if %{with bootstrap}
%else
%endif
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  javapackages-bootstrap
# /oreon:deps
%description
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

%package manual
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND (AFL-2.0 OR BSD-3-Clause) AND ISC
Summary:        Manual for %{name}
Obsoletes:      %{name}-javadoc < 7.0.13-5
%description manual
Manual for %{name}.

%package demo
Summary:        Examples for %{name}
Requires:       %{name} = %{version}-%{release}
%description demo
Examples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n javacc-javacc-7.0.13
%autosetup -p1 -n javacc-javacc-7.0.13

# Remove binary information in the source tar
find . -name "*.jar" -delete
find examples -name .gitignore -delete

fixtimestamp() {
  touch -r $1.orig $1
  rm $1.orig
}

mv examples/JJTreeExamples/cpp/README examples/JJTreeExamples/cpp/README.orig
iconv -f WINDOWS-1252 -t UTF-8 examples/JJTreeExamples/cpp/README.orig > \
  examples/JJTreeExamples/cpp/README
fixtimestamp examples/JJTreeExamples/cpp/README

sed -i.orig 's/\r//' examples/JJTreeExamples/cpp/eg3.jjt
fixtimestamp examples/JJTreeExamples/cpp/eg3.jjt

%build

%if %{with bootstrap}
cp %{_datadir}/javapackages-bootstrap/javacc.jar bootstrap/javacc.jar
%else
build-jar-repository -p bootstrap javacc
%endif
%ant jar -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8
%mvn_artifact --skip-dependencies pom.xml target/javacc.jar
%install
%mvn_file : %{name}
%mvn_install
%jpackage_script javacc '' '' javacc javacc true
ln -s javacc %{buildroot}%{_bindir}/javacc.sh
%jpackage_script jjdoc '' '' javacc jjdoc true
%jpackage_script jjtree '' '' javacc jjtree true
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n javacc-manual -f %{oreon_filedir}/javacc-manual.list
%files -n javacc-demo -f %{oreon_filedir}/javacc-demo.list

%changelog

* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.13-1
- Import
