%global source0_hash df1990096036085c8e2d45904fe180f82bfed40f1a7e05243f334ea10090fc54

Name:           perl-XML-RegExp
Version:        0.04
Release:        37%{?dist}
Summary:        Regular expressions for XML tokens

License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/XML-RegExp
Source0:        https://cpan.metacpan.org/authors/id/T/TJ/TJMATHER/XML-RegExp-%{version}.tar.gz

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
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
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
