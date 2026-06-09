%global source0_hash e6ef91d439ada9045f419c77543ebe0416c3cdfc5b063448343417a3e4a72123

%bcond_with bootstrap

Name:           aopalliance
Version:        1.0
Release:        %autorelease
Summary:        Java/J2EE AOP standards
License:        LicenseRef-Public-Domain
URL:            https://aopalliance.sourceforge.net
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

# cvs -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance login
# password empty
# cvs -z3 -d:pserver:anonymous@aopalliance.cvs.sourceforge.net:/cvsroot/aopalliance export -r HEAD aopalliance
Source0:        https://repo1.maven.org/maven2/aopalliance/aopalliance/%{version}/aopalliance-%{version}-sources.jar
Source1:        https://repo1.maven.org/maven2/aopalliance/aopalliance/%{version}/aopalliance-%{version}.pom
Source2:        %{name}-MANIFEST.MF

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  javapackages-local-openjdk25
BuildRequires:  ant-openjdk25 
%endif
# TODO Remove in Fedora 46
Obsoletes:      %{name}-javadoc < 1.0-56

%description
Aspect-Oriented Programming (AOP) offers a better solution to many
problems than do existing technologies, such as EJB.  AOP Alliance
intends to facilitate and standardize the use of AOP to enhance
existing middleware environments (such as J2EE), or development
environements (e.g. Eclipse).  The AOP Alliance also aims to ensure
interoperability between Java/J2EE AOP implementations to build a
larger AOP community.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f"  | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -n %{name}

%build
mkdir -p build/classes
javac -source 1.8 -target 1.8 -d build/classes $(find org -name '*.java')
jar cf build/%{name}.jar -C build/classes .

# Inject OSGi manifest required by Eclipse.
%jar umf %{SOURCE2} build/%{name}.jar

%install
%mvn_file : %{name}
%mvn_artifact %{SOURCE1} build/%{name}.jar

%mvn_install

%files -f .mfiles

%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.0-1
- Import
