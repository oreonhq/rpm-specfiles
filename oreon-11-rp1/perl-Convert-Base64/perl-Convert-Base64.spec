Name:           perl-Convert-Base64
Version:        0.001
Release:        28%{?dist}
Summary:        Encoding and decoding of Base64 strings
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Convert-Base64
Source0:        https://cpan.metacpan.org/authors/id/R/RO/ROBN/Convert-Base64-%{version}.tar.gz
# oreon url source checksums begin
%global source0_sha256 bc99df7fe1c1ae615f82b40194e7d0bd2f42be6692de037fd6a267930b273ebb
%global source0_file Convert-Base64-0.001.tar.gz
# oreon url source checksums end
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.30
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time:
BuildRequires:  perl(Exporter)
BuildRequires:  perl(MIME::Base64)
# Tests:
BuildRequires:  perl(Test::More)

%description
This Perl module provides functions to convert strings to and from the Base64
encoding as described in RFC 4648.

%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/Convert-Base64-0.001.tar.gz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "bc99df7fe1c1ae615f82b40194e7d0bd2f42be6692de037fd6a267930b273ebb" || { echo "oreon: Source0 SHA256 mismatch for Convert-Base64-0.001.tar.gz" >&2; exit 1; })
# oreon verify url source checksums end
%setup -q -n Convert-Base64-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{make_install}
%{_fixperms} %{buildroot}/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 0.001-28
- Prepare for Oreon 11 (RP1)
