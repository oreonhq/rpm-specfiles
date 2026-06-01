%global source0_hash ed25f020c3eedad02d7bea4ce9fd845ca312e7433ddfa6405769502c3353dab2

%bcond_with bootstrap
%global pkg_version 11b

Name:           java_cup
Epoch:          1
Version:        0.11b
Release:        %autorelease
Summary:        LALR parser generator for Java
License:        SMLNJ
URL:            https://www2.cs.tum.edu/projects/cup/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/DrMichaelPetter/cup/archive/c35ed3ab0cde2310af9b01321c930349c7c797e2.tar.gz#/java_cup-%{version}.tar.gz
# Add OSGi manifests
Source2:        %{name}-MANIFEST.MF
Source4:        %{name}-runtime-MANIFEST.MF

Patch:          0001-Adopt-build-script.patch

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
BuildRequires:  java_cup
BuildRequires:  jflex
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1:0.11b-57

%description
java_cup is a LALR Parser Generator for Java

%package manual
Summary:        Documentation for java_cup

%description manual
Documentation for java_cup.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -p1 -n cup-c35ed3ab0cde2310af9b01321c930349c7c797e2

# remove all binary files
find -name "*.class" -delete

%mvn_file ':{*}' @1

# remove prebuilt JFlex
rm -rf bin/JFlex.jar

# remove prebuilt java_cup, if not bootstrapping
rm -rf bin/java-cup-11.jar

%build
export CLASSPATH=$(build-classpath java_cup java_cup-runtime jflex)

%ant -Dcupversion=20150326 -Dsvnversion=65

# inject OSGi manifests
%jar ufm dist/java-cup-%{pkg_version}.jar %{SOURCE2}
%jar ufm dist/java-cup-%{pkg_version}-runtime.jar %{SOURCE4}

%install
%mvn_artifact %{name}:%{name}:%{version} dist/java-cup-%{pkg_version}.jar
%mvn_artifact %{name}:%{name}-runtime:%{version} dist/java-cup-%{pkg_version}-runtime.jar

%mvn_install

# wrapper script for direct execution
%jpackage_script java_cup.Main "" "" java_cup cup true

%files -f .mfiles
%{_bindir}/cup
%doc changelog.txt
%license licence.txt

%files manual
%doc manual.html
%license licence.txt

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1:0.11b-1
- Import
