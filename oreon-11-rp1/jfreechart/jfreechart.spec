%global source0_hash 02370e037950fee2e15f61d163b9b5c641e2438a4b110ff112f948ceff57d36a

Name:           jfreechart
Version:        1.5.4
Release:        11%{?dist}
Summary:        A 2D chart library for Java applications (JavaFX, Swing or server-side)
# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            https://www.jfree.org/jfreechart
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jfree/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(javax.servlet:servlet-api)
# need apiguardian-api until Fedora releases junit >= 5.8.0 (1)
# link:
# https://junit.org/junit5/docs/5.8.0/release-notes/index.html#deprecations-and-breaking-changes
# https://junit.org/junit5/docs/5.8.0/release-notes/index.html#new-features-and-improvements
BuildRequires:  mvn(org.apiguardian:apiguardian-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-engine)

%description
JFreeChart is a comprehensive free chart library for the Java platform that can
be used on the client-side (JavaFX and Swing) or the server side (with export to
multiple formats including SVG, PNG and PDF).

%{?javadoc_package}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# (1)
%pom_add_dep org.apiguardian:apiguardian-api:1.1.1

%build
%mvn_build -f -- -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%license licence-LGPL.txt
%doc README.md

%changelog
%autochangelog
