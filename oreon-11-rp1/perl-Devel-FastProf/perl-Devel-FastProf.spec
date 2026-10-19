%global source0_hash 8811020f4404b1ad12d513afa2ee134493ab254ceba585fa7d4e11047cfc5d98
Name:           perl-Devel-FastProf
Version:        0.08
Release:        52%{?dist}
Summary:        Fast perl per-line profiler
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Devel-FastProf
Source0:        https://cpan.metacpan.org/authors/id/S/SA/SALVA/Devel-FastProf-%{version}.tar.gz
Requires:       perl(Sort::Key) >= 0.13
Requires:       perl(Time::HiRes) >= 1.74
%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(DB\\)$
%global __provides_exclude %__provides_exclude|^perl\\(main\\)$
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Sort::Key\\)$
# oreon:deps
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl(Carp)
BuildRequires:  perl(Config)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Time::HiRes)
BuildRequires:  perl(XSLoader)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Devel::FastProf is a perl per-line profiler. What that means is that it can
tell you how much time is spent on every line of a perl script (the
standard Devel::DProf is a per-subroutine profiler).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Devel-FastProf-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
