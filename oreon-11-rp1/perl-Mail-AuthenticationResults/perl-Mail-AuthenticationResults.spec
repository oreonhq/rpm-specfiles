Name:           perl-Mail-AuthenticationResults
Version:        2.20260216
Release:        1%{?dist}
Summary:        Object Oriented Authentication-Results Headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-AuthenticationResults/
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/Mail-AuthenticationResults-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  make
BuildRequires:  perl >= 0:5.008
BuildRequires:  perl-generators
BuildRequires:  perl(base)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Clone)
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(JSON)
BuildRequires:  perl(lib)
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
BuildRequires:  perl(warnings)


%description
Object Oriented Authentication-Results email headers.


%prep
%setup -q -n Mail-AuthenticationResults-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%make_build


%install
%make_install
%{_fixperms} $RPM_BUILD_ROOT/*


%check
%make_build test


%files
%license LICENSE
%doc Changes dist.ini README README.md
%{perl_vendorlib}/Mail/
%{_mandir}/man3/Mail::AuthenticationResults*.3pm*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.20260216-1
- Prepare for Oreon 11 (RP1)
