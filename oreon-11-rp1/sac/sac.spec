Name: sac
Version: 1.3
Release: 51%{?dist}
Summary: Java standard interface for CSS parser
License: W3C
#Original source: http://www.w3.org/2002/06/%%{name}java-%%{version}.zip
#unzip, find . -name "*.jar" -exec rm {} \;
#to simplify the licensing
Source0: %{name}java-%{version}-jarsdeleted.zip
Source1: %{name}-build.xml
Source2: %{name}-MANIFEST.MF
Source3: https://repo1.maven.org/maven2/org/w3c/css/sac/1.3/sac-1.3.pom
URL: http://www.w3.org/Style/CSS/SAC/

%if 0%{?fedora}
BuildRequires: ant-openjdk25 
BuildRequires: javapackages-local-openjdk25
%else
BuildRequires: ant-openjdk21
BuildRequires: javapackages-local-openjdk21
%endif

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

%description
SAC is a standard interface for CSS parsers, intended to work with CSS1, CSS2,
CSS3 and other CSS derived languages.

%package javadoc
Summary: Javadoc for %{name}

%description javadoc
Javadoc for %{name}.

%prep
%setup -q
install -m 644 %{SOURCE1} build.xml
find . -name "*.jar" -exec rm -f {} \;

%build
ant jar javadoc

# inject OSGi manifest
jar ufm build/lib/sac.jar %{SOURCE2}

%install
%mvn_artifact %{SOURCE3} build/lib/sac.jar
%mvn_file ":sac" sac
%mvn_install -J build/api

%files -f .mfiles
%license COPYRIGHT.html

%files javadoc -f .mfiles-javadoc
%license COPYRIGHT.html

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.3-51
- Prepare for Oreon 11 (RP1)
