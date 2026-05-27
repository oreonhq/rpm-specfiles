%global source0_hash none

Epoch: 1

%global eclipse_ver 4.23
%global bundle_ver 3.29.0
%global jar_ver %{eclipse_ver}
%global drop R-%{jar_ver}-202203080310

Summary: Eclipse Compiler for Java
Name: ecj
Version: %{eclipse_ver}
Release: 15%{?dist}
URL: https://www.eclipse.org
License: EPL-2.0

Source0: https://download.eclipse.org/eclipse/downloads/drops4/%{drop}/ecjsrc-%{jar_ver}.jar
Source1: https://repo1.maven.org/maven2/org/eclipse/jdt/ecj/%{bundle_ver}/ecj-%{bundle_ver}.pom
# The ecj build does not generate a proper manifest, so use the one from the binary distribution
# Extracted from: https://download.eclipse.org/eclipse/downloads/drops4/%%{drop}/ecj-%%{jar_ver}.jar
Source2: MANIFEST.MF

# Always generate debug info when building RPMs (Andrew Haley)
Patch0: 0001-Always-generate-bytecode-debuginfo.patch

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires: ant-openjdk25 
BuildRequires: javapackages-local-openjdk25
BuildRequires: java-25-devel >= 1:11

# Explicit requires for javapackages-tools since ecj
# uses /usr/share/java-utils/java-functions
Requires:       javapackages-tools

%description
ECJ is the Java bytecode compiler of the Eclipse Platform.  It is also known as
the JDT Core batch compiler.

%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%autosetup -p1 -c -n %{name}-%{eclipse_ver}

# Specify encoding
sed -i -e '/compilerarg/s/Xlint:none/Xlint:none -encoding cp1252/' build.xml

cp %{SOURCE1} pom.xml
mkdir -p scripts/binary/META-INF/
cp %{SOURCE2} scripts/binary/META-INF/MANIFEST.MF

# Aliases
%mvn_alias org.eclipse.jdt:ecj org.eclipse.jdt:core org.eclipse.jdt.core.compiler:ecj \
  org.eclipse.tycho:org.eclipse.jdt.core org.eclipse.tycho:org.eclipse.jdt.compiler.apt

%build
export JAVA_HOME=/usr/lib/jvm/java
ant

%install
%mvn_artifact pom.xml ecj.jar
%mvn_install

# Install the ecj wrapper script
%jpackage_script org.eclipse.jdt.internal.compiler.batch.Main '' '' ecj ecj true

# Install manpage
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 644 -p ecj.1 $RPM_BUILD_ROOT%{_mandir}/man1/ecj.1

%files -f .mfiles
%license about.html
%{_bindir}/ecj
%{_mandir}/man1/ecj*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - %{eclipse_ver}-15
- Prepare for Oreon 11 (RP1)
