%global source0_hash 011d13d26c7f70392a00aa5c47faa6813fcab160e0e031e71652f33589ff9dfd

Name:      brazil
Version:   2.3
Release:   43%{?dist}
Summary:   Extremely small footprint Java HTTP stack
License:   SPL-1.0
URL:       https://github.com/mbooth101/brazil

Source0:   https://github.com/mbooth101/brazil/archive/%{name}-%{version}.tar.gz

# upsteam's build script doesn't build javadocs, so use our own, better script - it is not better, pls fix upstream pom.xm!
Source2:   brazil-build.xml

# https://github.com/mbooth101/brazil/pull/1
Patch0:   jdk17.patch

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:    java-25-devel
BuildRequires:    jpackage-utils
BuildRequires:    ant-openjdk25 
Requires:         java-25-headless
Requires:         jpackage-utils

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
# jars
mkdir -p %{buildroot}%{_javadir}
cp -p build/%{name}.jar %{buildroot}%{_javadir}/%{name}.jar

# javadoc
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -pr build/javadoc/* %{buildroot}%{_javadocdir}/%{name}

# samples
mkdir -p %{buildroot}%{_datadir}/%{name}
cp -pr samples %{buildroot}%{_datadir}/%{name}

%files
%doc README.md srcs/license.terms
%{_javadir}/%{name}.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%files demo
%doc %{_datadir}/%{name}/samples/README
%{_datadir}/%{name}

%changelog
%autochangelog
