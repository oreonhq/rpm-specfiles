%global source0_hash d4638f0460cc85f2ec3ecf75f040e8fc8877d6eaa891925a718282b1ed58d88f
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
%bcond_with bootstrap
Name:           jaxb
Version:        4.0.9
Release:        1%{?dist}
Summary:        JAXB Reference Implementation
License:        BSD-3-Clause
URL:            https://github.com/eclipse-ee4j/jaxb-ri
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/eclipse-ee4j/jaxb-ri/archive/refs/tags/4.0.9-RI.tar.gz#/jaxb-4.0.5.tar.gz
%if %{with bootstrap}
%else
%endif
# oreon:deps
BuildRequires:  javapackages-bootstrap
# /oreon:deps
%description
GlassFish JAXB Reference Implementation.

%package codemodel
Summary:        Codemodel Core
%description codemodel
The core functionality of the CodeModel java source code generation library.

%package codemodel-annotation-compiler
Summary:        Codemodel Annotation Compiler
%description codemodel-annotation-compiler
The annotation compiler ant task for the CodeModel java source code generation
library.

%package relaxng-datatype
Summary:        RelaxNG Datatype
%description relaxng-datatype
RelaxNG Datatype library.

%package xsom
Summary:        XML Schema Object Model
%description xsom
XML Schema Object Model (XSOM) is a Java library that allows applications to
easily parse XML Schema documents and inspect information in them. It is
expected to be useful for applications that need to take XML Schema as an
input.

%package core
Summary:        JAXB Core
%description core
JAXB Core module. Contains sources required by XJC, JXC and Runtime modules.

%package rngom
License:        MIT AND BSD-3-Clause
Summary:        RELAX NG Object Model/Parser
%description rngom
This package contains RELAX NG Object Model/Parser.

%package runtime
Summary:        JAXB Runtime
%description runtime
JAXB (JSR 222) Reference Implementation

%package txw2
Summary:        TXW2 Runtime
%description txw2
TXW is a library that allows you to write XML documents.

%package xjc
License:        BSD-3-Clause AND Apache-2.0
Summary:        JAXB XJC
%description xjc
JAXB Binding Compiler. Contains source code needed for binding customization
files into java sources. In other words: the tool to generate java classes for
the given xml representation.

%package txwc2
Summary:        TXW2 Compiler
%description txwc2
JAXB schema generator. The tool to generate XML schema based on java classes.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n jaxb-ri-%{version}-RI

pushd jaxb-ri

# Remove ee4j parent
%pom_remove_parent boms/bom codemodel external xsom

%pom_remove_plugin -r :buildnumber-maven-plugin
%pom_remove_plugin -r :maven-enforcer-plugin

# Skip docs generation because of missing dependencies
%pom_xpath_remove "pom:profiles/pom:profile[pom:id='default-profile']/pom:modules"

# Disable unneeded extra OSGi bundles
%pom_disable_module bundles

# Missing dependency on org.checkerframework:compiler
%pom_disable_module jxc

%pom_remove_dep org.eclipse.angus:angus-activation core

# Don't install aggregator and parent poms
%mvn_package :jaxb-bom __noinstall
%mvn_package :jaxb-bom-ext __noinstall
%mvn_package :jaxb-bundles __noinstall
%mvn_package :jaxb-codemodel-parent __noinstall
%mvn_package :jaxb-docs-parent __noinstall
%mvn_package :jaxb-external-parent __noinstall
%mvn_package :jaxb-parent __noinstall
%mvn_package :jaxb-runtime-parent __noinstall
%mvn_package :jaxb-samples __noinstall
%mvn_package :jaxb-txw-parent __noinstall
%mvn_package :jaxb-www __noinstall

%if %{with bootstrap}
%pom_disable_module core
%pom_disable_module codemodel-annotation-compiler codemodel
%pom_disable_module runtime
%pom_disable_module relaxng-datatype external
%pom_disable_module rngom external
%pom_disable_module xjc
%pom_disable_module xsom
%pom_disable_module txw
%endif
popd

%build

pushd jaxb-ri
%mvn_build -s -f -j -- -Dproject.build.sourceEncoding=UTF-8
popd
%install
pushd jaxb-ri
%mvn_install
popd
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jaxb-codemodel -f %{oreon_filedir}/jaxb-codemodel.list
%files -n jaxb-codemodel-annotation-compiler -f %{oreon_filedir}/jaxb-codemodel-annotation-compiler.list
%files -n jaxb-relaxng-datatype -f %{oreon_filedir}/jaxb-relaxng-datatype.list
%files -n jaxb-xsom -f %{oreon_filedir}/jaxb-xsom.list
%files -n jaxb-core -f %{oreon_filedir}/jaxb-core.list
%files -n jaxb-rngom -f %{oreon_filedir}/jaxb-rngom.list
%files -n jaxb-runtime -f %{oreon_filedir}/jaxb-runtime.list
%files -n jaxb-txw2 -f %{oreon_filedir}/jaxb-txw2.list
%files -n jaxb-xjc -f %{oreon_filedir}/jaxb-xjc.list
%files -n jaxb-txwc2 -f %{oreon_filedir}/jaxb-txwc2.list

%changelog

%autochangelog
