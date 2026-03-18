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

Name:           dom4j
Version:        2.1.4
Release:        5%{?dist}
Epoch:          0
Summary:        Open Source XML framework for Java
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            https://dom4j.github.io/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/dom4j/dom4j/archive/version-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/org/%{name}/%{name}/%{version}/%{name}-%{version}.pom

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(jaxen:jaxen)
BuildRequires:  mvn(javax.xml.bind:jaxb-api)

# Test deps
BuildRequires:  mvn(org.testng:testng)
BuildRequires:  mvn(xerces:xercesImpl)
BuildRequires:  mvn(xalan:xalan)
BuildRequires:  mvn(xalan:serializer)

%description
dom4j is an Open Source XML framework for Java. dom4j allows you to read,
write, navigate, create and modify XML documents. dom4j integrates with
DOM and SAX and is seamlessly integrated with full XPath support.

%package javadoc
Summary:        Javadoc for %{name}

%description javadoc
Javadoc for %{name}.


%prep
%autosetup -p1 -n %{name}-version-%{version}

%mvn_alias org.%{name}:%{name} %{name}:%{name}
%mvn_file : %{name}/%{name} %{name}

cp %{SOURCE1} pom.xml
sed -i 's/runtime/compile/' pom.xml

# test deps missing from pom
%pom_add_dep xalan:xalan::test
%pom_add_dep org.testng:testng:6.8.21:test
%pom_add_dep xerces:xercesImpl::test
%pom_add_dep xalan:serializer

# Remove support for code which depends on ancient / deprecated classes
# xpp2 (deprecated and not developed since 2003)
rm -r src/main/java/org/dom4j/xpp
rm src/main/java/org/dom4j/io/XPPReader.java
# The datatype code depends on msv (deprecated and not developed since 2013)
rm -r src/main/java/org/dom4j/datatype
rm -r src/test/java/org/dom4j/datatype
%pom_remove_dep net.java.dev.msv:xsdlib

# dom4j supports multiple parsers, remove support for unpackaged parsers
rm src/main/java/org/dom4j/io/XPP3Reader.java
rm src/test/java/org/dom4j/io/XPP3ReaderTest.java
%pom_remove_dep xpp3:xpp3
%pom_remove_dep pull-parser:pull-parser
%pom_remove_dep javax.xml.stream:stax-api

# Remove non-deterministic tests
rm src/test/java/org/dom4j/ThreadingTest.java
rm src/test/java/org/dom4j/util/PerThreadSingletonTest.java


%build
%mvn_build -- -Dproject.build.sourceEncoding=UTF-8 -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8


%install
%mvn_install


%files -f .mfiles
%license LICENSE
%doc README.md

%files javadoc -f .mfiles-javadoc
%license LICENSE


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.1.4-5
- Prepare for Oreon 11 (RP1)
