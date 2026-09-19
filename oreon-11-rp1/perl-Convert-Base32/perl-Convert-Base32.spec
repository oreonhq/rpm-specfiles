%global source0_hash 4ba82c167c41f455aa8284738727e4c94a2ebcb1c4ce797f6fda07245a642115

Name:           perl-Convert-Base32
Version:        0.06
Release:        23%{?dist}
Summary:        Encoding and decoding of base32 strings
# Automatically converted from old format: GPL+ or Artistic - review is highly recommended.
License:        GPL-1.0-or-later OR Artistic-1.0-Perl
URL:            https://metacpan.org/pod/Convert::Base32
Source0:        http://www.cpan.org/modules/by-module/Convert/Convert-Base32-%{version}.tar.gz
BuildArch:      noarch

BuildRequires: make
BuildRequires:  perl-generators
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
BuildRequires:  perl(Carp)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)
Requires:       perl(Test::Exception)
Requires:       perl(Test::More)

%description
This module provides functions to convert string from / to Base32 encoding,
specified in RACE internet-draft. The Base32 encoding is designed to encode
non-ASCII characters in DNS-compatible host name parts.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n Convert-Base32-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

%changelog
%autochangelog
