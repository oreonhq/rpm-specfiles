%global source0_hash a987a49becd8742a671d36ba0e028c7fdfdd6ef65e8d90d18521e545be810e5a
Name:           cambozola
Version:        0.936
Release:        31%{?dist}
Summary:        A viewer for multipart jpeg streams
License:        GPL-2.0-or-later
URL:            http://www.charliemouse.com/code/cambozola/index.html
Source0:        http://www.andywilcock.com/code/cambozola/%{name}-latest.tar.gz
Patch0:         %{name}-add-javadoc.patch
Patch1:         %{name}-source-target.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
%{?el6:BuildRequires:  ant-nodeps}
Requires:       jpackage-utils
Requires:       java-25
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  findutils
BuildRequires:  java-25-devel
BuildRequires:  jpackage-utils
# /oreon:deps
%description
Cambozola is a very simple (cheesy!) viewer for multipart jpeg streams
that are often pumped out by a streaming webcam server,
sending over multiple images per second.

%package javadoc
Summary:        Javadoc for %{name}
Requires:       jpackage-utils
%description javadoc
This package contains the API documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p 1

# Remove pre-built JAR and class files
find -name '*.jar' -exec rm -f '{}' \;
find -name '*.class' -exec rm -f '{}' \;

%build

%ant javadoc
%ant
%install
mkdir -p %{buildroot}%{_javadir}
cp -p dist/%{name}.jar   \
  %{buildroot}%{_javadir}/%{name}.jar
cp -p dist/%{name}-server.jar   \
  %{buildroot}%{_javadir}/%{name}-server.jar
mkdir -p %{buildroot}%{_javadocdir}/%{name}
cp -rp javadoc/*  \
  %{buildroot}%{_javadocdir}/%{name}
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n cambozola-javadoc -f %{oreon_filedir}/cambozola-javadoc.list

%changelog

%autochangelog
