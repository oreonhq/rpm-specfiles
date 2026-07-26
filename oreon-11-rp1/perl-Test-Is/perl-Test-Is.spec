%global source0_hash fb9a959b7004d629f20d45c9965de59e80f46ab50453906bd1a97ff656419dbe

Name:           perl-Test-Is
Version:        20140823.1
Release:        29%{?dist}
Summary:        Skip test in a declarative way
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Test-Is
Source0:        https://cpan.metacpan.org/authors/id/D/DO/DOLMEN/Test-Is-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.6
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
# This can check only for Perl 5 versions
BuildRequires:  perl(:VERSION) < 6
# This is a plug-in into Test::More. It calls skip_all().
BuildRequires:  perl(Test::More) >= 0.88
# Tests:
BuildRequires:  perl(blib)
BuildRequires:  perl(File::Spec)
BuildRequires:  perl(IO::Handle)
BuildRequires:  perl(IPC::Open3)
# Optional tests:
BuildRequires:  perl(TAP::Harness)
# This can check only for Perl 5 versions
Requires:       perl(:VERSION) >= 5
Requires:       perl(:VERSION) < 6
# This is a plug-in into Test::More. It calls skip_all().
Requires:       perl(Test::More) >= 0.88

%description
This module is a simple way of following the specifications of the
environment variables available for Perl tests as defined as one of
the "Lancaster Consensus" at Perl QA Hackathon 2013. Those variables
(NONINTERACTIVE_TESTING, EXTENDED_TESTING) define which tests should
be skipped.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Test-Is-%{version}

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
