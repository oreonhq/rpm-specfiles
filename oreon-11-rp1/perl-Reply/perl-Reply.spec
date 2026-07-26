%global source0_hash 4ada2a45a77a54ae10c4e9a48144ea826d5d79ad050cb9626e9f783d03ab79f2

Name:           perl-Reply
Version:        0.42
Release:        27%{?dist}
Summary:        Plugin-based read-evaluate-print loop for Perl
License:        MIT
URL:            https://metacpan.org/release/Reply
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Reply-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# App::Nopaste not used at tests
# B::Keywords not used at tests
BuildRequires:  perl(base)
# Carp::Always not used at tests
# Class::Refresh 0.05 not used at tests
BuildRequires:  perl(Config::INI::Reader::Ordered)
# Data::Dump not used at tests
BuildRequires:  perl(Data::Dumper)
# Data::Printer not used at tests
BuildRequires:  perl(Eval::Closure) >= 0.11
BuildRequires:  perl(Exporter)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long) >= 2.36
BuildRequires:  perl(IO::Pager)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(mro)
# MRO::Compat not used with perl >= 5.10
# overload not used at tests
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(PadWalker)
# Proc::InvokeEditor not used at tests
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
# Term::ReadKey not used at tests
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
# Win32::Console::ANSI not used on Linux
# Tests:
BuildRequires:  perl(blib) >= 1.01
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test::More) >= 0.88
Requires:       perl(Carp::Always)
Requires:       perl(IO::Pager)
Requires:       perl(mro)
Recommends:     perl(Term::ReadLine::Gnu)

%description
Reply is a lightweight, extensible read-evaluate-print loop (REPL) for Perl.
It is plugin-based (see Reply::Plugin), and through plugins supports many
advanced features such as coloring and pretty printing, Readline support, and
pluggable commands.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Reply-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{_bindir}/reply
%{perl_vendorlib}/*
%{_mandir}/man1/*
%{_mandir}/man3/*

%changelog
%autochangelog
