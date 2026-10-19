%global source0_hash 83da656205fe9cae8fc17aaff71237836acac582a88116c7579e362126bd0ec4
Name:           jzlib
Version:        1.1.3
Release:        1%{?dist}
Summary:        Re-implementation of zlib in pure Java
License:        BSD-3-Clause
URL:            http://www.jcraft.com/jzlib/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/ymnk/jzlib/archive/refs/tags/%{version}.tar.gz#/jzlib-1.1.3.tar.gz
Patch:          jzlib-javadoc-fixes.patch
Obsoletes:      %{name}-javadoc < 1.1.3-37
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
# /oreon:deps
%description
The zlib is designed to be a free, general-purpose, legally unencumbered 
-- that is, not covered by any patents -- loss-less data-compression 
library for use on virtually any computer hardware and operating system. 
The zlib was written by Jean-loup Gailly (compression) and Mark Adler 
(decompression). 

%package demo
Summary:        Examples for %{name}
Requires:       %{name} = %{version}-%{release}
%description demo
%{summary}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1

%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:source" 1.8
%pom_xpath_set "pom:plugin[pom:artifactId='maven-compiler-plugin']/pom:configuration/pom:target" 1.8

# Make into OSGi bundle
%pom_xpath_inject "pom:project" "<packaging>bundle</packaging>"
%pom_add_plugin "org.apache.felix:maven-bundle-plugin" . "<extensions>true</extensions>"

%mvn_file : %{name}

%build

%mvn_build -j
%install
%mvn_install
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -pr example/* %{buildroot}%{_datadir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n jzlib-demo -f %{oreon_filedir}/jzlib-demo.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-1
- Prepare for Oreon 11 (RP1)
