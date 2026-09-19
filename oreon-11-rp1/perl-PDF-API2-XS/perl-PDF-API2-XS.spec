%global source0_hash d0166abe469ee02d84c65bca561673acf89aca29dca5164def82375de1928ce9

Name:           perl-PDF-API2-XS
Version:        1.002
Release:        18%{?dist}
Summary:        Optional PDF::API2 add-on using XS to speed up expensive operations
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/PDF-API2-XS
Source0:        https://cpan.metacpan.org/authors/id/S/SS/SSIMMS/PDF-API2-XS-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(:VERSION) >= 5.10.0
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Exporter)
BuildRequires:  perl(XSLoader)
# Tests
BuildRequires:  perl(PDF::API2)
BuildRequires:  perl(Test::More)

%description
PDF::API2 will make use of this distribution, if it's installed, to speed
up some operations that are significantly faster in C than in Perl.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n PDF-API2-XS-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS" NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
unset AUTHOR_TESTING
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/PDF*
%{_mandir}/man3/*

%changelog
%autochangelog
