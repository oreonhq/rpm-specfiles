Name:           perl-XML-RegExp
Version:        0.04
Release:        37%{?dist}
Summary:        Regular expressions for XML tokens

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-RegExp
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-RegExp-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 df1990096036085c8e2d45904fe180f82bfed40f1a7e05243f334ea10090fc54
%global source0_file XML-RegExp-0.04.tar.gz
# oreon url source checksums end

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(vars)

%description
This package contains an utility module containing regular expressions
for the following XML tokens: BaseChar, Ideographic, Letter, Digit,
Extender, CombiningChar, NameChar, EntityRef, CharRef, Reference,
Name, NmToken, and AttValue.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/XML-RegExp-0.04.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "df1990096036085c8e2d45904fe180f82bfed40f1a7e05243f334ea10090fc54" || { echo "oreon: Source0 SHA256 mismatch for XML-RegExp-0.04.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n XML-RegExp-%{version}


%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}


%install
%{make_install}
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test



%files
%doc Changes README
%{perl_vendorlib}/XML/
%{_mandir}/man3/XML::RegExp.3*


%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.04-37
- Prepare for Oreon 11 (RP1)
