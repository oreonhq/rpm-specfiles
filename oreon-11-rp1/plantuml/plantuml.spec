%global source0_hash caa1dc0b2df3058c38b69de5878eb048a24a99346aeab663b7027e85cdc83467
Name:           plantuml
Version:        1.2026.8
Release:        1%{?dist}
Epoch:          1
Summary:        Program to generate UML diagram from a text description
License:        LGPL-3.0-or-later
URL:            http://plantuml.com/
Source0:        https://github.com/%{name}/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       java-25
Requires:       javapackages-tools
Requires:       graphviz
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  help2man
BuildRequires:  javapackages-local-openjdk25
# /oreon:deps
%description
PlantUML is a program allowing to draw UML diagrams, using a simple
and human readable text description. It is extremely useful for code
documenting, sketching project architecture during team conversations
and so on.

PlantUML supports the following diagram types
  - sequence diagram
  - use case diagram
  - class diagram
  - activity diagram
  - component diagram
  - state diagram

%prep
%oreon_prep
%build

ant
%install
%mvn_file net.sourceforge.%{name}:%{name} %{name}
%mvn_artifact net.sourceforge.%{name}:%{name}:%{version} %{name}.jar
%mvn_install
%jpackage_script net.sourceforge.plantuml.Run "" "" plantuml plantuml true
install -d "%{buildroot}%{_mandir}/man1"
help2man --help-option='-h' --version-option='--version' --no-info --output='%{buildroot}%{_mandir}/man1/plantuml.1' "java -jar plantuml.jar"
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
