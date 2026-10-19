%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash 5c7e387cd5df47b3aec3fc7719a8f78228a8a5183c61b557da67c2d52c93edf5
Name:          jackson-parent
Version:       2.22
Release:        1%{?dist}
Summary:        Parent pom for all Jackson components
License:       Apache-2.0
URL:           https://github.com/FasterXML/jackson-parent
Source0:        https://github.com/FasterXML/jackson-parent/archive/refs/tags/jackson-parent-%{version}.tar.gz#/jackson-parent-%{version}.tar.gz
Source1:       https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)
# /oreon:deps
%description
Project for parent pom for all Jackson components.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-%{name}-%{version}

cp -p %{SOURCE1} LICENSE
sed -i 's/\r//' LICENSE

%build

%mvn_build -j
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.1-6
- Prepare for Oreon 11 (RP1)
