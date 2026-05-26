Name:           jzlib
Version:        1.1.3
Release:        %autorelease
Summary:        Re-implementation of zlib in pure Java
License:        BSD-3-Clause
URL:            http://www.jcraft.com/jzlib/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/ymnk/jzlib/archive/%{version}.tar.gz

# This patch is sent upstream: https://github.com/ymnk/jzlib/pull/15
Patch:          jzlib-javadoc-fixes.patch
# oreon url source checksums begin
%global source0_sha256 83da656205fe9cae8fc17aaff71237836acac582a88116c7579e362126bd0ec4
%global source0_file 1.1.3.tar.gz
# oreon url source checksums end

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.1.3-37

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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/1.1.3.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "83da656205fe9cae8fc17aaff71237836acac582a88116c7579e362126bd0ec4" || { echo "oreon: Source0 SHA256 mismatch for 1.1.3.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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

# examples
install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -pr example/* %{buildroot}%{_datadir}/%{name}

%files -f .mfiles
%license LICENSE.txt

%files demo
%doc %{_datadir}/%{name}

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.1.3-1
- Prepare for Oreon 11 (RP1)
