%global source0_hash 0b20c57708a7e98c70b400749c7bdf5c028d4e352e4ed0b0750004df793dfa90

# Copyright (c) 2000-2007, JPackage Project
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

Name:           bsh
Version:        2.1.0
Release:        19%{?dist}
Epoch:          0
Summary:        Lightweight Scripting for Java
URL:            https://beanshell.github.io/
# bundled asm is BSD
# bsf/src/bsh/util/BeanShellBSFEngine.java is public-domain
License:        Apache-2.0 AND BSD-3-Clause AND LicenseRef-Public-Domain

# ./generate-tarball.sh
Source0:        https://github.com/beanshell/beanshell/archive/refs/tags/2.1.0.tar.gz

# Remove bundled jars which cannot be easily verified for licensing
# Remove code marked as SUN PROPRIETARY/CONFIDENTAIL
Source2:        generate-tarball.sh

# compatibility with Java 11:
# - set javac / javadoc source and target values to 1.8
Patch0:         0000-source-target-1.8.patch
# - remove references to invisible symbols and methods
Patch1:         0001-java-11-compatibility.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant-openjdk25 
BuildRequires:  bsf
BuildRequires:  glassfish-servlet-api
BuildRequires:  javacc
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  junit

Requires:       bsf
Requires:       java-25-headless
Requires:       jline2

# Explicit javapackages-tools requires since scripts use
# /usr/share/java-utils/java-functions
Requires:       javapackages-tools

Provides:       %{name}-utils = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-utils < 0:2.0
Obsoletes:      %{name}-demo < 0:2.0

# bsh uses small subset of modified (shaded) classes from ancient version of
# objecweb-asm under asm directory
Provides:       bundled(objectweb-asm) = 1.3.6

%description
BeanShell is a small, free, embeddable, Java source interpreter with
object scripting language features, written in Java. BeanShell
executes standard Java statements and expressions, in addition to
obvious scripting commands and syntax. BeanShell supports scripted
objects as simple method closures like those in Perl and
JavaScript(tm). You can use BeanShell interactively for Java
experimentation and debugging or as a simple scripting engine for your
applications. In short: BeanShell is a dynamically interpreted Java,
plus some useful stuff. Another way to describe it is to say that in
many ways BeanShell is to Java as Tcl/Tk is to C: BeanShell is
embeddable - You can call BeanShell from your Java applications to
execute Java code dynamically at run-time or to provide scripting
extensibility for your applications. Alternatively, you can call your
Java applications and objects from BeanShell; working with Java
objects and APIs dynamically. Since BeanShell is written in Java and
runs in the same space as your application, you can freely pass
references to "real live" objects into scripts and return them as
results.

%package manual
Summary:        Manual for %{name}

%description manual
Documentation for %{name}.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
This package provides %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n beanshell-%{version}
%patch 0 -p1
%patch 1 -p1

sed -i 's,org.apache.xalan.xslt.extensions.Redirect,http://xml.apache.org/xalan/redirect,' docs/manual/xsl/*.xsl

%mvn_alias :bsh bsh:bsh bsh:bsh-bsf org.beanshell:bsh

%mvn_file : %{name}

%build
mkdir lib
build-jar-repository lib bsf javacc junit glassfish-servlet-api

ant test dist

%install
%mvn_artifact pom.xml dist/%{name}-%{version}.jar

%mvn_install -J javadoc

install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet.war %{buildroot}%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet-wbsh.war %{buildroot}%{_datadir}/%{name}/webapps

# scripts
install -d %{buildroot}%{_bindir}

%jpackage_script bsh.Interpreter "\${BSH_DEBUG:+-Ddebug=true}" jline.console.internal.ConsoleRunner %{name}:jline2/jline %{name} true
%jpackage_script bsh.Console "\${BSH_DEBUG:+-Ddebug=true}" "" bsh bsh-console true

echo '#!%{_bindir}/bsh' > %{buildroot}%{_bindir}/bshdoc
cat scripts/bshdoc.bsh >> %{buildroot}%{_bindir}/bshdoc

%files -f .mfiles
%license LICENSE NOTICE
%doc README.md src/Changes.html src/CodeMap.html docs/faq/faq.html

%attr(0755,root,root) %{_bindir}/%{name}*
%{_datadir}/%{name}/

%files manual
%doc docs/manual/html
%doc docs/manual/images/*.jpg
%doc docs/manual/images/*.gif
%license LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%license LICENSE NOTICE

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0:2.1.0-19
- Import
