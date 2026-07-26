%global source0_hash 1c176e8e1c01bbe86a7f3acde4473f0f034d410050246f2eba4cf68a08daf643

Name:           perl-Text-SimpleTable-AutoWidth
Version:        0.09
Release:        21%{?dist}
Summary:        Simple eye-candy ASCII tables with auto-width selection
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-SimpleTable-AutoWidth
Source0:        https://cpan.metacpan.org/authors/id/C/CU/CUB/Text-SimpleTable-AutoWidth-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(List::Util)
BuildRequires:  perl(Moo)
BuildRequires:  perl(Text::SimpleTable)
# Tests:
# English not used
# Pod::Coverage::TrustPod not used
BuildRequires:  perl(Test::More)
# Test::Pod 1.41 not used
# Test::Pod::Coverage 1.08 not used
# Optional tests:
# Test::Perl::Critic not used

%description
Simple eye-candy ASCII tables with auto-selection columns width, as seen
in Catalyst.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Text-SimpleTable-AutoWidth-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING RELEASE_TESTING TEST_POD
make test

%files
%license LICENSE
%doc README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
