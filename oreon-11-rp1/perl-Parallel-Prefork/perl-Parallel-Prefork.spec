%global source0_hash f1c1f48f1ae147a58bc88f9cb2f570d6bb15ea4c0d589abd4c3084ddc961596e

Name:           perl-Parallel-Prefork
Version:        0.18
Release:        29%{?dist}
Summary:        Simple prefork server framework
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Parallel-Prefork
Source0:        https://cpan.metacpan.org/authors/id/K/KA/KAZUHO/Parallel-Prefork-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  perl-generators
BuildRequires:  perl(Class::Accessor::Lite) >= 0.04
BuildRequires:  perl(Fcntl)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Parallel::Scoreboard)
BuildRequires:  perl(Proc::Wait3) >= 0.03
BuildRequires:  perl(Scope::Guard)
BuildRequires:  perl(Signal::Mask)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Requires)
BuildRequires:  perl(Test::SharedFork)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(warnings)

BuildRequires:  perl(inc::Module::Install)
BuildRequires:  perl(Module::Install::ReadmeFromPod)

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

%check
%{__make} test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
