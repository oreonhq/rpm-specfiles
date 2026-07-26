%global source0_hash e47db087f2381e4a6d5ed20df304d1af56d5daaa373cc9140d25569d826651e4

Name:		perl-Parallel-Runner
Version:	0.014
Release:	5%{?dist}
Summary:	An object to manage running things in parallel processes
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/Parallel-Runner
Source0:	https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Parallel-Runner-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	make
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker)
# Module Runtime
BuildRequires:	perl(Carp)
BuildRequires:	perl(Child) >= 0.009
BuildRequires:	perl(POSIX)
BuildRequires:	perl(strict)
BuildRequires:	perl(Time::HiRes)
BuildRequires:	perl(warnings)
# Test Suite
BuildRequires:	perl(Test2::IPC)
BuildRequires:	perl(Test2::V0)
# Dependencies
# (none)

%description
There are several other modules to do this, you probably want one of them. This
module exists as a super-specialized parallel task manager. You create the
object with a process limit and callbacks for what to do while waiting for a
free process slot, as well as a callback for what a process should do just
before exiting.

You must explicitly call $runner->finish() when you are done. If the runner is
destroyed before its children are finished, a warning will be generated and
your child processes will be killed, by force if necessary.

If you specify a maximum of 1 then no forking will occur, and run() will block
until the coderef returns. You can force a fork by providing a boolean true
value as the second argument to run(), which will force the runner to fork
before running the coderef; however, run() will still block until the child
exits.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parallel-Runner-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
RUN_KILL_TESTS=1 make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Parallel/
%{_mandir}/man3/Parallel::Runner.3*

%changelog
%autochangelog
