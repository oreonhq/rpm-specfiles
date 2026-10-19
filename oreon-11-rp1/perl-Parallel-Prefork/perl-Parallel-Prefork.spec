%global source0_hash f1c1f48f1ae147a58bc88f9cb2f570d6bb15ea4c0d589abd4c3084ddc961596e
Name:           perl-Parallel-Prefork
Version:        0.18
Release:        1%{?dist}
Summary:        Simple prefork server framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parallel-Prefork
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Parallel-Prefork-%{version}.tar.gz
BuildArch:      noarch
# oreon:deps
BuildRequires:  /usr/bin/make
BuildRequires:  perl(Class::Accessor::Lite)
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Install::ReadmeFromPod)
BuildRequires:  perl(Parallel::Scoreboard)
BuildRequires:  perl(Proc::Wait3)
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Signal::Mask)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
# /oreon:deps
%description
Parallel::Prefork is much like Parallel::ForkManager, but supports graceful
shutdown and run-time reconfiguration.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Parallel-Prefork-%{version}
rm -r inc
sed -i -e '/^inc\/*$/d' MANIFEST

%build

%{__perl} Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

%{__make} test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
