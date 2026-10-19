%global source0_hash 856c0fe49bfeafba8446f9a8a72e5439cb6544817d5ec0dafa2a65fb3cd7409e
Name:           perl-TAP-Formatter-JUnit
Version:        0.17
Release:        1%{?dist}
Summary:        Harness output delegate for JUnit output
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/TAP-Formatter-JUnit
Source0:        https://cpan.metacpan.org/modules/by-module/TAP/TAP-Formatter-JUnit-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(TAP::Formatter::Console)
Requires:       perl(TAP::Formatter::Console::Session)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl(CPAN::Meta)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::File)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Scalar)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(Moose)
BuildRequires:  perl(MooseX::NonMoose)
BuildRequires:  perl(Pod::Usage)
BuildRequires:  perl(Storable)
BuildRequires:  perl(TAP::Formatter::Console)
BuildRequires:  perl(TAP::Formatter::Console::Session)
BuildRequires:  perl(TAP::Harness)
BuildRequires:  perl(TAP::Parser)
BuildRequires:  perl(TAP::Parser::Aggregator)
BuildRequires:  perl(Test::DiagINC)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::XML)
BuildRequires:  perl(XML::Generator)
BuildRequires:  perl(blib)
BuildRequires:  perl(if)
BuildRequires:  perl(namespace::clean)
BuildRequires:  perl(strict)
BuildRequires:  perl(version)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
