%global source0_hash 1663c4d71754f0b0174b6d7e1f80c9690f3ba838b84385242dac2c500aac799c

# Perform optional tests
%bcond_without perl_Iterator_Simple_Lookahead_enables_optional_test

Name:           perl-Iterator-Simple-Lookahead
Version:        0.09
Release:        21%{?dist}
Summary:        Simple iterator with look-ahead and unget
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Iterator-Simple-Lookahead
Source0:        https://cpan.metacpan.org/authors/id/P/PS/PSCUST/Iterator-Simple-Lookahead-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.8
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  sed
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Class::Accessor) >= 0.51
BuildRequires:  perl(Iterator::Simple) >= 0.07
BuildRequires:  perl(Iterator::Simple::Iterator)
BuildRequires:  perl(overload)
# Tests:
BuildRequires:  perl(Test::More) >= 1.001014
%if %{with perl_Iterator_Simple_Lookahead_enables_optional_test}
# Optional tests:
BuildRequires:  perl(Pod::Coverage) >= 0.18
# Test::CheckManifest 1.42 not used
BuildRequires:  perl(Test::Pod) >= 1.22
BuildRequires:  perl(Test::Pod::Coverage) >= 1.08
%endif
Requires:       perl(Class::Accessor) >= 0.51
Requires:       perl(Iterator::Simple) >= 0.07

# Remove under-specified dependencies
%global __requires_exclude %{?__requires_exclude:%{__requires_exclude}|}^perl\\((Class::Accessor|Iterator::Simple)\\)$

%description
This Perl module encapsulates an iterator that allows the user to peek the Nth
element without consuming it or to push elements back to the iterated stream.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Iterator-Simple-Lookahead-%{version}
# Correct EOLs
for F in Changes; do
    sed -e 's/\r$//' < "$F" > "${F}.new"
    touch -r "$F" "${F}.new"
    mv "${F}.new" "$F"
done
%if %{without perl_Iterator_Simple_Lookahead_enables_optional_test}
for F in t/pod.t t/pod-coverage.t t/manifest.t; do
    rm "$F"
    sed -i "\|^$F|d" MANIFEST
done
%endif

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset RELEASE_TESTING
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
