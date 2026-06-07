%global source0_hash f2f69d770b86cb5c26b5e0a4f4f0f09ecbf31f5774ed66d032f10ee1424a17d6

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
#    distributio4.3n.
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

Name:           tagsoup
Version:        1.2.1
Release:        38%{?dist}
Epoch:          0
Summary:        A SAX-compliant HTML parser written in Java 
# AFL/GPLv2+ license for src/java/org/ccil/cowan/tagsoup/PYXScanner.java is
# likely mixup of upstream but needs to be cleared up
# Automatically converted from old format: ASL 2.0 and (GPLv2+ or AFL) - review is highly recommended.
License:        Apache-2.0 AND (GPL-2.0-or-later OR LicenseRef-Callaway-AFL)
Source0:        https://repo1.maven.org/maven2/org/ccil/cowan/tagsoup/tagsoup/%{version}/tagsoup-%{version}-sources.jar#/tagsoup-%{version}-src.zip
URL:            https://home.ccil.org/~cowan/XML/tagsoup/
Source1:        https://repo1.maven.org/maven2/org/ccil/cowan/tagsoup/tagsoup/%{version}/tagsoup-%{version}.pom
BuildRequires:  javapackages-local-openjdk25

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
TagSoup is a SAX-compliant parser written in Java that, instead of
parsing well-formed or valid XML, parses HTML as it is found in the wild: nasty
and brutish, though quite often far from short. TagSoup is designed for people
who have to process this stuff using some semblance of a rational application
design. By providing a SAX interface, it allows standard XML tools to be
applied to even the worst HTML.

%package javadoc
Summary:       Javadoc for %{name}
Requires:      jpackage-utils >= 0:1.6

%description javadoc
Javadoc for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c

find . -name '*.class' -delete
find . -name "*.jar" -delete

%build
mkdir -p build/classes build/docs
javac --release 8 -d build/classes $(find org -name '*.java')
jar --create --file build/%{name}-%{version}.jar -C build/classes .
javadoc --release 8 -quiet -Xdoclint:none -d build/docs $(find org -name '*.java')

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE1} build/%{name}-%{version}.jar

%mvn_install

%files -f .mfiles

%files javadoc
%doc build/docs

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0:1.2.1-38
- Import
