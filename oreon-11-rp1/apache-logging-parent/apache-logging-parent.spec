%global source0_hash 3c39e1e291fef7be8f2de734c086b05b14ce1e80bf1dfd7e24e86aa2fa94f559

Name:           apache-logging-parent
Summary:        Parent pom for Apache Logging Services projects
Version:        9
Release:        13%{?dist}
License:        Apache-2.0

URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(org.apache:apache:pom:)

%description
Parent pom for Apache Logging Services projects.


%prep
%(test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; })
%setup -q -n logging-parent-%{version}
cp -p %SOURCE1 LICENSE

%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin

%build
%mvn_build


%install
%mvn_install


%files -f .mfiles
%license LICENSE


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 9-13
- Prepare for Oreon 11 (RP1)
