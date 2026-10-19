%global source0_hash 5ecf68b9a86c40249823eeaa1c055baf9249dbcb7eff9da541af86b4fcf04bdd
Name:           perl-JavaScript-Beautifier
Version:        0.25
Release:        24%{?dist}
Summary:        Beautify Javascript (beautifier for javascript)
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/JavaScript-Beautifier
Source0:        https://cpan.metacpan.org/authors/id/F/FA/FAYLAND/JavaScript-Beautifier-%{version}.tar.gz
BuildArch:      noarch
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(JavaScript::Packer1\\)
# oreon:deps
BuildRequires:  dos2unix
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(base)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module is mostly a Perl-rewrite of
http://github.com/einars/js-beautify/tree/master/beautify.js

%package -n perl-Code-TidyAll-Plugin-JSBeautifier
Summary:        Use JavaScript::Beautifier with tidyall
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Requires:       %{_bindir}/js_beautify.pl
Requires:       perl(Code::TidyAll::Plugin)
%description -n perl-Code-TidyAll-Plugin-JSBeautifier
Runs js_beautify.pl of JavaScript::Beautifier, a JavaScript tidier
implemented in Perl.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n JavaScript-Beautifier-%{version}
dos2unix Changes
dos2unix README.md

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles perl-Code-TidyAll-Plugin-JSBeautifier usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

./Build test
%files -f %{oreon_filedir}/main.list
%files -n perl-Code-TidyAll-Plugin-JSBeautifier -f %{oreon_filedir}/perl-Code-TidyAll-Plugin-JSBeautifier.list

%changelog

%autochangelog
