%global source0_hash ac340b676ba2b62246b9df77e62f81ad4447bcfd329ab539716bcd09950b7096

Name:           Mars
Version:        4.5
Release:        34%{?dist}
Summary:        An interactive development environment for programming in MIPS assembly language

License:        MIT
URL:            https://dpetersanderson.github.io/
Source0:        https://github.com/dpetersanderson/MARS/releases/download/v.4.5.1/Mars4_5.jar
Source1:        Mars
Source2:        Mars.desktop
Source3:        build.xml
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch

BuildRequires:  ant-openjdk25 
BuildRequires:  java-25-devel
BuildRequires:  desktop-file-utils

Requires:       java-25

%description
MARS is a lightweight interactive development environment (IDE) for
programming in MIPS assembly language, intended for educational-level
use with Patterson and Hennessy's Computer Organization and Design.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{name}-%{version}

find . -name '*.jar'   -exec rm -f '{}' \;
find . -name '*.class' -exec rm -f '{}' \;

%build
sed -i 's/\r//' MARSlicense.txt

cp -p %{SOURCE3} build.xml
ant

%install
install -Dpm 644 %{name}.jar ${RPM_BUILD_ROOT}%{_javadir}/%{name}.jar
install -Dpm 755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}/%{name}
desktop-file-install                                \
    --add-category="Development"                    \
    --dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
    %{SOURCE2}

%files
%{_javadir}/%{name}.jar
%{_bindir}/%{name}
%{_datadir}/applications/Mars.desktop
%doc MARSlicense.txt

%changelog
%autochangelog
