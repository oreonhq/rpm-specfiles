%global source0_hash 493b909a98798668004a2ae486510dd603f858efbab8c50d931627ee8c40a5ac

Name:           perl-Lingua-EN-Numbers
Version:        2.03
Release:        29%{?dist}
Summary:        Turn "407" into "four hundred and seven", etc
License:        GPL-2.0-only
URL:            https://metacpan.org/release/Lingua-EN-Numbers
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Lingua-EN-Numbers-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::More) >= 0.88
BuildRequires:  perl(warnings)

%description
Lingua::EN::Numbers turns numbers into English text. It exports (upon
request) two functions, num2en and num2en_ordinal. Each takes a scalar
value and returns a scalar value. The return value is the English text
expressing that number; or if what you provided wasn't a number, then they
return undefined.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Lingua-EN-Numbers-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Lingua
%{_mandir}/man3/Lingua::EN::Numbers*

%changelog
%autochangelog
