%global source2_hash f154a693df7d01290487b3bf4c045481cdde6bd310b9eeb37b7a533b03b3299a
%global source1_hash 1dacc34ebc8f3e9e7dea7f802549e6e5db79aef321c0e28eb875f665958fe36e
%global source0_hash 88cd253b6695b3d6e14d5ced7753fdf4a9e6d322d1c5f08122a8fefce61d1e4c
%global jarname commons-text
Name:           apache-%{jarname}
Version:        1.15.0
Release:        1%{?dist}
Summary:        Apache Commons Text is a library focused on algorithms working on strings
License:        Apache-2.0
URL:            https://commons.apache.org/proper/%{jarname}
BuildArch:      noarch
Source0:        https://archive.apache.org/dist/commons/text/source/%{jarname}-%{version}-src.tar.gz
Source1:        https://archive.apache.org/dist/commons/text/source/%{jarname}-%{version}-src.tar.gz.asc
Source2:        https://archive.apache.org/dist/commons/KEYS
# oreon:deps
BuildRequires:  gnupg2
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.assertj:assertj-core)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter)
BuildRequires:  mvn(org.mockito:mockito-core)
# /oreon:deps
%description
The Commons Text library provides additions to the standard JDK's text handling.
Our goal is to provide a consistent set of tools for processing text generally
from computing distances between Strings to being able to efficiently do String
escaping of various types.

%{?javadoc_package}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

# verify signed sources
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

# -p1: strip one level directory in patch(es)
# -n: base directory name
%autosetup -p1 -n %{jarname}-%{version}-src

# delete precompiled jar and class files
find -type f '(' -name '*.jar' -o -name '*.class' ')' -print -delete

# mockito-inline was merged into mockito-core
%pom_change_dep :mockito-inline :mockito-core

%build

%mvn_build -f -- -Dmaven.compiler.release=8
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog

