%global source0_hash 12dada19d9554e3133d51f809e67d604e400b4c81ac70149db502de873741ec3
Name:           bsh
Version:        2.1.1
Release:        1%{?dist}
Epoch:          0
Summary:        Lightweight Scripting for Java
URL:            https://beanshell.github.io/
License:        Apache-2.0 AND BSD-3-Clause AND LicenseRef-Public-Domain
Source0:        https://github.com/beanshell/beanshell/archive/refs/tags/2.1.1.tar.gz#/bsh-2.1.1.tar.gz
Patch0:        0000-source-target-1.8.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       bsf
Requires:       java-25-headless
Requires:       jline2
Requires:       javapackages-tools
Provides:       %{name}-utils = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-utils < 0:2.0
Obsoletes:      %{name}-demo < 0:2.0
Provides:       bundled(objectweb-asm) = 1.3.6
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  bsf
BuildRequires:  glassfish-servlet-api
BuildRequires:  javacc
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  junit
# /oreon:deps
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

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n beanshell-%{version}
%patch 0 -p1

sed -i 's,org.apache.xalan.xslt.extensions.Redirect,http://xml.apache.org/xalan/redirect,' docs/manual/xsl/*.xsl

%mvn_alias :bsh bsh:bsh bsh:bsh-bsf org.beanshell:bsh

%mvn_file : %{name}

%build

rm -rf lib
mkdir -p lib
build-jar-repository lib bsf javacc junit glassfish-servlet-api
ant dist
%install
%mvn_artifact pom.xml dist/%{name}-%{version}.jar
%mvn_install -J javadoc
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet.war %{buildroot}%{_datadir}/%{name}/webapps
install -m 644 dist/bshservlet-wbsh.war %{buildroot}%{_datadir}/%{name}/webapps
install -d %{buildroot}%{_bindir}
%jpackage_script bsh.Interpreter "\${BSH_DEBUG:+-Ddebug=true}" jline.console.internal.ConsoleRunner %{name}:jline2/jline %{name} true
%jpackage_script bsh.Console "\${BSH_DEBUG:+-Ddebug=true}" "" bsh bsh-console true
echo '#!%{_bindir}/bsh' > %{buildroot}%{_bindir}/bshdoc
cat scripts/bshdoc.bsh >> %{buildroot}%{_bindir}/bshdoc
%oreon_autofiles bsh-manual usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles bsh-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n bsh-manual -f %{oreon_filedir}/bsh-manual.list
%files -n bsh-javadoc -f %{oreon_filedir}/bsh-javadoc.list

%changelog

%autochangelog
