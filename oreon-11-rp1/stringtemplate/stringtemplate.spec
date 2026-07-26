%global source0_hash 3a0adbb7510c2822ca515c635e1ff1469b3ac78f6d2072e48478876b9191de20

Summary: A Java template engine
Name: stringtemplate
Version: 3.2.1
Release: 41%{?dist}
License: BSD-3-Clause
URL: http://www.stringtemplate.org/
Source0: http://www.stringtemplate.org/download/stringtemplate-%{version}.tar.gz
# Build jUnit tests + make the antlr2 generated code before preparing sources
Patch0: stringtemplate-3.1-build-junit.patch
# With JDK 21 and later, StringTemplate is a name in java.lang, which makes a
# bar instance of the StringTemplate name ambiguous.  Only use the name fully
# qualified to eliminate the ambiguity.
Patch1: stringtemplate-3.2.1-ambiguity.patch
# Update deprecated uses of "new Integer" and "new Boolean"
Patch2: stringtemplate-3.2.1-deprecated.patch

BuildRequires: ant-openjdk25 
BuildRequires: ant-antlr
BuildRequires: ant-junit
BuildRequires: javapackages-local-openjdk25

BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch

%description
StringTemplate is a java template engine (with ports for 
C# and Python) for generating source code, web pages,
emails, or any other formatted text output. StringTemplate
is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package        javadoc
Summary:        API documentation for %{name}
Requires:       java-javadoc

%description    javadoc
API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p0
sed -i -e 's/source="1.4"/source="1.8"/g' build.xml
sed -i -e 's/target="1.4"/target="1.8"/g' build.xml

%build
rm -rf lib target
ant jar
ant javadocs -Dpackages= -Djavadocs.additionalparam="-Xdoclint:none"

%install
%mvn_artifact pom.xml build/%{name}.jar
%mvn_file : %{name}
%mvn_install -J docs/api/

%files -f .mfiles
%license LICENSE.txt
%doc README.txt

%files javadoc
%license LICENSE.txt
%{_javadocdir}/%{name}

%changelog
%autochangelog
