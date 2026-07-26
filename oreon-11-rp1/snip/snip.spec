%global source0_hash c5fc7c7c006ce4821cf143d94da29d99e7b6c25db8d3295dc72702bf05f89f33

Name:           snip
Version:        0.11
Release:        31%{?dist}
Summary:        An Ant task designed to help with the single-sourcing of program documentation

# Automatically converted from old format: BSD - review is highly recommended.
License:        LicenseRef-Callaway-BSD
URL:            http://www.martiansoftware.com/lab/snip/
Source0:        http://martiansoftware.com/lab/snip/snip-0.11-src.zip
Patch0:         snip-build.patch

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
#/usr/share/java must be owned: 
Requires:       javapackages-tools

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

%patch -P0 -p0

%build
ant jar javadoc

%install
mkdir -p %{buildroot}%{_javadir}
install -pm  0755 dist/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

mkdir -p %{buildroot}%{_javadocdir}/
mv javadoc/ %{buildroot}%{_javadocdir}/%{name}

%files 
%{_javadir}/%{name}.jar
%doc LICENSE.txt

%files javadoc
%doc LICENSE.txt
%{_javadocdir}/%{name}

%changelog
%autochangelog
