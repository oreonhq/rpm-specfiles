%global source0_hash a1ccd61ed05dc2bb3e706a01a455969d18d8744d59b71e11bee9c965c9370b72

# Perform optional tests
%bcond_without perl_Test2_Plugin_IOEvents_enables_optional_tests

Name:           perl-Test2-Plugin-IOEvents
%global cpan_version 0.001001
Version:        0.1.1
Release:        18%{?dist}
Summary:        Turn STDOUT and STDERR into Test2 events
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test2-Plugin-IOEvents
Source0:        https://cpan.metacpan.org/authors/id/E/EX/EXODIST/Test2-Plugin-IOEvents-%{cpan_version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8.9
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(Test2::API) >= 1.302165
# Tests:
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(Test2::V0) >= 0.000124
%if %{with perl_Test2_Plugin_IOEvents_enables_optional_tests}
# Optional tests:
BuildRequires:  perl(Capture::Tiny)
%endif
Requires:       perl(Test2::API) >= 1.302165

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\(Test2::API\\)$

%description
This Test2 plugin turns prints to STDOUT and STDERR objects (including warnings)
into the proper Test2 events.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test2-Plugin-IOEvents-%{cpan_version}

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
