%global source0_hash 0fd32a663018a93ef4adaa84d5e2936d1ae9275f7e5bffa252d976f01d213c1e

%global commit f159b88a16be4d103c7e7beb90e07a92617980b9
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global zipcommit %(c=%{commit}; echo ${c:0:12})

Name:           jFormatString
Version:        0
Release:        0.55.20131227git%{shortcommit}%{?dist}
Summary:        Java format string compile-time checker

License:        GPL-2.0-only WITH Classpath-exception-2.0
URL:            http://code.google.com/p/j-format-string/

Source0:        http://j-format-string.googlecode.com/archive/%{commit}.zip
Source1:        http://search.maven.org/remotecontent?filepath=com/google/code/findbugs/jFormatString/2.0.2/jFormatString-2.0.2.pom

# This patch has not been sent upstream, since it is Fedora specific.
Patch0:         %{name}-build.patch

Patch1:         %{name}-java8.patch

BuildRequires:  javapackages-local-openjdk25

BuildRequires:  ant-openjdk25 , java-25-devel, java-javadoc, jpackage-utils, junit
Requires:       java-25-headless, jpackage-utils

BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%description
This project is derived from Sun's implementation of java.util.Formatter.  It
is designed to allow compile time checks as to whether or not a use of a
format string will be erroneous when executed at runtime.

%package javadoc
Summary:        Javadoc documentation for %{name}
Requires:       java-javadoc

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n j-format-string-%{zipcommit}
%patch -P0 -p1
%patch -P1 -p1

cp %{SOURCE1} pom.xml

# delete test code - it requires FindBugs to compile
rm -rfv src/junit

# delete JARs
rm -v lib/*

%mvn_file com.google.code.findbugs:%{name} %{name}

%build
# Build the JAR
ant jarFile

# Create the javadocs
mkdir docs
javadoc -d docs -source 1.8 -sourcepath src/java \
  -classpath build/classes \
  -link file://%{_javadocdir}/java edu.umd.cs.findbugs.formatStringChecker

%mvn_artifact pom.xml build/%{name}.jar

%install

%mvn_install -J docs

%pretrans javadoc -p <lua>
path = "%{_javadocdir}/%{name}"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%files -f .mfiles

%files javadoc -f .mfiles-javadoc

%changelog
%autochangelog
