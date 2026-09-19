%global source0_hash c9b1764643933eb1a3356906cc372d483a99416207a31df3e58ee9892d9922f9

Name:           perl-Algorithm-Annotate
Version:        0.10
Release:        53%{?dist}
Summary:        Represent a series of changes in annotate form
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Algorithm-Annotate
Source0:        https://cpan.metacpan.org/modules/by-module/Algorithm/Algorithm-Annotate-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Runtime
BuildRequires:  perl(Algorithm::Diff) >= 1.15
BuildRequires:  perl(strict)
# Tests
BuildRequires:  perl(Test::More)

%description
Algorithm::Annotate generates a list that is useful for generating output
simlar to cvs annotate.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Algorithm-Annotate-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
