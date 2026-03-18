%global base_name exec
%global short_name commons-%{base_name}

Name:           apache-commons-exec
Version:        1.6.0
Release:        3%{?dist}
Summary:        Java library to reliably execute external processes from within the JVM
License:        Apache-2.0
URL:            https://commons.apache.org/proper/%{short_name}
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

Source0:        https://www.apache.org/dist/commons/%{base_name}/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  mvn(org.junit.jupiter:junit-jupiter-api)

# Tests require /usr/bin/ping
BuildRequires:  iputils

%description
Commons Exec is a library for dealing with external process execution and
environment management in Java.


%package javadoc
Summary:        Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.


%prep
%autosetup -n %{short_name}-%{version}-src

# Disable junit-pioneer features since it's not (yet) available in Fedora
%pom_remove_dep org.junit-pioneer:junit-pioneer
find src/test/java/ -name "*.java" -exec sed  -i '/SetSystemProperty/d' {} \;


%build
# - Skip Exec34Test/Exec41Test/Exec60Test ("socket: Operation not permitted" on Koji)
# - Skip Exec57Test (it is unstable), see RHBZ #1202260
# - Skip Exec65Test (calls sudo)
%mvn_build -- \
  -Dcommons.osgi.symbolicName=org.apache.commons.exec \
  -Dcommons.packageId=exec \
  -Dtest=\!org.apache.commons.exec.issues.Exec34Test,\!org.apache.commons.exec.issues.Exec41Test,\!org.apache.commons.exec.issues.Exec57Test,\!org.apache.commons.exec.issues.Exec60Test,\!org.apache.commons.exec.issues.Exec65Test


%install
%mvn_install


%files -f .mfiles
%license LICENSE.txt NOTICE.txt
%doc RELEASE-NOTES.txt


%files javadoc -f .mfiles-javadoc
%license LICENSE.txt NOTICE.txt


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.6.0-3
- Prepare for Oreon 11 (RP1)
