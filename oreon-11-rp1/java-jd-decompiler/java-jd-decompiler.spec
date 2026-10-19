%global source0_hash 98dfdbef1e6ac1814bf5fe4b58027eb655d85b92abf266e957982dd09f7899ba
Name:           java-jd-decompiler
Version:        1.1.3
Release:        1%{?dist}
Summary:        JAVA library having JAVA decompiler of "Java Decompiler project"
License:        GPL-3.0-only
URL:            https://github.com/java-decompiler/jd-core
Source0:        https://github.com/java-decompiler/jd-core/archive/refs/tags/v%{version}.tar.gz
Source1:        pom.xml
Source2:        Main.java
Source3:        java-jd-decompiler
Source4:        java-jd-decompiler.1
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       %{name}-core = %{version}-%{release}
Requires:       javapackages-tools
# oreon:deps
BuildRequires:  java-25-devel
BuildRequires:  maven-jar-plugin
BuildRequires:  maven-local-openjdk25
# /oreon:deps
%description
This is a launcher for using %{name}-core library from CLI

%package        javadoc    
Summary:        Javadoc for %{name} 
%description javadoc    
This package contains the API documentation for %{name}.

%package        core    
Summary:        Main library with decompiler
%description    core
This standalone JAVA library has JAVA decompiler of "Java Decompiler project".
It support Java 1.8.0 to Java 12.0.It has support for the Lambda expressions,
method references and default methods.JD-Core is the engine of JD-GUI.

%global debug_package %{nil}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n jd-core-%{version}
cp %{SOURCE1} pom.xml

%build

%mvn_build -f
javac -d $PWD -cp target/jd-core-%{version}.jar %{SOURCE2}
jar -cvf launcher.jar *.class  
rm -v *.class
%install
%mvn_install
mkdir -p  $RPM_BUILD_ROOT/%{_mandir}/man1
install -d -m 755 $RPM_BUILD_ROOT/%{_bindir}
install -m 755 %{SOURCE3} $RPM_BUILD_ROOT/%{_bindir}
cp -v launcher.jar $RPM_BUILD_ROOT/%{_javadir}/java-jd-decompiler
cp -v %{SOURCE4} $RPM_BUILD_ROOT/%{_mandir}/man1
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n java-jd-decompiler-javadoc -f %{oreon_filedir}/java-jd-decompiler-javadoc.list
%files -n java-jd-decompiler-core -f %{oreon_filedir}/java-jd-decompiler-core.list

%changelog

%autochangelog
