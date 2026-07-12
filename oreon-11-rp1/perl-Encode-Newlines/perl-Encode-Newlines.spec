%global source0_hash 34b31fcac8c8fdc821b9b3434a82d7133213ef74ccff255fe148a86af96837be

Name:           perl-Encode-Newlines
Version:        0.05
Release:        29%{?dist}
Summary:        Normalize line ending sequences
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/release/Encode-Newlines
Source0:        https://cpan.metacpan.org/authors/id/N/NE/NEILB/Encode-Newlines-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  make
BuildRequires:  perl-interpreter
BuildRequires:  perl-generators
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
# Run-time
BuildRequires:  perl(Carp)
BuildRequires:  perl(constant)
BuildRequires:  perl(Encode::Encoding)
BuildRequires:  perl(parent)
# Tests
BuildRequires:  perl(Encode)
BuildRequires:  perl(Test::More)
Requires:       perl(Carp)

Provides:       perl(Encode::Newlines)
%description
This module provides the CR, LF, CRLF and Native encodings, to aid in
normalizing line endings.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%setup -q -n Encode-Newlines-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%license LICENSE
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
