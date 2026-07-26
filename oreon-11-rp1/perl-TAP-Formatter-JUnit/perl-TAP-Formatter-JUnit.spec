%global source0_hash 856c0fe49bfeafba8446f9a8a72e5439cb6544817d5ec0dafa2a65fb3cd7409e

Name:           perl-TAP-Formatter-JUnit
Version:        0.17
Release:        3%{?dist}
Summary:        Harness output delegate for JUnit output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TAP-Formatter-JUnit
Source0:        https://cpan.metacpan.org/modules/by-module/TAP/TAP-Formatter-JUnit-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Module Runtime
BuildRequires:  perl(File::Path)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(Storable)
BuildRequires:  perl(TAP::Formatter::Console)
BuildRequires:  perl(TAP::Formatter::Console::Session)
BuildRequires:  perl(XML::Generator)
# Script Runtime
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(TAP::Parser::Aggregator)
# Test Suite
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(if)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(TAP::Harness) >= 3.12
BuildRequires:  perl(Test::DiagINC)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::XML)
BuildRequires:  perl(version)
# Optional Tests
BuildRequires:  perl(CPAN::Meta) >= 2.120900
# Runtime
Requires:       perl(TAP::Formatter::Console)
Requires:       perl(TAP::Formatter::Console::Session)

%description
This module provides JUnit output formatting for TAP::Harness (a replacement
for Test::Harness.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n TAP-Formatter-JUnit-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/tap2junit
%{perl_vendorlib}/TAP/
%{_mandir}/man1/tap2junit.1*
%{_mandir}/man3/TAP::Formatter::JUnit.3*
%{_mandir}/man3/TAP::Formatter::JUnit::Result.3*
%{_mandir}/man3/TAP::Formatter::JUnit::Session.3*

%changelog
%autochangelog
