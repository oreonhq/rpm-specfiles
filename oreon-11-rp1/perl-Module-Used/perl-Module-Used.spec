%global source0_hash 59b9a697b6eaf2569ba164faa9becaf00124619ecc2336c66e78bc905b7377c3
Name:           perl-Module-Used
Version:        1.3.0
Release:        1%{?dist}
Summary:        Find modules loaded by Perl code without running it
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Used
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/Module-Used-v%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter) >= 5.57
Requires:       perl(File::Next) >= 1.02
Requires:       perl(Module::Path) >= 0.01
Requires:       perl(PPI::Document) >= 1.205
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Next\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Path\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PPI::Document\\)$
# oreon:deps
BuildRequires:  perl(Config)
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(English)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Path)
BuildRequires:  perl(PPI::Document)
BuildRequires:  perl(Test::Deep)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  sed
# /oreon:deps
%description
Modules are found statically based upon use and require statements. If use
of the base or parent is found, both that module and the referenced ones
will be returned. If Moose or Moose::Role are found, this will look for
extends and with sugar will be looked for; presently, this will miss
modules listed in parentheses.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Module-Used-v%{version}
# Remove /usr/bin/env from shebang
sed -i -e '1 s|#!.*|%(perl -MConfig -e 'print $Config{startperl}')|' \
    bin/modules-used

%build

perl Build.PL installdirs=vendor
./Build
%install
./Build install destdir=%{buildroot} create_packlist=0
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
