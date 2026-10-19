%global source0_hash bed0c96fe91c98fd37e6eb59a804aaac9cc4a9e928450b76d4bf5527a9e6a47b
%bcond_without perl_POE_Test_Loops_enables_curses
Name:           perl-POE-Test-Loops
Summary:        Reusable tests for POE::Loop authors
Version:        1.360
Release:        1%{?dist}
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
Source0:        https://cpan.metacpan.org/authors/id/R/RC/RCAPUTO/POE-Test-Loops-%{version}.tar.gz
URL:            https://metacpan.org/release/POE-Test-Loops
BuildArch:      noarch
%if %{with perl_POE_Test_Loops_enables_curses}
%endif
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
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test::More\\)$
%global __provides_exclude %{?__provides_exclude:__provides_exclude|}^perl\\(POE::MySession\\)
%global __provides_exclude %__provides_exclude|perl\\(POE::Kernel\\)
%global __provides_exclude %__provides_exclude|perl\\(PoeTestWorker\\)
%global __provides_exclude %__provides_exclude|perl\\([DIFMOSU].*\\)
%global __provides_exclude %__provides_exclude|perl\\(Switch\\)
Provides:       perl(POE::Test::Loops)
Provides:       perl(POE::Test::Loops)
# oreon:deps
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Find)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(constant)
BuildRequires:  perl(lib)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
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
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
