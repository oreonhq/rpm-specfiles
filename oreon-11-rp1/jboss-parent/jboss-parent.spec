%global source1_hash a2010f343487d3f7618affe54f789f5487602331c0a8d03f49e9a7c547cf0499
%global source0_hash 7892327f038ec9e36880bd387618d8a10256948c76b47bbb9426fc90cbee1746

Name:           jboss-parent
Version:        54
Release:        1%{?dist}
Summary:        JBoss Parent POM
License:        CC0-1.0
URL:            http://www.jboss.org/
BuildArch:      noarch
%if 0%{?fedora}
ExclusiveArch:  %{java_arches} noarch
%endif

Source0:        https://github.com/jboss/jboss-parent-pom/archive/refs/tags/%{name}-%{version}.tar.gz#/jboss-parent-20.tar.gz
Source1:        https://repository.jboss.org/licenses/cc0-1.0.txt

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:  maven-local
%else
BuildRequires:  maven-local-openjdk25
%endif

BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)

%description
The Project Object Model files for JBoss packages.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n %{name}-pom-%{name}-%{version}

# NOT available plugins
%pom_remove_plugin :cobertura-maven-plugin
%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :javancss-maven-plugin
%pom_remove_plugin :license-maven-plugin
%pom_remove_plugin :sonar-maven-plugin

%pom_remove_plugin :maven-enforcer-plugin
%pom_remove_plugin :buildnumber-maven-plugin

cp -p %SOURCE1 LICENSE
sed -i 's/\r//' LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE

%changelog
%autochangelog
