%global source0_hash 87f4148aa0ff1d5e652723322eab7dafa3801c967d6f91ac9147a3c467b8a66a

Name:           perl-Safe-Isa
Version:        1.000010
Release:        23%{?dist}
Summary:        Call isa, can, does and DOES safely on things that may not be objects
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Safe-Isa
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/Safe-Isa-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-generators
BuildRequires:  perl-interpreter
BuildRequires:  perl(ExtUtils::MakeMaker)
# Module
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(Scalar::Util)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Test Suite
BuildRequires:  perl(Test::More) >= 0.82
BuildRequires:  perl(UNIVERSAL)
# Dependencies
# (none)

Provides:       perl(Safe::Isa)
%description
This module allows you to call isa, can, does and DOES safely on things that
may not be objects, without the risk of crashing.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Safe-Isa-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
%{_fixperms} -c %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/Safe/
%{_mandir}/man3/Safe::Isa.3*

%changelog
%autochangelog
