%global source0_hash 3234efd438140e5633bfb716012b7f78a0902661fb0511b24d146e07a6ebc5ae

Name:           perl-Net-CLI-Interact
Version:        2.400002
Release:        7%{?dist}
Summary:        Toolkit for CLI Automation
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Net-CLI-Interact
Source0:        https://cpan.metacpan.org/modules/by-module/Net/Net-CLI-Interact-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::ShareDir::Install) >= 0.06
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Class::Load)
BuildRequires:  perl(Class::Mix)
BuildRequires:  perl(File::ShareDir)
# FileHandle not used at tests
BuildRequires:  perl(IO::Pty)
BuildRequires:  perl(IPC::Run)
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Log::Dispatch::Config)
BuildRequires:  perl(Log::Dispatch::Configurator::Any)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Moo::Role)
BuildRequires:  perl(MooX::Types::MooseLike::Base)
BuildRequires:  perl(Net::Telnet)
BuildRequires:  perl(Path::Class)
# POSIX not used at tests
BuildRequires:  perl(Sub::Quote)
BuildRequires:  perl(Time::HiRes)
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88

%description
Automating command line interface (CLI) interactions is not a new idea, but
can be tricky to implement. This module aims to provide a simple and
manageable interface to CLI interactions, supporting:

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Net-CLI-Interact-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
unset AUTHOR_TESTING RELEASE_TESTING
make test

%files
%license LICENSE
%doc Changes
%{perl_vendorlib}/auto*
%{perl_vendorlib}/Net/CLI/Interact*
%{_mandir}/man3/Net::CLI::Interact*

%changelog
%autochangelog
