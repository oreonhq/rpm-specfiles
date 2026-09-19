%global source0_hash 2713f07a6adec7e253d91f1fca70e658b93e1a63f1b6a36f4907a2b83088543f

%global short_name commons-digester

Name:          apache-%{short_name}
Version:       2.1
Release:       37%{?dist}
Summary:       XML to Java object mapping module
# Automatically converted from old format: ASL 2.0 - review is highly recommended.
License:       Apache-2.0
URL:           http://commons.apache.org/digester/
BuildArch:     noarch
ExclusiveArch:  %{java_arches} noarch

Source0:       http://archive.apache.org/dist/commons/digester/source/%{short_name}-%{version}-src.tar.gz

BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-beanutils:commons-beanutils)
BuildRequires:  mvn(commons-logging:commons-logging)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.commons:commons-parent:pom:)

%description
Many projects read XML configuration files to provide initialization of
various Java objects within the system. There are several ways of doing this,
and the Digester component was designed to provide a common implementation
that can be used in many different projects

%package javadoc
Summary:       API documentation for %{name}

%description javadoc
This package contains the %{summary}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{short_name}-%{version}-src

# Compatibility links
%mvn_alias "%{short_name}:%{short_name}" "org.apache.commons:%{short_name}"
%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build -- -Dcommons.packageId=digester

%install
%mvn_install

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
%autochangelog
