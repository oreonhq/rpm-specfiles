%global source0_hash 5e0662d5a823ae081641f5ce82843111eec1831cd31f883a6c6de54afdf87c25

Name:           perl-Test2-Plugin-MemUsage
%global cpan_version 0.002003
Version:        0.2.3
Release:        18%{?dist}
Summary:        Test2 plugin that collects and displays memory usage information
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Plugin-MemUsage
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-MemUsage-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Test2::API) >= 1.302165
# Tests:
BuildRequires:  perl(Test2::Tools::Basic)
BuildRequires:  perl(Test2::Tools::Compare)
BuildRequires:  perl(Test2::Tools::Defer)
BuildRequires:  perl(vars)
Requires:       perl(Test2::API) >= 1.302165
# Removed from perl-Test2-Harness-0.001083
Conflicts:      perl-Test2-Harness < 0.001083

# Filter under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test2::API\\)$

%description
This Test2 plugin will collect memory usage information from /proc/PID/status
and display it for you when the test is done running.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Plugin-MemUsage-%{cpan_version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
