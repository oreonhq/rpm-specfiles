%global source0_hash d1bfebb4ca9261c5c3b16b00280b3278a41b193ca8503f2987f72de453bf99c6

# Copyright (c) 2000-2005, JPackage Project
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the
#    distribution.
# 3. Neither the name of the JPackage Project nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

# Build in bootstrap mode on new architectures
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
%bcond bootstrap 0

%global giturl  https://github.com/javacc/javacc

Name:           javacc
Version:        7.0.13
Release:        %autorelease
Summary:        A parser/scanner generator for java

# BSD-3-Clause: the project as a whole
# BSD-2-Clause:
# - src/main/javacc/ConditionParser.jj
# - src/main/java/org/javacc/parser/OutputFile.java
# - src/main/java/org/javacc/utils/OutputFileGenerator.java
License:        BSD-3-Clause AND BSD-2-Clause
URL:            https://javacc.org/
VCS:            git:%{giturl}.git
Source:        https://github.com/javacc/javacc/archive/refs/tags/javacc-7.0.13.tar.gz#/javacc-7.0.13.tar.gz
# Fix javadoc errors in the JavaCharStream template
# https://github.com/javacc/javacc/pull/257
Patch:          0001-Fix-javadoc-errors-in-JavaCharStream.template.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
BuildRequires:  javacc
%endif

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
Java Compiler Compiler (JavaCC) is the most popular parser generator for use
with Java applications. A parser generator is a tool that reads a grammar
specification and converts it to a Java program that can recognize matches to
the grammar. In addition to the parser generator itself, JavaCC provides other
standard capabilities related to parser generation such as tree building (via
a tool called JJTree included with JavaCC), actions, debugging, etc.

%package manual
# BSD-3-Clause: the project license
# GPL-2.0-or-later: docs/grammars/AsnParser.jj
# LGPL-2.1-or-later: docs/grammars/{ChemNumber.jj,RTFParser.jj}
# AFL-2.0 OR BSD-3-Clause: docs/grammars/EcmaScript.jjt
# ISC: docs/grammars/JSONParser.jjt
License:        BSD-3-Clause AND GPL-2.0-or-later AND LGPL-2.1-or-later AND (AFL-2.0 OR BSD-3-Clause) AND ISC
Summary:        Manual for %{name}
# TODO Remove in Fedora 46
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

# There is maven pom which doesn't really work for building. The tests don't
# work either (even when using bundled jars).
%ant jar -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8

# The pom dependencies are also wrong
%mvn_artifact --skip-dependencies pom.xml target/javacc.jar

%install
%mvn_file : %{name}

%mvn_install

%jpackage_script javacc '' '' javacc javacc true
ln -s javacc %{buildroot}%{_bindir}/javacc.sh
%jpackage_script jjdoc '' '' javacc jjdoc true
%jpackage_script jjtree '' '' javacc jjtree true

%files -f .mfiles
%license LICENSE
%doc README.md
%{_bindir}/javacc
%{_bindir}/javacc.sh
%{_bindir}/jjdoc
%{_bindir}/jjtree

%files manual
%doc docs/*

%files demo
%doc examples

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 7.0.13-1
- Import
