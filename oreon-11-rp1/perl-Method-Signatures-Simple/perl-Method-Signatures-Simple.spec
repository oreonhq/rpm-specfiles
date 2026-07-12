%global source0_hash c8cd7d471977cc8876044192abd98a81afddff2a26bb9a10bbe358efa371dadc

Name:           perl-Method-Signatures-Simple
Version:        1.07
Release:        31%{?dist}
Summary:        Basic method declarations with signatures, without source filters
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Method-Signatures-Simple
Source0:        https://cpan.metacpan.org/authors/id/R/RH/RHESA/Method-Signatures-Simple-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Runtime
BuildRequires:  perl(base)
BuildRequires:  perl(Devel::Declare::MethodInstaller::Simple)
# Tests only
BuildRequires:  perl(Test::More)

Provides:       perl(Method::Signatures::Simple)
%description
This module provides basic method and func keywords with simple
signatures. It's intentionally simple, and is supposed to be a
stepping stone for its bigger brothers MooseX::Method::Signatures and
Method::Signatures.  It only has a small benefit over regular subs,
so if you want more features, look at those modules.  But if you're
looking for a small amount of syntactic sugar, this might just be enough.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Method-Signatures-Simple-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
