%global namedreltag .Final
%global namedversion %{version}%{?namedreltag}

Name:             jdeparser
Version:          2.0.3
Release:          23%{?dist}
Summary:          Source generator library for Java
License:          Apache-2.0
URL:              https://github.com/jdeparser/jdeparser2
# old repos https://github.com/jdeparser/jdeparser
Source0:          %{url}/archive/%{namedversion}/%{name}-%{namedversion}.tar.gz
Patch1:           0001-Drop-Assertions.callerIs.patch

BuildArch:        noarch
ExclusiveArch:  %{java_arches} noarch

%if 0%{?rhel} || 0%{?fedora} && 0%{?fedora} <= 42
BuildRequires:    maven-local
%else
BuildRequires:    maven-local-openjdk25
%endif

BuildRequires:    mvn(junit:junit)
BuildRequires:    mvn(org.jboss:jboss-parent:pom:)

%description
This project is a fork of Sun's (now Oracle's) com.sun.codemodel project. We
decided to fork the project because by all evidence, the upstream project is
dead and not actively accepting outside contribution. All JBoss projects are
urged to use this project instead for source code generation.

%prep
%autosetup -n jdeparser2-%{namedversion} -p 1

%build
%mvn_build -j

%install
%mvn_install

%files -f .mfiles
%license LICENSE.txt

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.0.3-23
- Prepare for Oreon 11 (RP1)
