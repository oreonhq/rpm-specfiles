%global source0_hash 82e49065d408cba8b323eea0b7f49899578336d566096c6eb6e2d0a28745d63b
Summary:        Diagrams Through ASCII Art
Name:           ditaa
Version:        0.10
Release:        1%{?dist}
License:        GPL-2.0-or-later
URL:            http://ditaa.sourceforge.net/
Source0:        https://github.com/stathissideris/ditaa/archive/v%{version}.tar.gz
Source1:        ditaa.wrapper
Patch0:         ditaa-0.9-port-to-batik-1.8.patch
Patch1:         https://sources.debian.org/data/main/d/ditaa/0.10+ds1-1.2/debian/patches/remove-JavadocTaglet.patch
Patch2:         jdk17.patch
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Requires:       apache-commons-cli
Requires:       xml-commons-apis
Requires:       jericho-html
Requires:       batik
Requires:       jpackage-utils
Requires:       java-25-headless >= 1:1.6.0
# oreon:deps
BuildRequires:  ant-openjdk25
BuildRequires:  apache-commons-cli
BuildRequires:  batik
BuildRequires:  java-25-devel
BuildRequires:  jericho-html
BuildRequires:  jpackage-utils
BuildRequires:  xml-commons-apis
# /oreon:deps
%description
ditaa is a small command-line utility written in Java, that can
convert diagrams drawn using ASCII art ('drawings' that contain
characters that resemble lines like | / - ), into proper bitmap
graphics.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1
find -name '*.class' -delete
find -name '*.jar' -delete

%build

install -d bin
build-jar-repository -s -p lib commons-cli batik-all xml-commons-apis-ext jericho-html
ant -f build/release.xml
%install
install -D -p -m 0644 releases/%{name}0_9.jar %{buildroot}%{_javadir}/%{name}.jar
install -D -p -m 0755 %{SOURCE1} %{buildroot}%{_bindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
