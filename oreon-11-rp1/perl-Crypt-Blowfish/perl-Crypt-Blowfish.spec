%global source0_hash 46b3431ffb6bf5b9cb359f79565d48407e652ad2b04fdf5ca62a69e7197a67b1

Summary:        XS Blowfish implementation for Perl
Name:           perl-Crypt-Blowfish
Version:        2.14
Release:        36%{?dist}
License:        BSD-Systemics-W3Works
URL:            https://metacpan.org/release/Crypt-Blowfish
Source0:        https://cpan.metacpan.org/modules/by-module/Crypt/Crypt-Blowfish-%{version}.tar.gz
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  gcc
BuildRequires:  glibc-headers
BuildRequires:  make
BuildRequires:  perl-devel
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Runt-time:
BuildRequires:  perl(Carp)
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
# Tests:
BuildRequires:  perl(Benchmark)
# Optional tests:
BuildRequires:  perl(Crypt::CBC) >= 1.22
# Dependencies:

Provides:       perl(Crypt::Blowfish)
Provides:       perl(Crypt::Blowfish)
%description
Crypt::Blowfish is an XS-based implementation of the Blowfish
cryptography algorithm designed by Bruce Schneier. It's designed to
take full advantage of Crypt::CBC when desired. Blowfish keys may be
up to 448 bits (56 bytes) long.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Crypt-Blowfish-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -name '*.bs' -empty -delete
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%license COPYRIGHT
%doc Changes README
%{perl_vendorarch}/auto/Crypt/
%{perl_vendorarch}/Crypt/
%{_mandir}/man3/Crypt::Blowfish.3*

%changelog
%autochangelog
