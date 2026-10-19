%global source0_hash 011d13d26c7f70392a00aa5c47faa6813fcab160e0e031e71652f33589ff9dfd
Name:      brazil
Version:   2.3
Release:        43%{?dist}
Summary:        Extremely small footprint Java HTTP stack
License:   SPL-1.0
URL:       https://github.com/mbooth101/brazil
Source0:        https://github.com/mbooth101/brazil/archive/%{name}-%{version}.tar.gz
Source2:   brazil-build.xml
Patch0:   jdk17.patch
BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch
Requires:         java-25-headless
Requires:         jpackage-utils
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
# /oreon:deps
%description
Brazil is as an extremely small footprint HTTP stack and flexible architecture 
for adding URL-based interfaces to arbitrary applications and devices from Sun 
Labs. This package contains the core set of classes that are not dependent on 
any other external Java libraries.

%package javadoc
Summary:   Java-docs for %{name}
%description javadoc
API documentation for %{name}.

%package demo
Summary:   Demos for %{name}
Requires:  %{name} = %{version}-%{release}
Requires:  tcl
%description demo
Demonstrations and samples for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}

%patch -P0 -p1
 
# fix permissions and interpreter in sample scripts
grep -lR -e ^\#\!/usr/sfw/bin/tclsh8.3 samples | xargs sed --in-place "s|/usr/sfw/bin/tclsh8.3|/usr/bin/tclsh|"
grep -lR -e ^\#\!/usr/bin/tclsh        samples | xargs chmod 755
grep -lR -e ^\#\!/bin/sh               samples | xargs chmod 755

%build

cp -p %{SOURCE2} build.xml
ant all
%install
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}
%oreon_autofiles brazil-javadoc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles brazil-demo usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n brazil-javadoc -f %{oreon_filedir}/brazil-javadoc.list
%files -n brazil-demo -f %{oreon_filedir}/brazil-demo.list

%changelog

%autochangelog
