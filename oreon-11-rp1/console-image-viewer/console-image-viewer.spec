%global source0_hash ee8a1075c8d8ee297ecfe146e88cb96f36e77fa73d2cb82193c90a1c12c65d61
%global upstream ConsoleImageViewer
%global launcher consoleImageViewer
Name:    console-image-viewer
Version: 1.2
Release:        1%{?dist}
Summary:        Terminal image viewer
License:  MIT
URL:      https://github.com/judovana/ConsoleImageViewer
Source0:        https://github.com/judovana/%{upstream}/archive/%{upstream}-%{version}.tar.gz
Source1:  %{launcher}.man
BuildArch: noarch
ExclusiveArch:  %{java_arches} noarch
Requires: java-25
Requires: javapackages-tools
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  java-25-devel
# /oreon:deps
%description
Highly scale-able, high quality, image viewer for ANSI terminals.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{upstream}-%{upstream}-%{version}
find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;
sed 's;<attribute name="Main-Class" value="${main.class}"/>;;' -i nbproject/build-impl.xml
sed "s;1.6;1.8;g" -i nbproject/project.properties

%build

ant
%install
mkdir -p $RPM_BUILD_ROOT/%{_javadir}
cp dist/%{upstream}.jar $RPM_BUILD_ROOT/%{_javadir}/%{upstream}.jar
mkdir -p $RPM_BUILD_ROOT/%{_bindir}/
cat <<EOF > $RPM_BUILD_ROOT/%{_bindir}/%{launcher}
. /usr/share/java-utils/java-functions
MAIN_CLASS=org.judovana.linux.ConsoleImageViewer
set_classpath "%{upstream}-%{version}"
run \${@}
EOF
chmod 755 $RPM_BUILD_ROOT/%{_bindir}/%{launcher}
mkdir -p $RPM_BUILD_ROOT/%{_mandir}/man1/
gzip -c %{SOURCE1}  > $RPM_BUILD_ROOT/%{_mandir}/man1/%{launcher}.1.gz
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
