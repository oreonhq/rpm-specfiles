%global source0_hash d0812192d581e51108ad053278e54415e043cf903d8ba0297789bfd16f8314dc
%global giturl  https://github.com/antlr/stringtemplate4
Name:           stringtemplate4
Version:        4.3.4
Release:        10%{?dist}
Summary:        A Java template engine
License:        BSD-3-Clause
URL:            http://www.stringtemplate.org/
VCS:            git:%{giturl}.git
BuildArch:      noarch
ExclusiveArch:  %{java_arches} noarch
Source0:        %{giturl}/archive/ST4-%{version}/%{name}-%{version}.tar.gz
Patch:          %{name}-java11.patch
Patch:          %{name}-java21.patch
# oreon:deps
BuildRequires:  maven-local-openjdk25
BuildRequires:  mesa-dri-drivers
BuildRequires:  mutter
BuildRequires:  mvn(junit:junit)
BuildRequires:  mvn(org.antlr:antlr-runtime)
BuildRequires:  mvn(org.antlr:antlr3-maven-plugin)
BuildRequires:  xwayland-run
# /oreon:deps
%description
StringTemplate is a java template engine (with ports for C# and Python) for
generating source code, web pages, emails, or any other formatted text output.
StringTemplate is particularly good at multi-targeted code generators,
multiple site skins, and internationalization/localization.

%package javadoc
Summary:       Javadoc for %{name}
%description javadoc
This package contains javadoc for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-ST4-%{version}

%conf
# sonatype-oss-parent is deprecated in Fedora
%pom_remove_parent

%build

xwfb-run -c mutter -- %mvn_build
%install
%mvn_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n stringtemplate4-javadoc -f %{oreon_filedir}/stringtemplate4-javadoc.list

%changelog

%autochangelog
