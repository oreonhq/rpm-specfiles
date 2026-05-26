Name:           perl-Mail-AuthenticationResults
Version:        2.20260216
Release:        1%{?dist}
Summary:        Object Oriented Authentication-Results Headers
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Mail-AuthenticationResults/
Source0:        https://cpan.metacpan.org/authors/id/M/MB/MBRADSHAW/Mail-AuthenticationResults-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 9a53c1b7c7f160e898e6cb5be9948d64141d2819ade2d7a873d0e87d1e83f666
%global source0_file Mail-AuthenticationResults-2.20260216.tar.gz
# oreon url source checksums end
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
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Mail-AuthenticationResults-2.20260216.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "9a53c1b7c7f160e898e6cb5be9948d64141d2819ade2d7a873d0e87d1e83f666" || { echo "oreon: Source0 SHA256 mismatch for Mail-AuthenticationResults-2.20260216.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
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
