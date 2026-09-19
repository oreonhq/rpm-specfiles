%global source0_hash 59b9a697b6eaf2569ba164faa9becaf00124619ecc2336c66e78bc905b7377c3

Name:           perl-Module-Used
Version:        1.3.0
Release:        32%{?dist}
Summary:        Find modules loaded by Perl code without running it
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Module-Used
Source0:        https://cpan.metacpan.org/authors/id/E/EL/ELLIOTJS/Module-Used-v%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Config)
BuildRequires:  perl(English)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(strict)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Runtime
BuildRequires:  perl(Const::Fast)
BuildRequires:  perl(Exporter) >= 5.57
# Unused BuildRequires:  perl(File::Next) >= 1.02
BuildRequires:  perl(Module::Path) >= 0.01
BuildRequires:  perl(PPI::Document) >= 1.205
# Tests only
BuildRequires:  perl(Test::Deep) >= 0.098
BuildRequires:  perl(Test::More) >= 0.72
BuildRequires:  perl(version) >= 0.74
Requires:       perl(Exporter) >= 5.57
Requires:       perl(File::Next) >= 1.02
Requires:       perl(Module::Path) >= 0.01
Requires:       perl(PPI::Document) >= 1.205

%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Exporter\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(File::Next\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Module::Path\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(PPI::Document\\)$

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

%check
./Build test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
