%global source0_hash c93566a0e9bbc9aab5998243ff8129d2389ed98cf2414bec88f5e5a57af4e7ee

Name:           perl-Math-BaseCnv
Version:        1.14
Release:        28%{?dist}
Summary:        Fast functions to CoNVert between number Bases

# Automatically converted from old format: GPLv3 - review is highly recommended.
License:        GPL-3.0-only
URL:            https://metacpan.org/release/Math-BaseCnv
Source0:        https://cpan.metacpan.org/authors/id/P/PI/PIP/Math-BaseCnv-%{version}.tgz

BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
# Run-time:
BuildRequires:  perl(base)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(Math::BigInt)
BuildRequires:  perl(Memoize)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Tests:
BuildRequires:  perl(Test)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(Test::Pod::Coverage)

%description
BaseCnv provides a few simple functions for converting between arbitrary
number bases. It is as fast as I currently know how to make it (of course
relying only on the lovely Perl). If you would rather utilize an object syntax
for number-base conversion, please see Ken Williams's
<Ken@Forum.Swarthmore.Edu> fine Math::BaseCalc module.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Math-BaseCnv-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README ex
%license LICENSE
%{perl_vendorlib}/*
%{_mandir}/man3/Math::BaseCnv.3pm.*
%{_bindir}/cnv

%changelog
%autochangelog
