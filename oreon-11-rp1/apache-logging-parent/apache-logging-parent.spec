%global source1_hash cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
%global source0_hash e3384d98a69ee39b1bd417b495b79faee9f5624f65a46147cf1b3efeee337784
Name:           apache-logging-parent
Summary:        Parent pom for Apache Logging Services projects
Version:        12.1.1
Release:        1%{?dist}
License:        Apache-2.0
URL:            https://logging.apache.org/
Source0:        https://dist.apache.org/repos/dist/release/logging/logging-parent/%{version}/apache-logging-parent-%{version}-src.zip
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache:apache:pom:)
# /oreon:deps
%description
Parent pom for Apache Logging Services projects.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -c -T
unzip -q %{SOURCE0}
cp -p %SOURCE1 LICENSE

%pom_remove_plugin com.diffplug.spotless:spotless-maven-plugin

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
