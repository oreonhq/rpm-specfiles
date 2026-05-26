%bcond_with bootstrap

Name:           beust-jcommander
Version:        1.82
Release:        %autorelease
Summary:        Java framework for parsing command line parameters
License:        Apache-2.0
URL:            https://jcommander.org
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# ./generate-tarball.sh
Source0:        https://github.com/cbeust/jcommander/archive/dcf154b6d40dd3865e317de7250b7019044543a9.tar.gz
Source1:        https://repo1.maven.org/maven2/com/beust/jcommander/1.82/jcommander-1.82.pom
# Cleaned up bundled jars whose licensing cannot be easily verified
Source2:        generate-tarball.sh

Patch:          0001-ParseValues-NullPointerException-patch.patch
# oreon url source checksums begin
%global source0_sha256 4adddcef38265d5339ec28a0e34fc2a7c2f59cf7d6fb988b4e56380c0de0f96b
%global source0_file dcf154b6d40dd3865e317de7250b7019044543a9.tar.gz
# oreon url source checksums end

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.testng:testng)
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.82-23

%description
JCommander is a very small Java framework that makes it trivial to
parse command line parameters (with annotations).

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/dcf154b6d40dd3865e317de7250b7019044543a9.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "4adddcef38265d5339ec28a0e34fc2a7c2f59cf7d6fb988b4e56380c0de0f96b" || { echo "oreon: Source0 SHA256 mismatch for dcf154b6d40dd3865e317de7250b7019044543a9.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -p1 -C
chmod -x license.txt

cp -p %SOURCE1 pom.xml
%pom_xpath_set "pom:project/pom:version" "%{version}"

# maven-surefire-plugin requires explicit version >= 4.7
%pom_add_dep org.testng:testng:4.7:test

%mvn_file : %{name}

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license license.txt notice.md
%doc README.markdown

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.82-1
- Import
