%global source0_hash 8419e20e58e493f3ec9d545a17053900ea5686c3e3db25e2c9b338f8a3b4e575

Name: hid4java
Version: 0.7.0
Release: 13%{?dist}
Summary: Java wrapper for the hidapi library

License: MIT
URL: https://github.com/gary-rowe/hid4java
Source0: https://github.com/gary-rowe/%{name}/archive/%{name}-%{version}.tar.gz
Patch0: load-correct-library-name.patch
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

Requires: java-25-headless
Requires: hidapi

BuildRequires: maven-local-openjdk25
BuildRequires: mvn(net.java.dev.jna:jna)
BuildRequires: maven-surefire maven-surefire-provider-junit5
BuildRequires: junit5
BuildRequires: apiguardian

%description
hid4java supports USB HID devices through a common API. The API is very simple
but provides great flexibility such as support for feature reports and blocking
reads with timeouts. Attach/detach events are provided to allow applications to
respond instantly to device availability.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}-%{name}-%{version}

%patch -P0 -p1

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.dll' -print -delete

%pom_remove_plugin :maven-source-plugin
%pom_remove_plugin :maven-javadoc-plugin
	
for x in `find | grep pom.xml$` ; do
  if cat $x | grep -e "<source>.*7" -e "<target>.*7" ; then
    sed "s;<source>.*.7.*;<source>8</source>;g" -i $x;
    sed "s;<target>.*7.*;<target>8</target>;g" -i $x;
  fi
done

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc AUTHORS README.md
%license LICENSE

%files javadoc -f .mfiles-javadoc
%doc AUTHORS README.md
%license LICENSE

%changelog
%autochangelog
