%global source0_hash 54cfc962032578d07ffc0a057f1659a8f8585b6da8935288475842f1bed1d647
Name:           rundoc
Version:        0.11
Release:        31%{?dist}
Summary:        An Ant task designed to help with the single-sourcing of program documentation
License:        LicenseRef-Callaway-BSD
URL:            http://www.martiansoftware.com/lab/rundoc/
Source0:        http://martiansoftware.com/lab/rundoc/rundoc-0.11-src.zip
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       javapackages-tools
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  javapackages-local-openjdk25
# /oreon:deps
%description
An Ant task designed to help with the single-sourcing of program documentation.

%package	javadoc
Summary:        Javadocs for %{name}
%description    javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qc -n %{name}-%{version}

rm %{name}-%{version}.jar
rm -rf javadoc/ 

%build

ant jar javadoc
%install
mkdir -p %{buildroot}%{_javadir}
install -pm  0755 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar
mkdir -p %{buildroot}%{_javadocdir}/
mv javadoc/ %{buildroot}%{_javadocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n rundoc-javadoc -f %{oreon_filedir}/rundoc-javadoc.list

%changelog

%autochangelog
