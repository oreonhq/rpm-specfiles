%global source0_hash fdc8684fc1e2ff13e01058cd2219b7f0c450ea1ed7ced75c05e236d6ec43f31e

Name:           perl-Crypt-Salsa20
Version:        0.03
Release:        31%{?dist}
Summary:        Encrypt data with the Salsa20 cipher
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Crypt-Salsa20

Source0:        https://cpan.metacpan.org/authors/id/C/CJ/CJM/Crypt-Salsa20-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)

# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(integer)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)

# Testing
BuildRequires:  perl(Digest::MD5)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(Test::More) >= 0.88

%description
Crypt::Salsa20 implements D. J. Bernstein's Salsa20 stream cipher (a.k.a.
Snuffle 2005) in Perl. For more information on Salsa20, see his page at
http://cr.yp.to/snuffle.html.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Crypt-Salsa20-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test AUTOMATED_TESTING=1

%files
%{!?_licensedir:%global license %doc}
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
