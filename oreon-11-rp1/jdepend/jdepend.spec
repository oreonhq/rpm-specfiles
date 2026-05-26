Name:           jdepend
Version:        2.10
Release:        %autorelease
Summary:        Java Design Quality Metrics
License:        MIT
URL:            https://github.com/clarkware/jdepend
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/clarkware/jdepend/archive/refs/tags/2.10.tar.gz#/jdepend-2.10.tar.gz
# oreon url source checksums begin
%global source0_sha256 8c19f5d62127c11c20976ae130d1914a64f0115e5113810c38fe53bf8715378b
%global source0_file 2.10.tar.gz
# oreon url source checksums end

BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 2.10-27

%description
JDepend traverses a set of Java class and source file directories and
generates design quality metrics for each Java package. JDepend allows
you to automatically measure the quality of a design in terms of its
extensibility, reusability, and maintainability to effectively manage
and control package dependencies.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/2.10.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "8c19f5d62127c11c20976ae130d1914a64f0115e5113810c38fe53bf8715378b" || { echo "oreon: Source0 SHA256 mismatch for 2.10.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1
# remove all binary libs
find . -name "*.jar" -delete
# fix strange permissions
find . -type d -exec chmod 755 {} \;
find . -type f -exec chmod 644 {} \;

%mvn_file %{name}:%{name} %{name}

%build
%ant -Dant.build.javac.source=1.8 -Dant.build.javac.target=1.8 jar

%install
%mvn_artifact jdepend:jdepend:%{version} dist/%{name}-%{version}.jar
%mvn_install

%files -f .mfiles
%doc README.md CHANGELOG.md docs
%license LICENSE.md

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.10-1
- Prepare for Oreon 11 (RP1)
