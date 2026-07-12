%global source0_hash 2203dec33dd98d33f257b6ff38dada3c5e1f5105ef7797973a5a60985c13d933

Name:           perl-TAP-Formatter-HTML
Version:        0.13
Release:        7%{?dist}
Summary:        TAP Test Harness output delegate for html output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TAP-Formatter-HTML
Source0:        https://cpan.metacpan.org/modules/by-module/TAP/TAP-Formatter-HTML-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Module::Build)
# Runtime
BuildRequires:  perl(accessors) >= 0.02
BuildRequires:  perl(base)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Spec::Functions)
BuildRequires:  perl(File::Temp) >= 0.17
BuildRequires:  perl(IO::File)
BuildRequires:  perl(POSIX)
BuildRequires:  perl(strict)
BuildRequires:  perl(TAP::Base)
# Test Suite
BuildRequires:  perl(App::Prove)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Basename)
BuildRequires:  perl(lib)
BuildRequires:  perl(TAP::Harness) >= 3.17
BuildRequires:  perl(TAP::Parser::Aggregator) >= 3.10
BuildRequires:  perl(Template) >= 2.14
BuildRequires:  perl(Test::More) >= 0.01
BuildRequires:  perl(URI) >= 1.35
BuildRequires:  perl(URI::file)
BuildRequires:  perl(warnings)
# Optional Tests
BuildRequires:  perl(Test::Pod) >= 1.00
# Dependencies
Requires:       perl(accessors) >= 0.02
Requires:       perl(File::Temp) >= 0.17
Requires:       perl(TAP::Parser::Aggregator) >= 3.10
Requires:       perl(Template) >= 2.14
Requires:       perl(URI) >= 1.35

# Remove underspecified dependencies
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(accessors\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(File::Temp\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(TAP::Parser::Aggregator\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(Template\\)$
%global __requires_exclude %{__requires_exclude}|^perl\\(URI\\)$

Provides:       perl(TAP::Formatter::HTML)
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

%check
./Build test

%files
%doc Changes README Todo
%{perl_vendorlib}/App/
%{perl_vendorlib}/TAP/
%{_mandir}/man3/App::Prove::Plugin::HTML.3*
%{_mandir}/man3/TAP::Formatter::HTML.3*
%{_mandir}/man3/TAP::Formatter::HTML::Session.3*

%changelog
%autochangelog
