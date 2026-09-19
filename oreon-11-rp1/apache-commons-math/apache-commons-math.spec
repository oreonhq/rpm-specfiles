%global source0_hash 46171449bcfb7d76912275ed1af9ef7de03f7eb1cb9a801e3faf304cc8f586a6

%global short_name commons-math3

Name:             apache-commons-math
Version:          3.6.1
Release:          25%{?dist}
Summary:          Java library of lightweight mathematics and statistics components
# Automatically converted from old format: ASL 1.1 and ASL 2.0 and BSD - review is highly recommended.
License:          Apache-1.1 AND Apache-2.0 AND LicenseRef-Callaway-BSD
URL:              http://commons.apache.org/math/
Source0:          http://www.apache.org/dist/commons/math/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:    maven-local-openjdk25
BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.apache.commons:commons-parent:pom:)
BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

%description
Commons Math is a library of lightweight, self-contained mathematics and
statistics components addressing the most common problems not available in the
Java programming language or Commons Lang.

%package javadoc
Summary:          Javadoc for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{short_name}-%{version}-src -p1

# Skip test that fails on Java 11
sed -i -e '/checkMissingFastMathClasses/i@Ignore' \
src/test/java/org/apache/commons/math3/util/FastMathTest.java

# Compatibility links
%mvn_alias "org.apache.commons:%{short_name}" "%{short_name}:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build -- -Dcommons.packageId=math3

%install
%mvn_install

%files -f .mfiles
%doc NOTICE.txt RELEASE-NOTES.txt
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc
%doc NOTICE.txt
%license LICENSE.txt

%changelog
%autochangelog
