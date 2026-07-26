%global source0_hash d32c53e48471d7de1d097fe199a3df765472cc8d872315d4caf9934833573c93

Name:           vecmath1.2
Version:        1.14
Release:        41%{?dist}
Summary:        Free version of vecmath from the Java3D 1.2 specification
License:        MIT
URL:            http://www.objectclub.jp/download/vecmath_e
Source0:        http://www.objectclub.jp/download/files/vecmath//%{name}-%{version}.tar.gz
Patch0:         vecmath1.2-1.14-javadoc-fixes.patch
Patch1:         vecmath1.2-1.14-javac-1.8.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
BuildRequires: make
BuildRequires:  java-25-devel >= 1:1.6.0
Requires:       java-25-headless >= 1:1.6.0
Requires:       javapackages-filesystem
# Necessary due to architecture change to noarch
Obsoletes:      %{name} < %{version}-%{release}

%description
This is an unofficial implementation (java source code) of the javax.vecmath
package specified in the Java(TM) 3D API 1.2 . The package includes classes
for 3-space vector/point, 4-space vector, 4x4, 3x3 matrix, quaternion,
axis-angle combination and etc. which are often utilized for computer graphics
mathematics. Most of the classes have single and double precision versions.
Generic matrices' LU and SV decomposition are also there.

%package javadoc
Summary:        Javadoc for %{name}
# Necessary due to architecture change to noarch
Obsoletes:      %{name}-javadoc < %{version}-%{release}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1
find -name *.jar -delete
find -name *.class -delete

%build
make -f Makefile.unix all docs
pushd classes
jar cf ../%{name}.jar .
popd

%install
# jar
install -D -m 644 %{name}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
mkdir -p $RPM_BUILD_ROOT%{_javadocdir}/%{name}/
cp -r docs/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}/

%files
%doc README CHANGES
%{_javadir}/%{name}.jar

%files javadoc
%{_javadocdir}/%{name}/

%changelog
%autochangelog
