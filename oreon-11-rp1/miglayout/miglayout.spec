%global source0_hash 2f9fc839ac5cf501127d6128bc4f04e6a0adde960628dca1053dbdff29164ce9

Name:           miglayout
Version:        5.3
Release:        6%{?dist}
Summary:        Versatile and flexible Swing layout manager
URL:            http://www.miglayout.com/
# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD

# Hidden in maven.org labyrinth, so no download URL's
Source0:        miglayout-core-%{version}-sources.jar
Source1:        miglayout-swing-%{version}-sources.jar

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires:  java-25-devel

Requires:       java-25
# We no longer have an examples sub-package, note no provides as the examples
# are no longer packaged, so we do not provide them
Obsoletes:      %{name}-examples < %{version}-%{release}

%description
MiGLayout is a versatile Swing layout manager.  It uses String or
API type-checked constraints to format the layout. MiGLayout can
produce flowing, grid based, absolute (with links), grouped and
docking layouts. MiGLayout is created to be to manually coded layouts
what Matisse/GroupLayout is to IDE supported visual layouts.

%package javadoc
Summary:        Javadocs for MiGLayout

%description javadoc
This package contains the API documentation for MiGLayout.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}
unzip -oq %{SOURCE1}

%build
javac -encoding utf8 net/miginfocom/{layout,swing}/*.java

jar cmf META-INF/MANIFEST.MF %{name}-core.jar net/miginfocom/layout/*.class
jar cmf META-INF/MANIFEST.MF %{name}-swing.jar net/miginfocom/swing/*.class
javadoc -Xdoclint:none -d doc net.miginfocom.{layout,swing}

%install
mkdir -p %{buildroot}%{_javadir}
mkdir -p %{buildroot}%{_javadocdir}
cp -a %{name}-*.jar %{buildroot}%{_javadir}
cp -a doc %{buildroot}%{_javadocdir}/%{name}

%files
%{_javadir}/*.jar

%files javadoc
%doc %{_javadocdir}/%{name}

%changelog
%autochangelog
