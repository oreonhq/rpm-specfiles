%global source0_hash e8e152c555bf056cc7a21839a5de802887d4d7995ca13047bae77631d6bc5205

Name:          jackson-parent
Version:       2.18.1
Release:       6%{?dist}
Summary:       Parent pom for all Jackson components
License:       Apache-2.0

URL:           https://github.com/FasterXML/jackson-parent
Source0:        https://github.com/FasterXML/jackson-parent/archive/refs/tags/jackson-parent-2.18.1.tar.gz#/jackson-parent-2.18.1.tar.gz
# jackson-parent package don't include the license file
# reported @ https://github.com/FasterXML/jackson-parent/issues/1
Source1:       http://www.apache.org/licenses/LICENSE-2.0.txt

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(com.fasterxml:oss-parent:pom:)

BuildArch:      noarch
%if 0%{?fedora} || 0%{?rhel} >= 10
ExclusiveArch:  %{java_arches} noarch
%endif

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

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.18.1-6
- Prepare for Oreon 11 (RP1)
