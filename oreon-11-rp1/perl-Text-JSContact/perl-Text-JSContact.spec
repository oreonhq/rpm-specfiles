%global source0_hash a87d471f26d7134794b8e780dee66b277ecd4fd09b9cbd1f0246574d92b2efff

Name:           perl-Text-JSContact
Version:        0.02
Release:        1%{?dist}
Summary:        Convert between vCard and JSContact
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-JSContact
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Text-JSContact-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  make
BuildRequires:  perl(:VERSION) >= 5.014
BuildRequires:  perl(Encode)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::VCardFast) >= 0.06
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
Requires:       perl(Encode)
Requires:       perl(JSON)
Requires:       perl(MIME::Base64)
Requires:       perl(Scalar::Util)
Requires:       perl(Text::VCardFast) >= 0.06

%description
Convert between vCard and JSContact using the Text::JSContact Perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n Text-JSContact-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build

%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/Text/
%{_mandir}/man3/Text::JSContact.3*

%changelog
%autochangelog
