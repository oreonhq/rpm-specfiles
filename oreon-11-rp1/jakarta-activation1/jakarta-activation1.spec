%global source0_hash 6d2322271bf6fb00d5505317973b8797064d72390c1389906b72fc8a21636a01

%bcond_with bootstrap

Name:           jakarta-activation1
Version:        1.2.2
Release:        %autorelease
Summary:        Jakarta Activation API 1.2
License:        BSD-3-Clause
URL:            https://jakarta.ee/specifications/activation/1.2/
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://github.com/jakartaee/jaf-api/archive/%{version}/jaf-%{version}.tar.gz

%if %{with bootstrap}
BuildRequires:  javapackages-bootstrap
%else
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-dependency-plugin)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires:  mvn(org.codehaus.mojo:build-helper-maven-plugin)
%endif

%description
Jakarta Activation defines a set of standard services to: determine
the MIME type of an arbitrary piece of data; encapsulate access to it;
discover the operations available on it; and instantiate the
appropriate bean to perform the operation(s).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -C

%pom_remove_parent
%pom_disable_module demo

%pom_remove_plugin -r :maven-enforcer-plugin

%pom_remove_plugin :directory-maven-plugin
sed -i 's/${main.basedir}/${basedir}/' pom.xml

# Remove custom doclet configuration
%pom_remove_plugin :maven-javadoc-plugin activation

# Set bundle version manually instead of with osgiversion-maven-plugin
# (the plugin is only used to strip off -SNAPSHOT or -Mx qualifiers)
%pom_remove_plugin :osgiversion-maven-plugin
sed -i "s/\${activation.osgiversion}/%{version}/g" activation/pom.xml

%mvn_compat_version jakarta*: 1 %{version} 1.2.1 1.2.0 1.1.1

# TODO delete
%mvn_file com.sun.activation:jakarta.activation %{name}/jakarta.activation javax.activation

%build
# Javadoc fails:
# /builddir/build/BUILD/jaf-api-1.2.2/activation/src/main/java/module-info.java:11: error: duplicate module: jakarta.activation
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.md NOTICE.md

%changelog
%autochangelog
