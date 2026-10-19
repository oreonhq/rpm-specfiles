%global source0_hash 4ada2a45a77a54ae10c4e9a48144ea826d5d79ad050cb9626e9f783d03ab79f2
Name:           perl-Reply
Version:        0.42
Release:        1%{?dist}
Summary:        Plugin-based read-evaluate-print loop for Perl
License:        MIT
URL:            https://metacpan.org/release/Reply
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOY/Reply-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Carp::Always)
Requires:       perl(IO::Pager)
Requires:       perl(mro)
Recommends:     perl(Term::ReadLine::Gnu)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Config::INI::Reader::Ordered)
BuildRequires:  perl(Data::Dumper)
BuildRequires:  perl(Eval::Closure)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IO::Pager)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Module::Runtime)
BuildRequires:  perl(Package::Stash)
BuildRequires:  perl(PadWalker)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Term::ANSIColor)
BuildRequires:  perl(Term::ReadLine)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(Try::Tiny)
BuildRequires:  perl(base)
BuildRequires:  perl(blib)
BuildRequires:  perl(mro)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
