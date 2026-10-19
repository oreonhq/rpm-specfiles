%global source0_hash 06d948be8fbb4ed8854e70fc79cd50b9b3fb161e3feb6e3967c341ba572c1eae
Name:           perl-Test-RandomResult
Version:        0.001
Release:        1%{?dist}
Summary:        Test that results of a running code look random
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-RandomResult/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLANCAR/Test-RandomResult-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Exporter) >= 5.57
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}perl\\(Exporter\\)\\s*$
Provides:       perl(Test::RandomResult)
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
BuildRequires:  perl(Test2::API)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(blib)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Test that results of a running code look random

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Test-RandomResult-%{version}

%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}
%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
