%global source0_hash none

Name:             jtidy
Version:          1.0
Release:          0.50.20100930svn1125%{?dist}
Epoch:            2
Summary:          HTML syntax checker and pretty printer
License:          zlib
URL:              http://jtidy.sourceforge.net/
# svn export -r1125 https://jtidy.svn.sourceforge.net/svnroot/jtidy/trunk/jtidy/ jtidy
# tar caf jtidy.tar.xz jtidy
Source0:        https://github.com/jtidy/jtidy/archive/svn-r1125.tar.gz#/jtidy-1.0.tar.gz
Source1:        jtidy.jtidy.script

Patch0:           javac-1.8.patch

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:    javapackages-local-openjdk25
BuildRequires:    ant-openjdk25 
BuildRequires:    mvn(xerces:dom3-xml-apis)
# Explicit javapackages-tools requires since jtidy script uses
# /usr/share/java-utils/java-functions
Requires:         javapackages-tools

%description
JTidy is a Java port of HTML Tidy, a HTML syntax checker and pretty
printer.  Like its non-Java cousin, JTidy can be used as a tool for
cleaning up malformed and faulty HTML.  In addition, JTidy provides a
DOM interface to the document that is being processed, which
effectively makes you able to use JTidy as a DOM parser for real-world
HTML.

%package javadoc
Summary:          API documentation for %{name}

%description javadoc
This package contains %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n jtidy-svn-r1125
%patch -P0 -p1

%build
ant

%install
%mvn_file : %{name}
%mvn_alias : net.sf.jtidy:%{name}
%mvn_artifact pom.xml target/%{name}-*.jar

%mvn_install -J target/javadoc

# shell script
mkdir -p %{buildroot}%{_bindir}
cp -ap %{SOURCE1} %{buildroot}%{_bindir}/%{name}

# ant.d
mkdir -p %{buildroot}%{_sysconfdir}/ant.d
cat > %{buildroot}%{_sysconfdir}/ant.d/%{name} << EOF
jtidy
EOF


%files -f .mfiles
%license LICENSE.txt
%attr(755, root, root) %{_bindir}/*
%config(noreplace) %{_sysconfdir}/ant.d/%{name}

%files javadoc -f .mfiles-javadoc
%license LICENSE.txt


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2:1.0-0.50.20100930svn1125
- Import
