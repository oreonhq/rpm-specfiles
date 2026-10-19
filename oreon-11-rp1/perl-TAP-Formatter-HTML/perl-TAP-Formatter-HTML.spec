%global source0_hash 2203dec33dd98d33f257b6ff38dada3c5e1f5105ef7797973a5a60985c13d933
Name:           perl-TAP-Formatter-HTML
Version:        0.13
Release:        7%{?dist}
Summary:        TAP Test Harness output delegate for html output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TAP-Formatter-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/TAP/TAP-Formatter-HTML-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(accessors) >= 0.02
Requires:       perl(File::Temp) >= 0.17
Requires:       perl(TAP::Parser::Aggregator) >= 3.10
Requires:       perl(Template) >= 2.14
Requires:       perl(URI) >= 1.35
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(accessors\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(File::Temp\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(TAP::Parser::Aggregator\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Template\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(URI\\)$
Provides:       perl(TAP::Formatter::HTML)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(TAP::Base)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(TAP::Parser::Aggregator)
BuildRequires:  perl(Template)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(URI)
BuildRequires:  perl(URI::file)
BuildRequires:  perl(accessors)
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
This module provides HTML output formatting for TAP::Harness (a replacement
for Test::Harness). It is largely based on ideas from TAP::Test::HTMLMatrix
(which was built on Test::Harness and thus had a few limitations - hence
this module).

This module is targeted at all users of automated test suites. It's meant to
make reading test results easier, giving you a visual summary of your test
suite and letting you drill down into individual failures (which will hopefully
make testing more likely to happen at your organization!).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n TAP-Formatter-HTML-%{version}

%build

perl Build.PL --installdirs=vendor
./Build
%install
./Build install --destdir=%{buildroot} --create_packlist=0
%{_fixperms} -c %{buildroot}
%oreon_autofiles main

%check

./Build test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
