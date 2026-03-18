Name:           perl-String-CRC32
Version:        2.100
Release:        17%{?dist}
Summary:        Perl interface for cyclic redundancy check generation
License:        LicenseRef-Fedora-Public-Domain
URL:            https://metacpan.org/release/String-CRC32
Source0:        https://cpan.metacpan.org/modules/by-module/String/String-CRC32-%{version}.tar.gz
# Module Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker) >= 6.76
# Module Runtime
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
BuildRequires:  perl(XSLoader)
# Test Suite
# (no additional dependencies)
# Dependencies
# (no additional dependencies)

# Avoid perl object provides
%{?perl_default_filter}

%description
This packages provides a perl module to generate checksums from strings and
from files.

The checksums are the same as those calculated by ZMODEM, PKZIP, PICCHECK and
many others.

There's another perl module called String::CRC, which supports calculation of
CRC values of various widths (i.e. not just 32 bits), but the generated sums
differ from those of the programs mentioned above.

%prep
%setup -q -n String-CRC32-%{version}

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
%doc Changes README.md
%{perl_vendorarch}/String/
%{perl_vendorarch}/auto/String/
%{_mandir}/man3/String::CRC32.3*

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.100-17
- Prepare for Oreon 11 (RP1)
