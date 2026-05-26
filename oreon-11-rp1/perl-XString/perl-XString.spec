Name:		perl-XString
Version:	0.005
Release:	18%{?dist}
Summary:	Isolated String helpers from B
License:	GPL-1.0-or-later OR Artistic-1.0-Perl
URL:		https://metacpan.org/release/XString
Source0:	https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/XString-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 f247f55c19aee6ba4a1ae73c0804259452e02ea85a9be07f8acf700a5138f884
%global source0_file XString-0.005.tar.gz
# oreon url source checksums end
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl-generators
BuildRequires:	perl-interpreter
BuildRequires:	perl(ExtUtils::MakeMaker) >= 6.76
# Module
BuildRequires:	perl(:VERSION) >= 5.10.0
BuildRequires:	perl(strict)
BuildRequires:	perl(warnings)
BuildRequires:	perl(XSLoader)
# Test Suite
BuildRequires:	perl(B)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::More) >= 0.88
# Optional Tests
BuildRequires:	perl(CPAN::Meta) >= 2.120900
BuildRequires:	perl(CPAN::Meta::Prereqs)
# Dependencies
Requires:	perl(XSLoader)

%description
XString provides the B string helpers in one isolated package. Right now only
cstring and perlstring are available.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/XString-0.005.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "f247f55c19aee6ba4a1ae73c0804259452e02ea85a9be07f8acf700a5138f884" || { echo "oreon: Source0 SHA256 mismatch for XString-0.005.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n XString-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/XString.pm
%{perl_vendorarch}/auto/XString/
%{_mandir}/man3/XString.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.005-18
- Prepare for Oreon 11 (RP1)
