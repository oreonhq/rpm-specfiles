Name:           perl-Text-Levenshtein-Damerau-XS
Version:        3.2
Release:        31%{?dist}
Summary:        XS Damerau Levenshtein edit distance
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-Levenshtein-Damerau-XS
Source0:        https://cpan.metacpan.org/authors/id/U/UG/UGEXE/Text-Levenshtein-Damerau-XS-%{version}.tar.gz
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(CPAN::Meta::Requirements) >= 2.120920
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(utf8)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
Requires:       perl(XSLoader)

%description
This is an XS implementation of the true Damerau Levenshtein edit distance
algorithm.

%prep
%setup -q -n Text-Levenshtein-Damerau-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README.pod examples
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Text*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.2-31
- Prepare for Oreon 11 (RP1)
