%global source0_hash 2a88f21303021dc5919f68dafda23e2641cf9c9c01d15758db23dfbb97e7a36a
Name:           juniversalchardet
Version:        2.5.0
Release:        1%{?dist}
Summary:        Java character encoding detection
License:        MPL-1.1 OR GPL-2.0-or-later OR LGPL-2.1-or-later
URL:            https://github.com/albfernandez/juniversalchardet
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        https://github.com/albfernandez/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%{?javadoc_package}
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mvn(commons-codec:commons-codec)
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.apache.maven.plugins:maven-source-plugin)
# /oreon:deps
%description
Juniversalchardet is a Java port of universalchardet, that is, the
encoding detector library of Mozilla.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup

# Fix newline encoding
sed -i.orig 's/\r//' README.md
touch -r README.md.orig README.md
rm README.md.orig
sed 's;<compiler.level>1.7</compiler.level>;<compiler.level>1.8</compiler.level>;' -i pom.xml
# Plugins not needed for an RPM build
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin
%pom_remove_plugin :nexus-staging-maven-plugin
%pom_remove_plugin :spotbugs-maven-plugin

# Provide alias for the old name
%mvn_alias com.github.albfernandez:juniversalchardet com.googlecode.juniversalchardet:juniversalchardet

%build

%mvn_build
%install
%mvn_install
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
