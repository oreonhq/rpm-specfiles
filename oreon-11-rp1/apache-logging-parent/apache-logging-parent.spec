Name:           apache-logging-parent
Summary:        Parent pom for Apache Logging Services projects
Version:        9
Release:        13%{?dist}
License:        Apache-2.0

URL:            https://logging.apache.org/
Source0:        https://repo1.maven.org/maven2/org/apache/logging/logging-parent/%{version}/logging-parent-%{version}-source-release.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
# oreon url source checksums begin
%global source0_sha256 3c39e1e291fef7be8f2de734c086b05b14ce1e80bf1dfd7e24e86aa2fa94f559
%global source0_file logging-parent-9-source-release.zip
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/logging-parent-9-source-release.zip; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "3c39e1e291fef7be8f2de734c086b05b14ce1e80bf1dfd7e24e86aa2fa94f559" || { echo "oreon: Source0 SHA256 mismatch for logging-parent-9-source-release.zip" >&2; exit 1; })
# oreon verify url source checksums end
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
