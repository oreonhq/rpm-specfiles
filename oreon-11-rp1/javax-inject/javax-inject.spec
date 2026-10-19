%global source0_hash aa437908aa6b50f2a6fe30bade6495ab1195c3ec4d7708a66afc97f2edeee766
%global source1_hash 943e12b100627804638fa285805a0ab788a680266531e650921ebfe4621a8bfa
Name:           javax-inject
Version:        1
Release:        1%{?dist}
Summary:        Dependency injection API for Java
License:        Apache-2.0
URL:            https://github.com/javax-inject/javax-inject
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/javax-inject/javax-inject/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://repo1.maven.org/maven2/javax/inject/javax.inject/%{version}/javax.inject-%{version}.pom
Provides:       mvn(javax.inject:javax.inject) = %{version}
# oreon:deps
BuildRequires:  java-25-openjdk-devel
# /oreon:deps
%description
The javax.inject API defines the core annotations used for dependency
injection in Java.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
test "%{source1_hash}" = "none" || { f="%{SOURCE1}"; test -f "$f" || { echo "oreon: missing Source1 $f" >&2; exit 1; }; h=$(sha256sum "$f" | cut -d' ' -f1); test "$h" = "%{source1_hash}" || { echo "oreon: Source1 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}-%{version}
%oreon_prep
%build

mkdir -p classes
javac --release 8 -d classes $(find src -name '*.java')
jar --create --file %{name}.jar -C classes javax
%install
mkdir -p %{buildroot}%{_javadir}/javax.inject
install -m 0644 %{name}.jar %{buildroot}%{_javadir}/javax.inject/javax.inject.jar
mkdir -p %{buildroot}%{_mavenpomdir}/javax.inject
install -m 0644 %{SOURCE1} %{buildroot}%{_mavenpomdir}/javax.inject/javax.inject.pom
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
