%global source0_hash 8404f661f71b0580d9945561294790dd1738f6252d363385a73ecb334b4e36d5

Name:           perl-Test-Log-Dispatch
Version:        0.03
Release:        44%{?dist}
Summary:        Test what you are logging
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Log-Dispatch
Source0:        https://cpan.metacpan.org/authors/id/J/JS/JSWARTZ/Test-Log-Dispatch-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{__make}
BuildRequires:  %{__perl}

BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Log::Dispatch::Array)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Test::Tester)

BuildRequires:  perl(inc::Module::Install)

%description
Test::Log::Dispatch is a Log::Dispatch object that keeps track of
everything logged to it in memory, and provides convenient tests against
what has been logged.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Log-Dispatch-%{version}
rm -r inc

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps NO_PACKLIST=1 NO_PERLLOCAL=1
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
