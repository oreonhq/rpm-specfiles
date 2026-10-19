%global source0_hash 5f57508ee516009532b215a209ae0ae887e15a8ec05916a3a13f1b1dce348425
Name: java-scrypt
Version: 1.4.0
Release:        1%{?dist}
Summary:        Java implementation of scrypt
License: Apache-2.0
URL: https://github.com/wg/scrypt
Source0:        https://github.com/wg/scrypt/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0: no-jni.patch
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
# /oreon:deps
%description
A pure Java implementation of the scrypt key derivation function.

%package javadoc
Summary: Javadoc for %{name}
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n scrypt-%{version}
%patch -P0 -p1

%pom_remove_plugin :maven-compiler-plugin

find -name '*.so' -print -delete
find -name '*.dylib' -print -delete
find -name '*.jar' -print -delete

%build

%mvn_build -f -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n java-scrypt-javadoc -f %{oreon_filedir}/java-scrypt-javadoc.list

%changelog

%autochangelog
