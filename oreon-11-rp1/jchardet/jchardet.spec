%global source0_hash 2d83cd7a24a5a5c1cbf02f649008b0d792f5e4bc11e18a7df8ce4f885bc8650a

Name:           jchardet
Version:        1.1
Release:        40%{?dist}
Summary:        Java port of Mozilla's automatic character set detection algorithm

# Automatically converted from old format: MPLv1.1 or GPLv2+ or LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-MPLv1.1 OR GPL-2.0-or-later OR LicenseRef-Callaway-LGPLv2+
URL:            http://jchardet.sourceforge.net/
Source0:        https://download.sourceforge.net/jchardet/%{version}/jchardet-%{version}.zip
Source1:        https://repo1.maven.org/maven2/net/sourceforge/%{name}/%{name}/1.0/%{name}-1.0.pom
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  maven-local-openjdk25

%description
jchardet is a java port of the source from Mozilla's automatic charset
detection algorithm. The original author is Frank Tang. What is available
here is the java port of that code. The original source in C++ can be found
from http://lxr.mozilla.org/mozilla/source/intl/chardet/. More information can
be found at http://www.mozilla.org/projects/intl/chardet.html.

%package javadoc
Summary:    API documentation for %{name}

%description javadoc
%{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

cp %{SOURCE1} pom.xml

# fix up the provided version
%pom_xpath_set /pom:project/pom:version %{version}

# remove hard-coded compiler configuration
%pom_remove_plugin :maven-compiler-plugin

# remove distributionManagement.status from pom (maven stops build
# when it's there)
%pom_xpath_remove pom:distributionManagement

# create proper dir structure
mkdir -p src/main/java/org/mozilla/intl/chardet
mv src/*java src/main/java/org/mozilla/intl/chardet

%build
%mvn_build -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
%autochangelog
