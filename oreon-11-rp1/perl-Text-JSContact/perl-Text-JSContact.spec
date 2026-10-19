%global source0_hash a87d471f26d7134794b8e780dee66b277ecd4fd09b9cbd1f0246574d92b2efff
Name:           perl-Text-JSContact
Version:        0.02
Release:        1%{?dist}
Summary:        Convert between vCard and JSContact
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Text-JSContact
Source0:        https://cpan.metacpan.org/authors/id/B/BR/BRONG/Text-JSContact-%{version}.tar.gz
BuildArch:      noarch
Requires:       perl(Encode)
Requires:       perl(JSON)
Requires:       perl(MIME::Base64)
Requires:       perl(Scalar::Util)
Requires:       perl(Text::VCardFast) >= 0.06
# oreon:deps
BuildRequires:  make
BuildRequires:  perl(:VERSION)
BuildRequires:  perl(Encode)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(JSON)
BuildRequires:  perl(JSON::XS)
BuildRequires:  perl(LWP::UserAgent)
BuildRequires:  perl(MIME::Base64)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(Text::VCardFast)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
# /oreon:deps
%description
Convert between vCard and JSContact using the Text::JSContact Perl module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir Text-JSContact-%{version}
%oreon_prep
%build

perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build
%install
%make_install
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} %{buildroot}/*
%oreon_autofiles main

%check

make test
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
