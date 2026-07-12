%global source0_hash bed0c96fe91c98fd37e6eb59a804aaac9cc4a9e928450b76d4bf5527a9e6a47b

# Enable curses on PTY
%bcond_without perl_POE_Test_Loops_enables_curses

Name:           perl-POE-Test-Loops
Summary:        Reusable tests for POE::Loop authors
Version:        1.360
Release:        33%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Test-Loops-%{version}.tar.gz 
URL:            https://metacpan.org/release/POE-Test-Loops
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
# File::Temp not used at tests
# Getopt::Long not used at tests
# IO::File not used at tests
# IO::Handle not used at tests
# IO::Pipely not used at tests
# IO::Socket not used at tests
# IO::Socket::INET not used at tests
BuildRequires:  perl(lib)
# POE not used at tests
# POE::Component::Client::TCP not used at tests
# POE::Component::Server::TCP not used at tests
# POE::Driver::SysRW not used at tests
# POE::Filter::Block not used at tests
# POE::Filter::Line not used at tests
# POE::Filter::Map not used at tests
# POE::Filter::Stream not used
# POE::NFA not used at tests
# POE::Pipe::OneWay not used at tests
# POE::Pipe::TwoWay not used at tests
# POE::Session not used at tests
# POE::Wheel::Curses not used at all
# POE::Wheel::FollowTail no used at tests
# POE::Wheel::ListenAccept not used at tests
# POE::Wheel::ReadWrite not used at tests
# POE::Wheel::Run not used at tests
# POE::Wheel::SocketFactory not used at tests
# POSIX not used at tests
# Socket not used at tests
# Symbol not used at tests
BuildRequires:  perl(Test::More) >= 1.001002
# Time::HiRes not used at tests
BuildRequires:  perl(vars)
%if %{with perl_POE_Test_Loops_enables_curses}
# Optional run-time:
# Curses not used at tests
# IO::Pty not used at tests
%endif
# Socket6 not used at all
# Optional tests:
BuildRequires:  perl(Scalar::Util)
Requires:       perl(Carp)
Requires:       perl(POE::Component::Client::TCP)
Requires:       perl(POE::Component::Server::TCP)
Requires:       perl(POE::Driver::SysRW)
Requires:       perl(POE::Filter::Block)
Requires:       perl(POE::Filter::Line)
Requires:       perl(POE::Filter::Map)
Requires:       perl(POE::Pipe::TwoWay)
Requires:       perl(POE::Wheel::FollowTail)
Requires:       perl(POE::Wheel::ListenAccept)
Requires:       perl(POE::Wheel::SocketFactory)
Requires:       perl(Test::More) >= 1.001002
%if %{with perl_POE_Test_Loops_enables_curses}
Suggests:       perl(Curses)
Suggests:       perl(IO::Pty)
%endif

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$

# Hide private modules
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(POE::MySession\\)
%global __provides_exclude %__provides_exclude|perl\\(POE::Kernel\\)
%global __provides_exclude %__provides_exclude|perl\\(PoeTestWorker\\)
%global __provides_exclude %__provides_exclude|perl\\([DIFMOSU].*\\)
%global __provides_exclude %__provides_exclude|perl\\(Switch\\)

Provides:       perl(POE::Test::Loops)
Provides:       perl(POE::Test::Loops)
%description
POE::Test::Loops contains one function, generate(), which will generate all
the loop tests for one or more POE::Loop subclasses.  The poe-gen-tests manual
page also documents the POE::Test::Loops system in more detail.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n POE-Test-Loops-%{version}
find . -type f -exec chmod -c -x {} +

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*
%{_bindir}/poe-gen-tests
%{_mandir}/man1/poe-gen-tests.1.gz

%changelog
%autochangelog
